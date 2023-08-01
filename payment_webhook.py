import logging
from fastapi import FastAPI, Request
from fastapi.responses import Response

from utils import get_buy_keyboard, get_payment_info

from db import Database
from main import bot, admin_ID
import markups as nav

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = Database("database.db")

app = FastAPI()


@app.post("/hook/")
async def recWebHook(request: Request):
    try:
        body = await request.json()
        logger.info(body)
        status = body["Status"]
        if status == "CONFIRMED":
            await _confirmed_payment(body["OrderId"], body["Amount"])
        if status == "REJECTED":
            await _rejected_payment(body["OrderId"], body["Amount"])
        return Response(status_code=200, content="OK")
    except Exception as _exec:
        logger.error(f"{_exec}")
        return Response({"Error": "Some error occured."})


async def _confirmed_payment(order_id: str, amount: int):
    """
    Посылает пользователю сообщение, что оплата прошла успешно
    и меняет статус в БД
    """
    try:
        user_id = db.get_user_from_order_idA(order_id)
        amount = amount // 100
        await process_pay(user_id, amount)
    except Exception as _exec:
        logger.error(f"{_exec}")
        return Response({"Error": "Some error occured."})


async def _rejected_payment(order_id: str, amount: int):
    """
    Посылает пользователю сообщение в случае непрошедшей оплаты
    и отправляет новую ссылку на повторную оплату
    """
    try:
        amount = amount // 100

        user_id = db.get_user_from_order_idA(order_id)
        db.delete_userA(user_id)

        payment_url, payment_id = get_payment_info(order_id, amount)
        db.add_user_idA(user_id, payment_id, order_id)
        buy_keyboard = get_buy_keyboard(payment_url)

        await bot.send_message(user_id, text="Произошла ошибка. Попробуйте еще раз", reply_markup=buy_keyboard)

    except Exception as _exec:
        logger.error(f"{_exec}")
        # return JsonResponse({"Error": "Some error occured."})



async def process_pay(user_id, amount):
    """
    Этот метод выглядит так, потому что изначально бот написан не в самом лучшем стиле((
    """
    amounts_dict = {500: 990, 1000: 1790, 1500: 2690, 2000: 3590, 3000: 5390, 4000: 7190, 5000: 8990}
    if amount == amounts_dict[500]:
        literal = db.countA()
        code = db.get_codA(literal)
        if literal == 50:
            literal = 0
        db.up_nA(literal+1)

    elif amount == amounts_dict[1000]:
        literal = db.countB()
        code = db.get_codB(literal)

        if literal == 50:
            literal = 0
        db.up_nB(literal+1)

    elif amount == amounts_dict[1500]:
        literal = db.countC()
        code = db.get_codC(literal)

        if literal == 50:
            literal = 0
        db.up_nC(literal + 1)

    elif amount == amounts_dict[2000]:
        literal =  db.countD()
        code = db.get_codD(literal)

        if literal == 50:
            literal = 0
        db.up_nD(literal + 1)

    elif amount == amounts_dict[3000]:
        literal = db.countE()
        code = db.get_codE(literal)

        if literal == 50:
            literal = 0
        db.up_nE(literal + 1)

    elif amount == amounts_dict[4000]:
        literal = db.countF()
        code = db.get_codF(literal)

        if literal == 50:
            literal = 0
        db.up_nF(literal + 1)

    elif amount == amounts_dict[5000]:
        literal = db.countG()
        code = db.get_codG(literal)

        if literal == 50:
            literal = 0
        db.up_nG(literal + 1)

    await bot.send_message(user_id, f"Спасибо за покупку!\nВаш код: <code>{code}</code>\nЕсли возникли проблемы с гифт кодом - обратитесь в службу поддержки.",reply_markup = nav.mainMenu,parse_mode="html")
    await bot.send_message(admin_ID, f"<b>---Куплен номер {literal}, номинал {amount} рублей---</b>", parse_mode="html")