import { NavLink, Outlet } from 'react-router-dom';
import { Bell, Building2, ChartNoAxesCombined, CheckSquare, Inbox, LayoutDashboard, Moon, Search, Settings, Sun } from 'lucide-react';
import { useState } from 'react';

const groups = [
  ['Main', [['Dashboard', '/dashboard', LayoutDashboard]]],
  ['CRM', [['Companies', '/companies', Building2], ['Contacts', '/contacts', Building2], ['Leads', '/leads', Search], ['Deals', '/deals', ChartNoAxesCombined], ['Products', '/products', Building2], ['Requests', '/requests', Inbox]]],
  ['Work', [['Tasks', '/tasks', CheckSquare], ['Projects', '/projects', CheckSquare]]],
  ['Comms', [['Inbox', '/inbox', Inbox], ['Campaigns', '/campaigns', Inbox], ['Segments', '/segments', Search]]],
  ['Admin', [['Analytics', '/analytics/sales', ChartNoAxesCombined], ['Settings', '/settings', Settings]]],
] as const;

export function AppLayout() {
  const [dark, setDark] = useState(false);
  document.documentElement.classList.toggle('dark', dark);
  return <div className="min-h-screen lg:flex">
    <aside className="bg-ink text-white lg:w-72">
      <div className="flex h-16 items-center px-5 text-xl font-semibold">PulseCRM</div>
      <nav className="space-y-5 px-3 pb-6">
        {groups.map(([label, links]) => <section key={label}><div className="px-3 pb-2 text-xs uppercase tracking-wide text-slate-300">{label}</div>{links.map(([name, href, Icon]) => <NavLink key={href} to={href} className={({isActive}) => `mb-1 flex items-center gap-3 rounded-md px-3 py-2 text-sm ${isActive ? 'bg-coral text-white' : 'text-slate-200 hover:bg-white/10'}`}><Icon size={18}/>{name}</NavLink>)}</section>)}
      </nav>
    </aside>
    <main className="min-w-0 flex-1">
      <header className="flex h-16 items-center gap-3 border-b bg-white px-4 dark:border-slate-800 dark:bg-slate-950">
        <div className="relative max-w-xl flex-1"><Search className="absolute left-3 top-2.5" size={18}/><input className="w-full rounded-md border py-2 pl-10 pr-3 text-sm dark:border-slate-700 dark:bg-slate-900" placeholder="Search CRM records" /></div>
        <button className="rounded-md border p-2 dark:border-slate-700"><Bell size={18}/></button>
        <button className="rounded-md border p-2 dark:border-slate-700" onClick={() => setDark(!dark)}>{dark ? <Sun size={18}/> : <Moon size={18}/>}</button>
      </header>
      <div className="p-4 lg:p-6"><Outlet /></div>
    </main>
  </div>;
}
