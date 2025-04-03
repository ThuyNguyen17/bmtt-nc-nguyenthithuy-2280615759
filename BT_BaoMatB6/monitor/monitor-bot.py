import psutil
import logging
import time
import asyncio
from telegram import Bot

# Thay thế bằng API Token của bot Telegram
BOT_TOKEN = "6808243924:AAFJCe4KtZVGPhz2_D074K148ZJOhsNamQQ"

# Thay thế bằng Chat ID của nhóm/chat Telegram
CHAT_ID = "-4031606701"

# Cấu hình logging
logging.basicConfig(
    level=logging.INFO,
    filename="system_monitor_bot.log",
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()

# Hàm ghi log
def log_info(category, message):
    logger.info(f"{category}: {message}")
    print(f"{category}: {message}")

# Hàm gửi tin nhắn qua Telegram (Asynchronous)
async def send_telegram_message(message):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Hàm giám sát CPU và bộ nhớ
def monitor_cpu_memory():
    cpu_percent = psutil.cpu_percent(interval=1)  # Thêm interval để lấy dữ liệu chính xác hơn
    memory_info = psutil.virtual_memory()

    log_info("CPU", f"Usage: {cpu_percent}%")
    log_info("Memory", f"Usage: {memory_info.percent}%")

    # Gửi thông báo nếu CPU hoặc RAM vượt ngưỡng
    if cpu_percent > 80 or memory_info.percent > 80:
        message = f"⚠️ CẢNH BÁO!\nCPU: {cpu_percent}%\nRAM: {memory_info.percent}%"
        asyncio.run(send_telegram_message(message))  # Gọi asyncio đúng cách

# Hàm giám sát toàn bộ hệ thống
def monitor_system():
    log_info("System Monitor", "📡 Bắt đầu giám sát hệ thống...")

    while True:
        monitor_cpu_memory()
        log_info("System Monitor", "=" * 30)  # Dòng phân cách log

        time.sleep(60)  # Lặp lại sau 60 giây

# Kiểm tra nếu script đang chạy chính
if __name__ == "__main__":
    monitor_system()
