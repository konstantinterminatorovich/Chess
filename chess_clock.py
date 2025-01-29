from pygame import *

# Инициализация окна
window = display.set_mode((1000, 700))
display.set_caption('Chess clock')
clock = time.Clock()

# Инициализация шрифта
font.init()
font1 = font.SysFont('Arial', 36, bold=1)

# Таймеры ожидания
wait1 = 600  # Время для первого игрока
wait2 = 600  # Время для второго игрока

# Переменные для отслеживания состояния
current_timer = 0  # 0 - никакой, 1 - первый таймер, 2 - второй таймер
winner = None  # Кто выиграл: None, "Player 1" или "Player 2"
current_timer1 = current_timer

# Основной цикл игры
run = True
while run:
    window.fill((139, 69, 19))  # Коричневый фон

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN and e.key == K_SPACE and winner is None:
            # Переключение между таймерами
            if current_timer == 0:
                current_timer = 1  # Запуск первого таймера
            elif current_timer == 1:
                current_timer = 2  # Остановка первого и запуск второго
            elif current_timer == 2:
                current_timer = 1  # Остановка второго и возврат к первому
        elif e.type == KEYDOWN and e.key == K_s and winner is None:
            # Восстановление предыдущего таймера и добавление времени
            current_timer1 = current_timer
            if current_timer == 1 or current_timer == 2:
                current_timer = 0  # Остановка таймера
            elif current_timer == 0:
                current_timer = current_timer1  # Возвращаем предыдущий таймер
                wait1 += 120  # Добавление времени
                wait2 += 120

    # Логика таймеров
    if current_timer == 1 and wait1 > 0:
        wait1 -= 1
    elif current_timer == 2 and wait2 > 0:
        wait2 -= 1

    # Проверка завершения таймеров
    if wait1 == 0 and winner is None:
        winner = "Player 2"
        current_timer = 0  # Остановка таймера
    elif wait2 == 0 and winner is None:
        winner = "Player 1"
        current_timer = 0  # Остановка таймера

    # Отображение таймеров
    text_timer1 = font1.render(f'Время 1: {wait1 // 60} секунд', 1, (255, 255, 255))
    text_timer2 = font1.render(f'Время 2: {wait2 // 60} секунд', 1, (255, 255, 255))
    window.blit(text_timer1, (20, 20))
    window.blit(text_timer2, (20, 80))

    # Отображение текущего активного таймера
    if winner is None:
        if current_timer == 0:
            text_instruction = font1.render('Нажмите пробел, чтобы запустить первый таймер.', 1, (255, 255, 255))
            window.blit(text_instruction, (20, 140))
        elif current_timer == 1:
            text_active = font1.render('Активен таймер 1', 1, (0, 255, 0))
            window.blit(text_active, (20, 140))
        elif current_timer == 2:
            text_active = font1.render('Активен таймер 2', 1, (0, 255, 0))
            window.blit(text_active, (20, 140))
    else:
        # Сообщение о победителе
        text_winner = font1.render(f'{winner} выиграл!', 1, (255, 0, 0))
        window.blit(text_winner, (20, 140))

    display.update()
    clock.tick(60)
