import logging
import uuid

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
from aiogram.types import InputFile, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import payment

import markups as nav
from db import Database

from utils import get_payment_info, get_buy_keyboard

db = Database("database.db")

# --- Конфиг ---
# TOKEN = "5807268799:AAFgOQEJEnqspKvo0AJbPHvVXQi44qrHT50"
TOKEN = "6173169313:AAFaduSszLzSwrFbJe3wyhGzFr4pl_sye84"

ROBOKASSATEST = "1920051371:TEST:638150151980623935"
YOOTOKEN = "390540012:LIVE:33158"
SBERBANK = "401643678:TEST:d97574e6-085c-4013-b784-ad589793eff3"

admin_ID = 703278582

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
#    animation = open('kukard.MP4', 'rb')
#    fayl = open("Пользовательское соглашение.docx","rb")
#    await bot.send_animation(message.from_user.id, animation)
    await bot.send_message(message.from_user.id,'Добро пожаловать в наш Telegram bot <b>{0.first_name}</b>. Мы рады приветствовать и рассчитываем на долгосрочное сотрудничество вместе, перед использованием немного серьезности, тебе нужно принять классическое пользовательское соглашение, указанное ниже. '.format(message.from_user), reply_markup = nav.yesMenu, parse_mode="html")
#    await bot.send_document(message.chat.id, document=fayl)


@dp.message_handler(commands=['jojo'])
async def jojo(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await bot.send_message(message.from_user.id, 'Какой наминал?', reply_markup = nav.adminMenu)


class FSMA(StatesGroup):
    cIDA = State()
    codesA = State()

@dp.message_handler(commands='500руб💵', state=None)
async def cA(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSMA.cIDA.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSMA.cIDA)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDA'] = message.text[0]
    A = message.text
    db.up_IDA(A)
    await FSMA.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSMA.codesA)
async def imput_CODE(message: types.Message, state: FSMContext):
    A1 = db.get_IDA()
    A2 = message.text
    db.up_codA(A2,A1)
    await bot.send_message(message.from_user.id,"Код на 500руб успешно записан!")
    await state.finish()


class FSMB(StatesGroup):
    cIDB = State()
    codesB = State()

@dp.message_handler(commands='1000руб💴', state=None)
async def cB(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSMB.cIDB.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSMB.cIDB)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDB'] = message.text[0]
    B = message.text
    db.up_IDB(B)
    await FSMB.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSMB.codesB)
async def imput_CODE(message: types.Message, state: FSMContext):
    B1 = db.get_IDB()
    B2 = message.text
    db.up_codB(B2,B1)
    await bot.send_message(message.from_user.id,"Код на 1000руб успешно записан!")
    await state.finish()


class FSMC(StatesGroup):
    cIDC = State()
    codesC = State()

@dp.message_handler(commands='1500руб💴', state=None)
async def cC(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSMC.cIDC.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSMC.cIDC)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDC'] = message.text[0]
    C = message.text
    db.up_IDC(C)
    await FSMC.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSMC.codesC)
async def imput_CODC(message: types.Message, state: FSMContext):
    C1 = db.get_IDC()
    C2 = message.text
    db.up_codC(C2,C1)
    await bot.send_message(message.from_user.id,"Код на 1500руб успешно записан!")
    await state.finish()


class FSMD(StatesGroup):
    cIDD = State()
    codesD = State()

@dp.message_handler(commands='2000руб💶', state=None)
async def cD(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSMD.cIDD.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSMD.cIDD)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDD'] = message.text[0]
    D = message.text
    db.up_IDD(D)
    await FSMD.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSMD.codesD)
async def imput_CODE(message: types.Message, state: FSMContext):
    D1 = db.get_IDD()
    D2 = message.text
    db.up_codD(D2,D1)
    await bot.send_message(message.from_user.id,"Код на 2000руб успешно записан!")
    await state.finish()


class FSME(StatesGroup):
    cIDE = State()
    codesE = State()

@dp.message_handler(commands='3000руб💶', state=None)
async def cE(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSME.cIDE.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSME.cIDE)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDE'] = message.text[0]
    E = message.text
    db.up_IDE(E)
    await FSME.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSME.codesE)
async def imput_CODE(message: types.Message, state: FSMContext):
    E1 = db.get_IDE()
    E2 = message.text
    db.up_codE(E2,E1)
    await bot.send_message(message.from_user.id,"Код на 3000руб успешно записан!")
    await state.finish()


class FSMF(StatesGroup):
    cIDF = State()
    codesF = State()

@dp.message_handler(commands='4000руб💶', state=None)
async def cF(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSMF.cIDF.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSMF.cIDF)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDF'] = message.text[0]
    F = message.text
    db.up_IDF(F)
    await FSMF.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSMF.codesF)
async def imput_CODE(message: types.Message, state: FSMContext):
    F1 = db.get_IDF()
    F2 = message.text
    db.up_codF(F2,F1)
    await bot.send_message(message.from_user.id,"Код на 4000руб успешно записан!")
    await state.finish()


class FSMG(StatesGroup):
    cIDG = State()
    codesG = State()

@dp.message_handler(commands='5000руб💷', state=None)
async def cG(message: types.Message):
    if message.chat.type == 'private':
        if message.from_user.id == admin_ID:
            await FSMG.cIDG.set()
            await bot.send_message(message.from_user.id,'С какого ID начинаем?')

@dp.message_handler(state=FSMG.cIDG)
async def imput_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cIDG'] = message.text[0]
    G = message.text
    db.up_IDG(G)
    await FSMG.next()
    await bot.send_message(message.from_user.id,"Вводите код")

@dp.message_handler(state=FSMG.codesG)
async def imput_CODE(message: types.Message, state: FSMContext):
    G1 = db.get_IDG()
    G2 = message.text
    db.up_codG(G2,G1)
    await bot.send_message(message.from_user.id,"Код на 5000руб успешно записан!")
    await state.finish()


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Согласен':
        await bot.send_message(message.from_user.id, 'Спасибо за доверие <b>{0.first_name}</b>!Далее ты можешь скорее перейти к оплате или же узнать о больше информации о сервисе, а также разобраться и обратиться с возникшими вопросами.'.format(message.from_user), reply_markup = nav.mainMenu,parse_mode="html")

    elif message.text == 'Не согласен':
        await bot.send_message(message.from_user.id, f'К сожалению я не могу продолжить работу, без принятия соглашения.\nСоглашайся и управляй своей жизнью сам!')
    
    elif message.text == 'Узнать о сервисе больше':
#        photo = open('kukardJ.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Здесь представлена информация о нашем проекте и возможные возникшие вопросы, на которые мы постараемся ответить.', reply_markup = nav.meMenu)
        await message.delete()

    elif message.text == 'Наш сайт':
        await bot.send_message(message.from_user.id, 'https://iamdocard.ru/', reply_markup = nav.meMenu)
        await message.delete()

    elif message.text == 'Кто мы?':
        await bot.send_message(message.from_user.id, f'docard – он такой один.\n\nОнлайн-сервис, позволяющий купить электронную подарочную карту для пополнения твоего Apple ID.\n\n\n\n👨‍🎓 Нам можно доверять.\n\nМы команда Стартап-проекта, сотрудничающая с Фондом содействия инновациям. Победители конкурса “Студенческий стартап” и просто обычные люди, способные на большее.\n\n🎯 Наша цель.\n\nМы молодые, дерзкие, живые и актуальные, поэтому на одной волне с нашей аудиторией что позволяет делать современный продукт.\n\nНаша цель- сделать комфортную экосистему, через которую любой желающий сможет с легкостью пополнить свои любимые сервисы, не покидая родную среду Telegram за разумную цену.\n\n🍏 Apple ID это только начало.\n\nМы не собираемся ограничиваться одной тематикой Apple ID, за кого вы нас держите?\n\nСейчас мы работаем над совершенствованием нашего бота, после чего, нашим приоритетом поставлено масштабирование с помощью внедрения пополнения других, ранее доступных сервисов из-за границы.\n\n🛫Ориентация на будущее.\n\nМы ориентируемся на такую же молодежь как и мы сами и двигаемся в направлении современного развития, для того чтобы сделать качественный продукт, поэтому давайте двигаться вперед вместе, будем рады вашим отзывам и предложениям для развития нашего проекта, которые вы можете оставить во вкладке отзывы.\n\nВ наши дальнейшие планы входит развитие собственной экосистемы, реализованной через мессенджер Telegram и плодотворная работа над улучшением сервиса.\n\n💞 Мы-это новая искренность.\n\nХотим поблагодарить в отдельности каждого нашего клиента за оказанное доверие, в ответ мы будем оставаться верны себе, прислушиваться к нашей аудитории и обещаем становиться лучше вместе с вами.', reply_markup = nav.meMenu)
        await message.delete()

    elif message.text == 'Пополнить “Apple ID”':
#        photo = open('impresion.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Здесь представлен номинал наших карт выбирай любую которая понравится!\nПомни, ни что не истина все дозволено, но с другой стороны:\nДелай что по кайфу, но в меру!', reply_markup = nav.payMenu)
        await message.delete()

    elif message.text == '500р':
#        photo = open('500x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 500 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_500_rub)
        await message.delete()

    elif message.text == '1000р':
#        photo = open('1000x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 1000 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_1000_rub)
        await message.delete()
    
    elif message.text == '1500р':
#        photo = open('1500x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 1500 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_1500_rub)
        await message.delete()
    
    elif message.text == '2000р':
#        photo = open('2000x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 2000 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_2000_rub)
        await message.delete()

    elif message.text == '3000р':
#        photo = open('3000x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 3000 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_3000_rub)
        await message.delete()

    elif message.text == '4000р':
#        photo = open('4000x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 4000 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_4000_rub)
        await message.delete()

    elif message.text == '5000р':
#        photo = open('5000x.jpg', 'rb')
#        await bot.send_photo(message.from_user.id, photo)
        await bot.send_message(message.from_user.id, 'Ты выбрал карту 5000 рублей\nС учетом комиссии, цена составит:', reply_markup = nav.pay_5000_rub)
        await message.delete()
 
    elif message.text == 'Назад':
        await bot.send_message(message.from_user.id, 'Назад', reply_markup = nav.mainMenu)
        await message.delete()

    else:
        pass


@dp.callback_query_handler(text="Back")
async def Back (call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_message(call.from_user.id, 'Назад', reply_markup = nav.payMenu)


description = "Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента."


@dp.callback_query_handler(Text(endswith="rub"))
async def p500rub(call: types.CallbackQuery):
    amounts_dict = {500: 990, 1000: 1790, 1500: 2690, 2000: 3590, 3000: 5390, 4000: 7190, 5000: 8990}
    amount: int = int(call.data[1:-3])
    order_id = str(uuid.uuid4())
    payment_url, payment_id = get_payment_info(order_id, amounts_dict[amount])
    db.add_user_idA(call.from_user.id, payment_id, order_id)
    keyboard = get_buy_keyboard(payment_url)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    text = f"<b>Giftcard номиналом - {amount} руб.</b>\n"
    text += description
    await bot.send_message(call.from_user.id, text=text, parse_mode="HTML", reply_markup=keyboard)


@dp.callback_query_handler(text="p1000rub")
async def p1000rub(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Giftcard номиналом -1000руб.", description="Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента.", payload="p1000", provider_token=SBERBANK, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб","amount": 179000}])

@dp.callback_query_handler(text="p1500rub")
async def p1500rub(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Giftcard номиналом -1500руб.", description="Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента.", payload="p1500", provider_token=SBERBANK, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб","amount": 269000}])

@dp.callback_query_handler(text="p2000rub")
async def p2000rub(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Giftcard номиналом -2000руб.", description="Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента.", payload="p2000", provider_token=SBERBANK, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб","amount": 359000}])

@dp.callback_query_handler(text="p3000rub")
async def p3000rub(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Giftcard номиналом -3000руб.", description="Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента.", payload="p3000", provider_token=SBERBANK, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб","amount": 539000}])

@dp.callback_query_handler(text="p4000rub")
async def p4000rub(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Giftcard номиналом -4000руб.", description="Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента.", payload="p4000", provider_token=SBERBANK, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб","amount": 719000}])

@dp.callback_query_handler(text="p5000rub")
async def p5000rub(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(chat_id=call.from_user.id, title="Giftcard номиналом -5000руб.", description="Подарочная карта – это электронный сертификат 16-значный код, начинающийся с символа X. Этот код используется для погашения карты путем зачисления суммы равной номиналу карты на счет идентификатора пополняемого клиента.", payload="p5000", provider_token=SBERBANK, currency="RUB", start_parameter="test_bot", prices=[{"label": "Руб","amount": 899000}])

@dp.pre_checkout_query_handler()
async def process_pre_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.Message):
    if message.successful_payment.invoice_payload == "p500":
        A = db.countA()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codA(A)}</code>\nЕсли возникли проблемы с гифт кодом - обратитесь в службу поддержки.",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrkdj53YlraqITVLxHrp87twO3l9EdgACbikAAkizOEvykQRAr7eVay4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {A}, номинал 500 рублей---</b>",parse_mode="html")
        if A == 50:
            A = 0
        db.up_nA(A+1)

    elif message.successful_payment.invoice_payload == "p1000":
        B = db.countB()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codB(B)}</code>",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrklj53Yrjc5urNqQcGqJ8TKQkl-0RwAC6yUAAsnrOUtbocbdf_vO0S4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {B}, номинал 1000 рублей---</b>",parse_mode="html")
        if B == 50:
            B = 0
        db.up_nB(B+1)

    elif message.successful_payment.invoice_payload == "p1500":
        C = db.countC()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codC(C)}</code>",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrktj53Yvxk9Zoz0wx29urLBqW56l3QACFCoAAuwYOUsaSFgr0qj17i4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {C}, номинал 1500 рублей---</b>",parse_mode="html")
        if C == 50:
            C = 0
        db.up_nC(C+1)

    elif message.successful_payment.invoice_payload == "p2000":
        D = db.countD()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codD(D)}</code>",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrk1j53YzvK3JsucUcEzhISaxvurKpAACyy0AAp1PMEsD-4Vw4eSpTC4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {D}, номинал 2000 рублей---</b>",parse_mode="html")
        if D == 50:
            D = 0
        db.up_nD(D+1)

    elif message.successful_payment.invoice_payload == "p3000":
        E = db.countE()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codE(E)}</code>",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrk9j53Y5ZIhn_NIDj77pnkDNsR3hTAACWikAAhwDOUv1-yYRQ7fQoC4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {E}, номинал 3000 рублей---</b>",parse_mode="html")
        if E == 50:
            E = 0
        db.up_nE(E+1)

    elif message.successful_payment.invoice_payload == "p4000":
        F = db.countF()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codF(F)}</code>",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrlFj53ZAv7zOPut5VHfRUITXe6N9kwACZSkAAhwyOUuWtwQDEpTqcy4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {F}, номинал 4000 рублей---</b>",parse_mode="html")
        if F == 50:
            F = 0
        db.up_nF(F+1)

    elif message.successful_payment.invoice_payload == "p5000":
        G = db.countG()
        await bot.send_message(message.from_user.id, f"Спасибо за покупку!\nВаш код: <code>{db.get_codG(G)}</code>",reply_markup = nav.mainMenu,parse_mode="html")
#        await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHrlNj53ZEPlXU1qg19U3ojndeJVNN-AAC4CMAAr_fOUubTY0Fkh7I8S4E")
        await bot.send_message(admin_ID,f"<b>---Куплен номер {G}, номинал 5000 рублей---</b>",parse_mode="html")
        if G == 50:
            G = 0
        db.up_nG(G+1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)