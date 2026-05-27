export function formatPrice(price) {
  return new Intl.NumberFormat('ru-RU', {
    style: 'currency',
    currency: 'RUB',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0,
  }).format(price)
}

export function formatDate(dateStr) {
  if (!dateStr) return ''
  return new Date(dateStr).toLocaleDateString('ru-RU', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  })
}

export const ORDER_STATUS_LABELS = {
  new: 'Новый',
  confirmed: 'Подтверждён',
  preparing: 'Готовится',
  ready: 'Готов',
  completed: 'Выполнен',
  cancelled: 'Отменён',
}

export function getStatusLabel(status) {
  return ORDER_STATUS_LABELS[status] || status
}

export function getStatusClass(status) {
  const map = {
    new: 'badge-status-new',
    confirmed: 'badge-status-confirmed',
    preparing: 'badge-status-preparing',
    ready: 'badge-status-ready',
    completed: 'badge-status-completed',
    cancelled: 'badge-status-cancelled',
  }
  return map[status] || 'bg-gray-100 text-gray-600'
}
