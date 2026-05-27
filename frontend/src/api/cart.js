import apiClient from './client'

export const cartApi = {
  getCart: () => apiClient.get('/cart'),
  addItem: (data) => apiClient.post('/cart', data),
  updateItem: (id, data) => apiClient.put(`/cart/${id}`, data),
  removeItem: (id) => apiClient.delete(`/cart/${id}`),
  clearCart: () => apiClient.delete('/cart/clear'),
}
