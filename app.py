import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Setup Data
# In a real app, use: df = pd.read_csv('financial_data.csv')
data = {
    'Month': ['Oct', 'Nov', 'Dec', 'Jan', 'Feb'],
    'Revenue': [95000, 98000, 115000, 105000, 142000],
    'Expenses': [120000, 125000, 130000, 128000, 132000]
}
df = pd.DataFrame(data)
starting_cash = 500000 

# 2. Calculations
df['Net_Cash_Flow'] = df['Revenue'] - df['Expenses']
avg_burn = abs(df['Net_Cash_Flow'].mean()) if df['Net_Cash_Flow'].mean() < 0 else 0
runway_months = starting_cash / avg_burn if avg_burn > 0 else "∞ (Profitable)"

# 3. Modern UI Header
st.set_page_config(page_title="Financial Health", layout="wide")
st.title("🛡️ Financial Runway Analysis")

# 4. KPI Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Cash on Hand", f"${starting_cash:,}", "Liquidity")
with col2:
    st.metric("Avg Monthly Burn", f"${avg_burn:,.0f}", "-3.2%", delta_color="inverse")
with col3:
    color = "normal" if isinstance(runway_months, str) or runway_months > 12 else "inverse"
    st.metric("Runway (Months)", f"{runway_months:.1f}" if not isinstance(runway_months, str) else runway_months, "Safety Margin", delta_color=color)

# 5. Visualizing the "Cash Decay" (Modern Area Chart)
st.subheader("Projected Cash Depletion")
months_proj = list(range(13))
cash_proj = [starting_cash - (avg_burn * m) for m in months_proj]

fig = go.Figure()
fig.add_trace(go.Scatter(x=months_proj, y=cash_proj, fill='tozeroy', 
                         line_color='#FF4B4B', name='Cash Reserves'))
fig.update_layout(template="plotly_dark", xaxis_title="Months from Now", yaxis_title="Cash ($)")
st.plotly_chart(fig, use_container_width=True)
