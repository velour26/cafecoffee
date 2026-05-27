import apiClient from './client'

export async function askBarista(question) {
  // AI-запросы могут идти долго (qwen2.5:3b прогревается до минуты), поэтому даём 4 минуты
  const { data } = await apiClient.post('/ai/barista', { question }, { timeout: 240000 })
  return data
}
