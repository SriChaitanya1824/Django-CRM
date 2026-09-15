import axios from 'axios';
export const api = axios.create({ baseURL: import.meta.env.VITE_API_URL ?? 'http://localhost:8000/api/v1' });
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('pulsecrm.access');
  const organization = localStorage.getItem('pulsecrm.organization');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  if (organization) config.headers['X-Organization-ID'] = organization;
  return config;
});
