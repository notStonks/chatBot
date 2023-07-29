from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


btnMain = KeyboardButton('Назад')

# --- Меню согласия ---
btnYes = KeyboardButton('Согласен')
btnNo = KeyboardButton('Не согласен')
yesMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnYes, btnNo)

# --- Основное меню ---
btnPay = KeyboardButton('Пополнить “Apple ID”')
btnInfo = KeyboardButton('Узнать о сервисе больше')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnPay, btnInfo)

# --- Мень номинала ---
btn500 = KeyboardButton('500р')
btn1000 = KeyboardButton('1000р')
btn1500 = KeyboardButton('1500р')
btn2000 = KeyboardButton('2000р')
btn3000 = KeyboardButton('3000р')
btn4000 = KeyboardButton('4000р')
btn5000 = KeyboardButton('5000р')
payMenu = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
payMenu.add(btn500).insert(btn1000).add(btn1500).insert(btn2000).add(btn3000).insert(btn4000).add(btn5000).insert(btnMain)

# --- Мень о нас ---
btnO = KeyboardButton('Кто мы?')
btnLink = KeyboardButton('Наш сайт')
btnFAQ = KeyboardButton('FAQ')
btnH = KeyboardButton('Отзывы и поддержка')
meMenu = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
meMenu.add(btnO).insert(btnLink).add(btnFAQ).insert(btnH).add(btnMain)

# --- Мень Админа ---
a500 = KeyboardButton('/500руб💵')
b1000 = KeyboardButton('/1000руб💴')
c1500 = KeyboardButton('/1500руб💴')
d2000 = KeyboardButton('/2000руб💶')
e3000 = KeyboardButton('/3000руб💶')
f4000 = KeyboardButton('/4000руб💶')
g5000 = KeyboardButton('/5000руб💷')
adminMenu = ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True)
adminMenu.add(a500).insert(b1000).add(c1500).insert(d2000).add(e3000).insert(f4000).add(btnMain).insert(g5000)

# --- Инлайт кнопки оплаты ---
pay_500_rub = InlineKeyboardMarkup(row_width=1)
btn500pay = InlineKeyboardButton(text="990 рублей", callback_data="p500rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_500_rub.insert(btn500pay)
pay_500_rub.insert(btnBack)

pay_1000_rub = InlineKeyboardMarkup(row_width=1)
btn1000pay = InlineKeyboardButton(text="1790 рублей", callback_data="p1000rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_1000_rub.insert(btn1000pay)
pay_1000_rub.insert(btnBack)

pay_1500_rub = InlineKeyboardMarkup(row_width=1)
btn1500pay = InlineKeyboardButton(text="2690 рублей", callback_data="p1500rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_1500_rub.insert(btn1500pay)
pay_1500_rub.insert(btnBack)

pay_2000_rub = InlineKeyboardMarkup(row_width=1)
btn2000pay = InlineKeyboardButton(text="3590 рублей", callback_data="p2000rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_2000_rub.insert(btn2000pay)
pay_2000_rub.insert(btnBack)

pay_3000_rub = InlineKeyboardMarkup(row_width=1)
btn3000pay = InlineKeyboardButton(text="5390 рублей", callback_data="p3000rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_3000_rub.insert(btn3000pay)
pay_3000_rub.insert(btnBack)

pay_4000_rub = InlineKeyboardMarkup(row_width=1)
btn4000pay = InlineKeyboardButton(text="7190 рублей", callback_data="p4000rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_4000_rub.insert(btn4000pay)
pay_4000_rub.insert(btnBack)

pay_5000_rub = InlineKeyboardMarkup(row_width=1)
btn5000pay = InlineKeyboardButton(text="8990 рублей", callback_data="p5000rub")
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_5000_rub.insert(btn5000pay)
pay_5000_rub.insert(btnBack)

# --- Инлайт кнопки оплаты Тинькофф ---

pay_500_rub_tinkoff = InlineKeyboardMarkup(row_width=1)
btn500paytinlkoff = InlineKeyboardButton(text="990 рублей", url=())
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_500_rub_tinkoff.insert(btn500paytinlkoff)
pay_500_rub_tinkoff.insert(btnBack)

pay_5000_rub_tinkoff = InlineKeyboardMarkup(row_width=1)
btn5000paytinlkoff = InlineKeyboardButton(text="1790 рублей", url=())
btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
pay_5000_rub_tinkoff.insert(btn5000paytinlkoff)
pay_5000_rub_tinkoff.insert(btnBack)