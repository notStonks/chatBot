import logging
import os
from dotenv import load_dotenv
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from payment import TinkoffPayment


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

terminal_key = os.getenv('terminal_key')
password = os.getenv('password')

notification_url = os.getenv('notification_url')


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
    pay.insert(btnpay)

    return pay

