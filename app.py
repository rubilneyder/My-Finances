import React, { useState, useMemo } from 'react';
import { 
  TrendingUp, 
  TrendingDown, 
  Wallet, 
  CreditCard, 
  PieChart, 
  ArrowUpRight, 
  ArrowDownRight, 
  Plus, 
  Search,
  LayoutDashboard,
  ArrowRightLeft,
  Bell,
  Settings,
  MapPin,
  Clock,
  BarChart3,
  Percent,
  ChevronRight,
  Filter,
  MoreVertical
} from 'lucide-react';

// Custom Rubymed Logo Component based on uploaded image
const RubymedLogo = ({ className = "w-10 h-10" }) => (
  <svg viewBox="0 0 100 100" className={className} fill="none" xmlns="http://www.w3.org/2000/svg">
    {/* Blue Cross (Lower Layer) */}
    <path 
      d="M42 28H54V42H68V54H54V68H42V54H28V42H42V28Z" 
      stroke="#004899" 
      strokeWidth="2.5" 
      strokeLinejoin="round"
    />
    {/* Red Cross (Upper Layer - Offset) */}
    <path 
      d="M46 32H58V46H72V58H58V72H46V58H32V46H46V32Z" 
      stroke="#e41520" 
      strokeWidth="2.5" 
      strokeLinejoin="round"
    />
  </svg>
);

const App = () => {
  // Multi-Revenue Stream Data per Location
  const locationPerformance = [
    { name: 'Downtown HQ', cashSales: 32000, creditSales: 13000, deposits: 31500, avgExpense: 12000, status: 'Optimal' },
    { name: 'North Branch', cashSales: 21000, creditSales: 7000, deposits: 20800, avgExpense: 8500, status: 'Warning' },
    { name: 'East Side', cashSales: 14500, creditSales: 5000, deposits: 13200, avgExpense: 6200, status: 'Optimal' },
    { name: 'West Mall', cashSales: 26000, creditSales: 6000, deposits: 25500, avgExpense: 9800, status: 'Optimal' },
  ];

  // AR Aging for Main Location (Downtown HQ)
  const arAging = [
    { period: '0-30 Days', amount: 12450, percentage: 64, color: 'bg-[#004899]' },
    { period: '31-60 Days', amount: 4200, percentage: 21, color: 'bg-slate-400' },
    { period: '61-90 Days', amount: 1850, percentage: 10, color: 'bg-slate-600' },
    { period: '90+ Days', amount: 940, percentage: 5, color: 'bg-[#e41520]' },
  ];

  const stats = [
    { label: 'Gross Revenue', amount: '$124,500', trend: '+8.2%', isPositive: true, icon: BarChart3 },
    { label: 'Cash Deposits', amount: '$91,000', trend: '+5.4%', isPositive: true, icon: Wallet },
    { label: 'Open AR', amount: '$19,440', trend: '+1.2%', isPositive: false, icon: Clock },
    { label: 'Collection Rate', amount: '92.4%', trend: '+2.1%', isPositive: true, icon: Percent },
  ];

  return (
    <div className="flex flex-col h-screen bg-[#F8FAFC] text-[#1E293B] font-sans selection:bg-[#004899]/10 overflow-hidden">
      {/* Refined Header - Now as the Primary Branding Bar */}
      <header className="h-20 bg-[#ffffff] border-b border-slate-200 flex items-center justify-between px-8 shrink-0 z-20 shadow-sm">
        <div className="flex items-center gap-8">
          {/* Logo Section */}
          <div className="flex items-center gap-1">
            <div className="bg-[#ffffff] rounded-xl flex items-center justify-center mr-2">
              <RubymedLogo className="w-10 h-10" />
            </div>
            <span className="text-xl font-black tracking-tighter text-[#004899]">RUBYMED</span>
          </div>

          {/* Search */}
          <div className="hidden md:block relative w-80">
            <Search className="absolute left-4 top-1/2 -translate-y-1/2 text-slate-400 w-4 h-4" />
            <input 
              type="text" 
              placeholder="Search financials..."
              className="w-full pl-11 pr-4 py-2 bg-slate-100 border-none rounded-xl text-sm focus:ring-2 focus:ring-[#004899]/20 outline-none transition-all placeholder:text-slate-400 font-medium"
            />
          </div>
        </div>
        
        <div className="flex items-center gap-4">
          <nav className="hidden lg:flex items-center gap-2 mr-4">
             <button className="px-4 py-2 text-sm font-bold text-[#004899] bg-[#004899]/5 rounded-xl">Overview</button>
             <button className="px-4 py-2 text-sm font-bold text-slate-500 hover:bg-slate-50 rounded-xl transition-colors">Locations</button>
             <button className="px-4 py-2 text-sm font-bold text-slate-500 hover:bg-slate-50 rounded-xl transition-colors">Reports</button>
          </nav>

          <div className="flex items-center gap-4">
            <button className="p-2.5 text-slate-500 hover:bg-slate-100 rounded-xl transition-colors relative">
              <Bell className="w-5 h-5" />
              <span className="absolute top-2.5 right-2.5 w-2 h-2 bg-[#e41520] rounded-full border-2 border-white"></span>
            </button>
            <div className="h-6 w-px bg-slate-200 mx-1"></div>
            <div className="flex items-center gap-3 pl-2 cursor-pointer hover:opacity-80 transition-opacity">
              <div className="text-right hidden sm:block">
                <p className="text-sm font-bold text-slate-900 leading-none">Financial Controller</p>
                <p className="text-[11px] font-medium text-[#004899] mt-1 uppercase tracking-wider">Group HQ</p>
              </div>
              <div className="w-10 h-10 rounded-xl bg-[#004899] flex items-center justify-center text-white font-bold text-xs shadow-lg shadow-[#004899]/20">
                RM
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-1 overflow-y-auto bg-[#F8FAFC]">
        <div className="p-8 lg:p-12 max-w-[1600px] mx-auto space-y-10">
          
          {/* Welcome/Page Header */}
          <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
            <div>
              <div className="flex items-center gap-2 mb-2">
                <span className="px-2 py-0.5 rounded bg-emerald-100 text-emerald-700 text-[10px] font-black uppercase tracking-widest">Live Sync</span>
                <span className="text-slate-400 text-xs font-medium">Updated 2 mins ago</span>
              </div>
              <h1 className="text-4xl font-black tracking-tight text-slate-900">Financial Dashboard</h1>
              <p className="text-slate-500 mt-1.5 font-medium text-lg">Real-time liquidity and revenue performance across Rubymed operational nodes.</p>
            </div>
            <div className="flex gap-3">
              <button className="px-6 py-3 bg-[#ffffff] border border-slate-200 rounded-2xl text-sm font-bold text-slate-600 hover:bg-slate-50 transition-all flex items-center gap-2 shadow-sm">
                <Filter className="w-4 h-4" /> Filter Views
              </button>
              <button className="px-6 py-3 bg-[#004899] text-[#ffffff] rounded-2xl text-sm font-bold hover:bg-[#003673] shadow-xl shadow-[#004899]/20 transition-all flex items-center gap-2">
                <Plus className="w-4 h-4" /> New Transaction
              </button>
            </div>
          </div>

          {/* Stats Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {stats.map((stat, idx) => (
              <div key={idx} className="bg-[#ffffff] p-8 rounded-[2.5rem] border border-slate-100 shadow-sm hover:shadow-xl hover:shadow-slate-200/40 transition-all group">
                <div className="flex items-center justify-between mb-6">
                  <div className="bg-slate-50 p-4 rounded-2xl group-hover:bg-[#004899]/5 transition-colors">
                    <stat.icon className="w-6 h-6 text-slate-600 group-hover:text-[#004899] transition-colors" />
                  </div>
                  <div className={`flex items-center gap-1 text-[11px] font-black px-3 py-1.5 rounded-xl ${stat.isPositive ? 'bg-emerald-50 text-emerald-600' : 'bg-[#e41520]/5 text-[#e41520]'}`}>
                    {stat.isPositive ? <ArrowUpRight className="w-3 h-3" /> : <ArrowDownRight className="w-3 h-3" />}
                    {stat.trend}
                  </div>
                </div>
                <p className="text-slate-400 text-[10px] font-black uppercase tracking-[0.15em]">{stat.label}</p>
                <h3 className="text-4xl font-black text-slate-900 mt-1.5">{stat.amount}</h3>
              </div>
            ))}
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-3 gap-10">
            {/* Detailed Location Breakdown */}
            <div className="lg:col-span-2 bg-[#ffffff] rounded-[2.5rem] border border-slate-100 shadow-sm overflow-hidden flex flex-col">
              <div className="p-8 border-b border-slate-50 flex items-center justify-between">
                <div>
                  <h2 className="font-black text-2xl text-slate-900 tracking-tight">Clinic Performance Metrics</h2>
                  <p className="text-sm text-slate-400 mt-0.5">Revenue breakdown by payment modality</p>
                </div>
                <button className="text-[#004899] p-2 hover:bg-[#004899]/5 rounded-xl transition-colors">
                  <MoreVertical className="w-5 h-5" />
                </button>
              </div>
              <div className="flex-1 overflow-x-auto">
                <table className="w-full text-left min-w-[600px]">
                  <thead>
                    <tr className="text-slate-400 text-[10px] font-black uppercase tracking-[0.2em]">
                      <th className="px-10 py-6">Operational Node</th>
                      <th className="px-6 py-6 text-right">Cash / Credit</th>
                      <th className="px-6 py-6 text-right">Settled Deposits</th>
                      <th className="px-6 py-6 text-right">Node Expense</th>
                      <th className="px-10 py-6 text-center">Status</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-50">
                    {locationPerformance.map((loc, idx) => (
                      <tr key={idx} className="hover:bg-slate-50/50 transition-colors group">
                        <td className="px-10 py-6">
                          <div className="flex flex-col">
                            <span className="font-black text-slate-900 text-sm tracking-tight">{loc.name}</span>
                            <span className="text-[10px] text-[#004899] font-bold uppercase mt-0.5">Active Center</span>
                          </div>
                        </td>
                        <td className="px-6 py-6 text-right">
                          <div className="flex flex-col items-end">
                            <span className="text-sm font-black text-slate-800">${loc.cashSales.toLocaleString()}</span>
                            <span className="text-[11px] font-bold text-[#004899]/60">${loc.creditSales.toLocaleString()} CR</span>
                          </div>
                        </td>
                        <td className="px-6 py-6 text-right">
                          <span className="inline-block px-4 py-1.5 bg-emerald-50 text-emerald-700 text-xs font-black rounded-xl border border-emerald-100">
                            ${loc.deposits.toLocaleString()}
                          </span>
                        </td>
                        <td className="px-6 py-6 text-right font-black text-sm text-[#e41520]/80">
                          ${loc.avgExpense.toLocaleString()}
                        </td>
                        <td className="px-10 py-6 text-center">
                          <div className={`h-2.5 w-2.5 rounded-full mx-auto ${loc.status === 'Optimal' ? 'bg-[#004899]' : 'bg-[#e41520] animate-pulse'}`}></div>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Claims Aging Report */}
            <div className="bg-[#0F172A] text-[#ffffff] p-10 rounded-[2.5rem] shadow-2xl shadow-slate-300 flex flex-col relative overflow-hidden">
              <div className="absolute top-0 right-0 w-48 h-48 bg-[#004899]/10 rounded-full -mr-24 -mt-24 blur-3xl"></div>
              <div className="absolute bottom-0 left-0 w-48 h-48 bg-[#e41520]/5 rounded-full -ml-24 -mb-24 blur-3xl"></div>
              
              <div className="mb-10 relative z-10">
                <div className="flex items-center gap-3 mb-3">
                  <div className="p-2 bg-[#ffffff]/10 rounded-lg">
                    <Clock className="w-5 h-5 text-[#004899]" />
                  </div>
                  <span className="text-[10px] font-black uppercase tracking-[0.25em] text-slate-400">Aging Intelligence</span>
                </div>
                <h2 className="font-black text-3xl tracking-tight">Receivables</h2>
                <p className="text-slate-400 text-sm mt-1.5 font-medium italic">"Current collection cycle: 28.4 days"</p>
              </div>
              
              <div className="space-y-8 relative z-10 flex-1">
                {arAging.map((age, idx) => (
                  <div key={idx} className="group cursor-pointer">
                    <div className="flex justify-between items-end text-sm mb-3">
                      <span className="font-black text-slate-400 group-hover:text-[#ffffff] transition-colors">{age.period}</span>
                      <div className="text-right">
                        <span className="block text-xs font-black text-slate-500 mb-0.5">{age.percentage}%</span>
                        <span className="font-black text-lg text-[#ffffff] tracking-tight">${age.amount.toLocaleString()}</span>
                      </div>
                    </div>
                    <div className="w-full bg-slate-800/50 h-3 rounded-full overflow-hidden p-[2px]">
                      <div 
                        className={`${age.color} h-full rounded-full transition-all duration-1000 ease-in-out`} 
                        style={{ width: `${age.percentage}%` }}
                      ></div>
                    </div>
                  </div>
                ))}
              </div>

              <div className="pt-8 border-t border-slate-800 mt-10 relative z-10">
                <button className="w-full bg-[#ffffff] text-[#0F172A] p-5 rounded-2xl flex justify-between items-center hover:bg-slate-50 transition-all group shadow-xl">
                  <div className="text-left">
                    <p className="text-[10px] font-black text-[#004899] uppercase tracking-[0.2em] mb-0.5">Consolidated Total</p>
                    <p className="text-2xl font-black tracking-tighter">$19,440.00</p>
                  </div>
                  <div className="w-12 h-12 rounded-xl bg-[#0F172A] flex items-center justify-center text-[#ffffff] group-hover:bg-[#e41520] transition-colors">
                    <ChevronRight className="w-6 h-6" />
                  </div>
                </button>
              </div>
            </div>
          </div>

          {/* Large Visualization Section */}
          <div className="bg-[#ffffff] p-12 rounded-[3rem] border border-slate-100 shadow-sm relative overflow-hidden">
            <div className="flex flex-col md:flex-row md:items-center justify-between mb-16 gap-4">
              <div>
                <h3 className="text-2xl font-black text-slate-900 tracking-tight">Operational Efficiency</h3>
                <p className="text-slate-400 text-sm font-medium mt-1">Comparison between Gross Sales and Direct Node Expenses.</p>
              </div>
              <div className="flex flex-wrap gap-6 text-[10px] font-black uppercase tracking-widest bg-slate-50 p-4 rounded-2xl">
                <div className="flex items-center gap-2.5"><div className="w-3.5 h-3.5 bg-[#004899] rounded-sm"></div> Cash Revenue</div>
                <div className="flex items-center gap-2.5"><div className="w-3.5 h-3.5 bg-[#004899]/30 rounded-sm"></div> Insurance / AR</div>
                <div className="flex items-center gap-2.5"><div className="w-3.5 h-3.5 bg-[#e41520] rounded-sm"></div> OpEx</div>
              </div>
            </div>

            <div className="h-80 flex items-end gap-6 md:gap-16 px-4">
              {locationPerformance.map((loc, idx) => {
                const maxVal = 55000;
                return (
                  <div key={idx} className="flex-1 flex flex-col items-center gap-6 h-full justify-end group">
                    <div className="relative flex w-full justify-center gap-4 h-full items-end">
                      {/* Revenue Stack */}
                      <div className="w-12 flex flex-col justify-end h-full relative group/bar">
                        <div 
                          className="bg-[#004899]/20 rounded-t-lg w-full transition-all group-hover/bar:bg-[#004899]/40" 
                          style={{ height: `${(loc.creditSales / maxVal) * 100}%` }}
                        ></div>
                        <div 
                          className="bg-[#004899] w-full shadow-lg shadow-[#004899]/10" 
                          style={{ height: `${(loc.cashSales / maxVal) * 100}%` }}
                        ></div>
                        <div className="absolute -top-12 left-1/2 -translate-x-1/2 bg-slate-900 text-[#ffffff] px-3 py-1.5 rounded-lg text-xs font-black opacity-0 group-hover/bar:opacity-100 transition-all translate-y-2 group-hover/bar:translate-y-0 shadow-xl whitespace-nowrap z-10">
                          ${(loc.cashSales + loc.creditSales).toLocaleString()} Total
                        </div>
                      </div>
                      {/* Expense Bar */}
                      <div className="w-12 h-full flex flex-col justify-end group/exp">
                        <div 
                          className="bg-[#e41520]/60 rounded-t-lg transition-all group-hover/exp:bg-[#e41520] shadow-lg shadow-[#e41520]/5" 
                          style={{ height: `${(loc.avgExpense / maxVal) * 100}%` }}
                        ></div>
                        <div className="absolute -top-12 left-1/2 -translate-x-1/2 bg-[#e41520] text-[#ffffff] px-3 py-1.5 rounded-lg text-xs font-black opacity-0 group-hover/exp:opacity-100 transition-all translate-y-2 group-hover/exp:translate-y-0 shadow-xl whitespace-nowrap z-10">
                          ${loc.avgExpense.toLocaleString()} Exp
                        </div>
                      </div>
                    </div>
                    <div className="text-center">
                      <span className="text-sm font-black text-slate-800 block tracking-tight">{loc.name}</span>
                      <span className="text-[10px] font-black text-[#004899] uppercase tracking-tighter opacity-60">Node RM-{(idx + 1).toString().padStart(2, '0')}</span>
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default App;
