import apiClient from './client'

export const contactApi = {
  /** Публичная отправка формы обратной связи */
  send: (data) => apiClient.post('/contact-messages', data),

  /** Список сообщений (admin) */
  getAll: (params = {}) => apiClient.get('/contact-messages', { params }),

  /** Пометить прочитанным (admin) */
  markRead: (id) => apiClient.patch(`/contact-messages/${id}/read`),

  /** Удалить сообщение (admin) */
  delete: (id) => apiClient.delete(`/contact-messages/${id}`),
}
