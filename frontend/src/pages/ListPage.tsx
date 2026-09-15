import { useQuery } from '@tanstack/react-query';
import { api } from '../api/client';
import type { RecordRow } from '../types/crm';

export function ListPage({ title, endpoint }: { title: string; endpoint: string }) {
  const { data, isLoading, error } = useQuery({ queryKey: [endpoint], queryFn: async () => (await api.get(endpoint)).data });
  const rows: RecordRow[] = Array.isArray(data) ? data : data?.results ?? [];
  return <div className="space-y-4"><div className="flex flex-wrap items-center justify-between gap-3"><h1 className="text-2xl font-semibold">{title}</h1><button className="rounded-md bg-coral px-4 py-2 text-sm font-medium text-white">New</button></div>
    <div className="rounded-md border bg-white dark:border-slate-800 dark:bg-slate-950"><div className="border-b p-3 dark:border-slate-800"><input className="w-full rounded-md border px-3 py-2 text-sm dark:border-slate-700 dark:bg-slate-900" placeholder={`Filter ${title.toLowerCase()}`} /></div>
    {isLoading && <div className="p-4 text-sm">Loading...</div>}{error && <div className="p-4 text-sm text-red-600">Could not load records.</div>}
    <div className="overflow-x-auto"><table className="w-full text-left text-sm"><thead className="bg-slate-50 dark:bg-slate-900"><tr><th className="p-3">Name</th><th className="p-3">Status</th><th className="p-3">Value</th><th className="p-3">Updated</th></tr></thead><tbody>{rows.map((row) => <tr key={row.id} className="border-t dark:border-slate-800"><td className="p-3 font-medium">{row.name ?? row.title ?? row.email}</td><td className="p-3">{row.status ?? row.stage ?? 'active'}</td><td className="p-3">{row.value ?? '-'}</td><td className="p-3">{row.updated_at ? new Date(row.updated_at).toLocaleDateString() : '-'}</td></tr>)}{!rows.length && !isLoading && <tr><td className="p-4 text-slate-500" colSpan={4}>No records yet.</td></tr>}</tbody></table></div></div></div>;
}
