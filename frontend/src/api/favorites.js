import apiClient from './client'

export const favoritesApi = {
  getAll: () => apiClient.get('/favorites'),
  add: (menuItemId) => apiClient.post(`/favorites/${menuItemId}`),
  remove: (menuItemId) => apiClient.delete(`/favorites/${menuItemId}`),
}
