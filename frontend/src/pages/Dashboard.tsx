import { useQuery } from '@tanstack/react-query';
import { Bar, BarChart, CartesianGrid, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts';
import { api } from '../api/client';
import type { DashboardMetrics } from '../types/crm';

const metricLabels: [keyof DashboardMetrics, string][] = [['total_leads','Total leads'], ['open_deals','Open deals'], ['won_deals','Won deals'], ['lost_deals','Lost deals'], ['pipeline_value','Pipeline value'], ['forecast_revenue','Forecast revenue'], ['pending_tasks','Pending tasks'], ['open_requests','Open requests']];

export function Dashboard() {
  const { data, isLoading } = useQuery({ queryKey: ['dashboard'], queryFn: async () => (await api.get<DashboardMetrics>('/analytics/dashboard/')).data });
  if (isLoading || !data) return <div className="text-sm">Loading dashboard...</div>;
  return <div className="space-y-6">
    <div><h1 className="text-2xl font-semibold">Dashboard</h1><p className="text-sm text-slate-500">Live metrics from tenant-scoped API queries.</p></div>
    <section className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">{metricLabels.map(([key,label]) => <div className="rounded-md border bg-white p-4 dark:border-slate-800 dark:bg-slate-950" key={String(key)}><div className="text-sm text-slate-500">{label}</div><div className="mt-2 text-2xl font-semibold">{String(data[key] ?? 0)}</div></div>)}</section>
    <section className="grid gap-4 xl:grid-cols-2">
      <div className="rounded-md border bg-white p-4 dark:border-slate-800 dark:bg-slate-950"><h2 className="mb-4 font-semibold">Deal Pipeline</h2><ResponsiveContainer width="100%" height={260}><BarChart data={data.deals_by_stage}><CartesianGrid strokeDasharray="3 3"/><XAxis dataKey="stage"/><YAxis/><Tooltip/><Bar dataKey="value" fill="#2f9d8f"/></BarChart></ResponsiveContainer></div>
      <div className="rounded-md border bg-white p-4 dark:border-slate-800 dark:bg-slate-950"><h2 className="mb-4 font-semibold">Lead Sources</h2><ResponsiveContainer width="100%" height={260}><LineChart data={data.leads_by_source}><CartesianGrid strokeDasharray="3 3"/><XAxis dataKey="source"/><YAxis/><Tooltip/><Line type="monotone" dataKey="count" stroke="#dc5f4d" strokeWidth={3}/></LineChart></ResponsiveContainer></div>
    </section>
  </div>;
}
