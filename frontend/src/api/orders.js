import apiClient from './client'

export const ordersApi = {
  create: (data) => apiClient.post('/orders', data),
  getMyOrders: (params = {}) => apiClient.get('/orders/my', { params }),
  getMy: (params = {}) => apiClient.get('/orders/my', { params }),
  getAll: (params = {}) => apiClient.get('/orders', { params }),
  getById: (id) => apiClient.get(`/orders/${id}`),
  updateStatus: (id, status) => apiClient.put(`/orders/${id}/status`, { status }),
}
