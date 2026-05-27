import apiClient from './client'

export const menuApi = {
  getItems: (params = {}) => apiClient.get('/menu-items', { params }),
  getAll: (params = {}) => apiClient.get('/menu-items', { params }),
  getById: (id) => apiClient.get(`/menu-items/${id}`),
  getReviews: (id) => apiClient.get(`/menu-items/${id}/reviews`),
  create: (data) => apiClient.post('/menu-items', data),
  update: (id, data) => apiClient.put(`/menu-items/${id}`, data),
  delete: (id) => apiClient.delete(`/menu-items/${id}`),
}
