from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://telegra.ph/file/a5a2bb456bf3eecdbbb99.mp4',
    'https://telegra.ph/file/03c6e49bea9ce6c908b87.mp4',
    'https://telegra.ph/file/9ebf412f09cd7d2ceaaef.mp4',
    'https://telegra.ph/file/293cc10710e57530404f8.mp4',
    'https://telegra.ph/file/506898de518534ff68ba0.mp4',
    'https://telegra.ph/file/dae0156e5f48573f016da.mp4',
    'https://telegra.ph/file/3e2871e714f435d173b9e.mp4',
    'https://telegra.ph/file/714982b9fedfa3b4d8d2b.mp4',
    'https://telegra.ph/file/876edfcec678b64eac480.mp4',
    'https://telegra.ph/file/6b1ab5aec5fa81cf40005.mp4',
    'https://telegra.ph/file/b4834b434888de522fa49.mp4'
]

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("📢 Updated Channel", url="https://t.me/Tech_Shreyansh1")
                ]
            ]
        )
        await app.send_video(kk.id, img, f"**Hello {kk.mention}!\nWelcome To {op.title}\n\nClick /start to know more.\n\n__Powerd By : @Tech_Shreyansh29__**", reply_markup=keyboard)
        add_user(kk.id)
    except errors.PeerIdInvalid:
        print("User hasn't started the bot (private chat).")
    except Exception as err:
        print(str(err))    

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Start ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("start"))
async def op(_, m :Message):
    try:
        # First check if CHID is valid
        try:
            chat = await app.get_chat(cfg.CHID)
            await app.get_chat_member(cfg.CHID, m.from_user.id)
        except ValueError:
            # If CHID is invalid, skip the membership check
            raise UserNotParticipant
        except Exception as e:
            print(f"Error checking membership: {e}")
            raise UserNotParticipant
            
        if m.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/Tech_Shreyansh"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/Tech_Shreyansh2")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/StarkApprovedBot?startgroup")
                    ]
                ]
            )
            add_user(m.from_user.id)
            await m.reply_photo("https://telegra.ph/file/a782e3bbbe40df8a4bb67.jpg", caption="**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @Tech_Shreyansh29__**".format(m.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard)
    
        elif m.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            keyboar = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("💁‍♂️ Start me private 💁‍♂️", url="https://t.me/StarkApprovedBot?start=start")
                    ]
                ]
            )
            add_group(m.chat.id)
            await m.reply_text("**🦊 Hello {}!\nwrite me private for more details**".format(m.from_user.first_name), reply_markup=keyboar)
        print(m.from_user.first_name +" Is started Your Bot!")

    except UserNotParticipant:
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🍀 Check Again 🍀", "chk")
                ]
            ]
        )
        await m.reply_text("**⚠️Access Denied!⚠️\n\nPlease Join @{} to use me.If you joined click check again button to confirm.**".format(cfg.FSUB), reply_markup=key)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Disclaimer Command ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("disclaimer"))
async def disclaimer(_, m : Message):
    disclaimer_text = """
📢 **Disclaimer – Auto Approve Join Request Bot**

🔹 This bot is an automated system that approves join requests in Telegram channels/groups based on predefined rules. By using this bot, you acknowledge and agree to the following:

✅ **No Liability**
The bot owner & developers are not responsible for any unauthorized access, spam, or misuse. Channel/Group admins must configure settings responsibly.

🤖 **Automated Decisions**
The bot works automatically based on set criteria. It does not verify user intent or guarantee member authenticity.

🔧 **Admin Responsibility**
Channel/Group admins are fully responsible for moderation. The bot only accepts requests and does not enforce any additional rules.

🚫 **No Responsibility for Content**
The bot does not control, monitor, or endorse any messages, media, or content posted in the group/channel. The channel admins and users are solely responsible for all content shared. The bot owner & developers cannot be held accountable for any violations, illegal content, or disputes arising in the channel/group.

🔒 **Privacy Notice**
The bot does not store or share personal data beyond what's needed for join request processing.

📌 **Ensure responsible usage to keep your channel/group secure!**
    """
    await m.reply_text(disclaimer_text, disable_web_page_preview=True)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Callback ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_callback_query(filters.regex("chk"))
async def chk(_, cb: CallbackQuery):
    try:
        try:
            chat = await app.get_chat(cfg.CHID)
            await app.get_chat_member(cfg.CHID, cb.from_user.id)
        except ValueError:
            await cb.answer(
                "🔒 Access Denied!\n\n"
                "👉 You must join our channel first to use this bot.\n"
                "📢 Channel: @Tech_Shreyansh",
                show_alert=True
            )
            return
        except Exception as e:
            print(f"Error checking membership: {e}")
            raise UserNotParticipant
            
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup([...])  # Keep your existing keyboard
            add_user(cb.from_user.id)
            await cb.message.edit(...)  # Keep your existing edit
        print(f"{cb.from_user.first_name} started your bot!")
        
    except UserNotParticipant:
        await cb.answer(
            "❌ Verification Failed!\n\n"
            "You haven't joined our channel yet.\n"
            "Please join @Tech_Shreyansh and try again.",
            show_alert=True
        )
            
        if cb.message.chat.type == enums.ChatType.PRIVATE:
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗯 Channel", url="https://t.me/Tech_Shreyansh"),
                        InlineKeyboardButton("💬 Support", url="https://t.me/Tech_Shreyansh2")
                    ],[
                        InlineKeyboardButton("➕ Add me to your Chat ➕", url="https://t.me/StarkApprovedBot?startgroup")
                    ]
                ]
            )
            add_user(cb.from_user.id)
            await cb.message.edit("**🦊 Hello {}!\nI'm an auto approve [Admin Join Requests]({}) Bot.\nI can approve users in Groups/Channels.Add me to your chat and promote me to admin with add members permission.\n\n__Powerd By : @Tech_Shreyansh29__**".format(cb.from_user.mention, "https://t.me/telegram/153"), reply_markup=keyboard, disable_web_page_preview=True)
        print(cb.from_user.first_name +" Is started Your Bot!")
    except UserNotParticipant:
        await cb.answer("🙅‍♂️ You are not joined to channel join and try again. 🙅‍♂️", show_alert=True)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Info ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("users") & filters.user(cfg.SUDO))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("bcast") & filters.user(cfg.SUDO))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Broadcast Forward ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_message(filters.command("fcast") & filters.user(cfg.SUDO))
async def fcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "fcast":
                await m.reply_to_message.forward(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

print("I'm Alive Now!")
app.run()
