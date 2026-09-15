import { Navigate, Route, Routes } from 'react-router-dom';
import { AppLayout } from '../layouts/AppLayout';
import { Dashboard } from '../pages/Dashboard';
import { ListPage } from '../pages/ListPage';
import { Login, Register, Auth } from '../pages/AuthPages';

export function AppRoutes() {
  return <Routes>
    <Route path="/login" element={<Login />} /><Route path="/register" element={<Register />} /><Route path="/forgot-password" element={<Auth title="Forgot password" />} /><Route path="/reset-password" element={<Auth title="Reset password" />} /><Route path="/verify-email" element={<Auth title="Verify email" />} />
    <Route element={<AppLayout />}>
      <Route path="/" element={<Navigate to="/dashboard" replace />} /><Route path="/dashboard" element={<Dashboard />} />
      <Route path="/companies" element={<ListPage title="Companies" endpoint="/companies/" />} /><Route path="/contacts" element={<ListPage title="Contacts" endpoint="/contacts/" />} /><Route path="/leads" element={<ListPage title="Leads" endpoint="/leads/" />} /><Route path="/deals" element={<ListPage title="Deals" endpoint="/deals/" />} /><Route path="/products" element={<ListPage title="Products" endpoint="/products/" />} /><Route path="/requests" element={<ListPage title="Requests" endpoint="/requests/" />} /><Route path="/tasks" element={<ListPage title="Tasks" endpoint="/tasks/" />} /><Route path="/projects" element={<ListPage title="Projects" endpoint="/projects/" />} /><Route path="/inbox" element={<ListPage title="Inbox" endpoint="/emails/messages/" />} /><Route path="/campaigns" element={<ListPage title="Campaigns" endpoint="/campaigns/" />} /><Route path="/segments" element={<ListPage title="Segments" endpoint="/campaigns/segments/" />} /><Route path="/analytics/:kind" element={<Dashboard />} /><Route path="/settings" element={<ListPage title="Settings" endpoint="/organizations/" />} />
    </Route>
  </Routes>;
}
