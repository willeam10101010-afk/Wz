import os
import openpyxl
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# Ganti dengan token bot Telegram Anda
TOKEN = 'YOUR_BOT_TOKEN_HERE'

# Path ke file XLSX
XLSX_FILE = 'data.xlsx'

def load_existing_data():
    """Memuat data dari XLSX jika file ada."""
    if os.path.exists(XLSX_FILE):
        wb = openpyxl.load_workbook(XLSX_FILE)
        sheet = wb.active
        return [row[0].value for row in sheet.iter_rows(min_row=2) if row[0].value]
    return []

def save_data(message):
    """Menyimpan pesan baru ke XLSX."""
    if not os.path.exists(XLSX_FILE):
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet['A1'] = 'Message'
    else:
        wb = openpyxl.load_workbook(XLSX_FILE)
        sheet = wb.active
    
    sheet.append([message])
    wb.save(XLSX_FILE)

async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    existing_data = load_existing_data()
    
    if user_message in existing_data:
        await update.message.reply_text("Pesan sudah ada di database.")
    else:
        await update.message.reply_text("Data dapat digunakan.")
        save_data(user_message)

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT, message_handler))
    application.run_polling()

if __name__ == '__main__':
    main()