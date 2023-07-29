import logging

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from payment import TinkoffPayment


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

terminal_key = '1678034071786DEMO'
password = 'ia6ntj8iywkfv1u4'

notification_url = "http://06dd-5-16-115-81.ngrok-free.app/hook/"


def get_payment_info(order_id: str, amount: int):
    try:
        payment = TinkoffPayment(terminal_key=terminal_key, password=password)

        payment_result = payment.init(
            order_id, str(amount*100),
            sign_request=True,
            notification_url=notification_url,
            # data={"Phone": user.phone}
        )
        payment_url = payment_result['PaymentURL']
        payment_id = payment_result['PaymentId']
        return payment_url, payment_id

    except AttributeError as _exec:
        logger.error(_exec)
    except Exception as _exec:
        logger.error(f"{_exec}")


def get_buy_keyboard(url: str):
    pay = InlineKeyboardMarkup(row_width=1)
    btnpay = InlineKeyboardButton(text="Оплатить", url=url)
    btnBack = InlineKeyboardButton(text="Назад", callback_data="Back")
    pay.insert(btnpay)
    pay.insert(btnBack)

    return pay

