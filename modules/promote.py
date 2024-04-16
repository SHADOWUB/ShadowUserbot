from telegram import *
from telegram.ext import *
import os , time , asyncio


def promote_user(update,context):
    chat_id = update.message.chat_id
    user=update.effective_user
    admins = context.bot.get_chat_administrators(chat_id)
    admin_list = []
    if chat.id == user.id:
        update.message.reply_text("*Gey\nThis command only usable in groups*",parse_mode=ParseMode.MARKDOWN)
        return
    for admin in admins:
        admin_list.append(admin.user.id)
    if user.id not in admin_list:
        update.message.reply_text("*You, nigga can't promote\nCoz nigga is not a admin*",parse_mode=ParseMode.MARKDOWN)
        return
    if update.message.reply_to_message :
        user_id = update.message.reply_to_message.from_user.id
        if user_id in admin_list:
            update.message.reply_text("*Seems like the replied user is already admin*",parse_mode=ParseMode.MARKDOWN)
            return
        try:
            context.bot.promote_chat_member(chat_id, user_id,can_delete_messages=True)
        except:
            update.message.reply_text("*IDH valid rights to promote the user*",parse_mode=ParseMode.MARKDOWN)
            return
        update.message.reply_text("Promoted",parse_mode=ParseMode.MARKDOWN)
    else:
        update.message.reply_text("*Reply To a User*",parse_mode=ParseMode.MARKDOWN)
        return

def demote(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    user=update.effective_user
    admins = context.bot.get_chat_administrators(chat_id)
    admin_list = []
    if chat.id == user.id:
        update.message.reply_text("*Gey\nThis command only usable in groups*",parse_mode=ParseMode.MARKDOWN)
        return
    for admin in admins:
        admin_list.append(admin.user.id)
    if user.id not in admin_list:
        update.message.reply_text("*You, nigga can't promote\nCoz nigga is not a admin*",parse_mode=ParseMode.MARKDOWN)
        return
    if update.message.reply_to_message :
        user_id = update.message.reply_to_message.from_user.id
        if user_id in admin_list:
            update.message.reply_text("*Seems like the replied user is already admin*",parse_mode=ParseMode.MARKDOWN)
            return
        user_to_demote = update.message.reply_to_message.from_user
        try:
            context.bot.promote_chat_member(update.effective_chat.id, user_to_demote.id, can_change_info=False, can_delete_messages=False, can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False)
        except:
            update.message.reply_text("IT seems like the user is more powerful than me",parse_mode=ParseMode.MARKDOWN)
            return    
        update.message.reply_text(f"{user_to_demote.first_name} has been demoted.")
    else:
        update.message.reply_text("You do not have permission to demote users in this group.")