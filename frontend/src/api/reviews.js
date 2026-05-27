import apiClient from './client'

export const reviewsApi = {
  getAll: (params = {}) => apiClient.get('/reviews', { params }),
  create: (data) => apiClient.post('/reviews', data),
  delete: (id) => apiClient.delete(`/reviews/${id}`),
}
