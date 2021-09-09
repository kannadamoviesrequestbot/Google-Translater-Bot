from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from translation import Translation

@Client.on_message(filters.private & filters.command("start"))
async def start_main(main, update):
    await update.reply_text(Translation.START_MSG.format(update.from_user.first_name),
                            reply_to_message_id = update.message_id,
                            parse_mode="markdown",
                            reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("Support channel", url="https://t.me/BAGURUJOINAGUUKANNADAMOVIES_17"),
                            InlineKeyboardButton("support group", url="https://t.me/searchkannadamovies")
                            ],[
                            InlineKeyboardButton("📢 Join Updates Channel 📢" ,url="t.me/BAGURUJOINAGUUKANNADAMOVIES_17")
                            ]])
                            )
@Client.on_message(filters.private & filters.command("about"))
async def about_main(main, update):
    await update.reply_text(Translation.ABOUT_MSG,
                            reply_to_message_id = update.message_id,
                            parse_mode="markdown",
                            reply_markup=InlineKeyboardMarkup([[
                            InlineKeyboardButton("📢 Join Updates Channel 📢" ,url="t.me/BAGURUJOINAGUUKANNADAMOVIES_17")
                            ]])
                            )
