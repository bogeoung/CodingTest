n = int(input())
m_list = [0] * 30001

for i in range(2, n+1):
    m_list[i] = m_list[i-1] + 1
    if i % 2 == 0:
        m_list[i] = min(m_list[i], m_list[i//2] + 1)
    if i % 3 == 0:
        m_list[i] = min(m_list[i], m_list[i//3] + 1)
    if i % 5 == 0:
        m_list[i] = min(m_list[i], m_list[i//5] + 1)

print(m_list[n])
