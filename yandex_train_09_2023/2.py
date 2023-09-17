# Обрабатывает строку лога, возвращает [id, минуты, событие]
def parse(entry):
    entry = entry.split()
    entry = list(map(int, entry[:-1])) + [entry[-1]]
    return [entry[3], entry[0] * 24 * 60 + entry[1] * 60 + entry[2], entry[4]]

n = int(input())

# В лог можно не включать события B, они никак не влияют на время
# Время в пути зависит только от расстояния между A и (C, S)
log = []
for _ in range(n):
    entry = parse(input())
    if entry[2] != 'B':
        log.append(entry)

last_id = log[0][0]
answer = []
time_sum = 0
last_timestamp = log[0][1]

# Сортируем по id такси, потом по времени события
for entry in sorted(log):
    id = entry[0]
    timestamp = entry[1]
    event = entry[2]

    # Если начался новый id, то суммарное время предыдущего добавляем в ответ
    if id != last_id:
        answer.append(str(time_sum))
        time_sum = 0
        last_id = id
    
    # Если заказ был принят, запоминаем момент времени
    if event == "A":
        last_timestamp = timestamp
    
    # Если заказ отменён или выполнен, считаем время в пути и прибавляем
    elif event == "C" or event == "S":
        time_sum += timestamp - last_timestamp
answer.append(time_sum)

print(' '.join(answer))
