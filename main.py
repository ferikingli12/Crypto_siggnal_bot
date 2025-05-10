import os
import time
import requests
from datetime import datetime

# توکن و چت آیدی از متغیر محیطی
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("📩 پیام با موفقیت ارسال شد.")
        else:
            print(f"❌ خطا در ارسال پیام: {response.status_code} - {response.text}")
    except Exception as e:
        print("❗ خطا:", e)

def fake_signal_generator():
    # اینجا رو بعداً با API یا تحلیل‌گر واقعی وصل می‌کنیم
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    signals = [
        "🔹 سیگنال خرید: BTCUSDT در تایم‌فریم 5 دقیقه‌ای",
        "🔻 سیگنال فروش: ETHUSDT در تایم‌فریم 15 دقیقه‌ای",
        "🟢 واگرایی مثبت در BNBUSDT - تایم‌فریم 1 ساعته"
    ]
    message = f"📈 سیگنال جدید ({now}):\n\n{signals[int(time.time()) % len(signals)]}"
    return message

# اجرای ربات به صورت دوره‌ای (هر 30 ثانیه یک‌بار)
if __name__ == "__main__":
    while True:
        msg = fake_signal_generator()
        send_telegram_message(msg)
        time.sleep(30)
