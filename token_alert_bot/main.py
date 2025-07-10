from fetch_data import get_token_data
from analyzer import choose_best_token
from emailer import send_email
import time

while True:
    try:
        token_info = get_token_data()
        best_token = choose_best_token(token_info)
        send_email(best_token)
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(3600)  # Espera 1 hora
