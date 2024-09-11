import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters, CallbackContext
import pandas as pd
from docx import Document

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to PagePal! Use /help to see available commands.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('/start - Welcome message\n/book - Recommend books by genre\n/preview - Get book preview link\n/list - Manage reading list\n/reading_list - View reading list\n/help - List of commands')

def book(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please enter the genre of the book you want to read.')

def preview(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please enter the name of the book for which you need a preview link.')

def list_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Please enter the name of the book to manage your reading list.')

def reading_list(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Add a book", callback_data='add')],
        [InlineKeyboardButton("Delete a book", callback_data='delete')],
        [InlineKeyboardButton("View Reading List", callback_data='view')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Manage your reading list:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'add':
        query.edit_message_text(text="Add a book feature coming soon!")
    elif query.data == 'delete':
        query.edit_message_text(text="Delete a book feature coming soon!")
    elif query.data == 'view':
        query.edit_message_text(text="View Reading List feature coming soon!")

def main() -> None:
    # Create the Updater and pass it your bot's token.
    updater = Updater("6511465677:AAFWqDg8y5uiT1zwpF9zOZnluyscIvcAT28")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("book", book))
    dispatcher.add_handler(CommandHandler("preview", preview))
    dispatcher.add_handler(CommandHandler("list", list_command))
    dispatcher.add_handler(CommandHandler("reading_list", reading_list))
    dispatcher.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
def book(update: Update, context: CallbackContext) -> None:
    genre = update.message.text.split(' ', 1)[1]  # Get the genre from the message
    # Fetch book details based on genre (dummy data for now)
    books = [
        {"Title": "Book1", "Author": "Author1", "Description": "Description1", "Year": 2000, "Language": "English", "Preview": "http://example.com/book1"},
        {"Title": "Book2", "Author": "Author2", "Description": "Description2", "Year": 2001, "Language": "English", "Preview": "http://example.com/book2"}
    ]
    df = pd.DataFrame(books)
    df.to_csv('books.csv', index=False)
    update.message.reply_document(document=open('books.csv', 'rb'))
def preview(update: Update, context: CallbackContext) -> None:
    book_name = update.message.text.split(' ', 1)[1]  # Get the book name from the message
    # Fetch preview link based on book name (dummy data for now)
    preview_link = "http://example.com/book_preview"
    update.message.reply_text(f'Preview link for {book_name}: {preview_link}')
