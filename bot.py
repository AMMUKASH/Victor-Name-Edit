import os
import random
import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserIsBlocked, PeerIdInvalid
from flask import Flask
from threading import Thread
from motor.motor_asyncio import AsyncIOMotorClient

# --- RENDER/SERVER SETUP ---
app = Flask('')
@app.route('/')
def home(): return "Victor Stylish Bot is Running!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    Thread(target=run).start()

# --- CONFIGURATION ---
API_ID = 34135757
API_HASH = "d3d5548fe0d98eb1fb793c2c37c9e5c8"
BOT_TOKEN = "8583239839:AAHsTIG-8b4Fnk3Q9t-h6N4zBoX_1yfQC8k"
OWNER_ID = 8482447535
LOG_GROUP = -1003867805165
MONGO_URL = "mongodb+srv://misssqn:VICTOR01@cluster0.3otqmso.mongodb.net/?appName=Cluster0"
START_IMG = "https://graph.org/file/06f17f2da3be3ddf5c9d6-f22b08d691cecb6be9.jpg"

FSUB_1 = "radhesupport"
FSUB_2 = "AboutVictore"

bot = Client("VictorStylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# MongoDB
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client["StylishBotDB"]
users_col = db["users"]

# --- DATABASE FUNCTIONS ---
async def add_user(user_id):
    if not await users_col.find_one({"user_id": user_id}):
        await users_col.insert_one({"user_id": user_id})

async def remove_user(user_id):
    await users_col.delete_one({"user_id": user_id})

async def get_all_users():
    return [doc["user_id"] async for doc in users_col.find({})]

# --- AUTO UPDATE BIO ---
async def update_bot_status():
    await asyncio.sleep(15)
    while True:
        try:
            count = await users_col.count_documents({})
            status_text = f"✨ Professional Stylish Name Editor Bot\n\n📊 Total Active Users: {count}+\n⚡ Powered by: @radhesupport"
            await bot.set_chat_description(chat_id="me", description=status_text)
        except: pass
        await asyncio.sleep(3600)

# --- FONT CHANGER MAPPING ---
def get_font(text, font_type):
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fonts = {
        "bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "italic": "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍",
        "monospace": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
        "double_struck": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "script": "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓌𝓍𝓎𝒿𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳℒ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "fraktur": "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "sans": "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝑉𝗪𝗫𝗬𝗭",
        "greek": "αβγδεζηθικλμνξοπρςστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    }
    if font_type == "greek":
        g_norm = "abgdehijklmnoprstufxoABGDEHIKLMNOPRSTUFXO"
        return "".join([fonts["greek"][g_norm.index(c)] if c in g_norm else c for c in text])
    
    target = fonts.get(font_type, normal)
    return "".join([target[normal.index(c)] if c in normal else c for c in text])

# --- STYLE GENERATOR ---
def get_styles(name):
    f_pool = [get_font(name, f) for f in ["bold", "italic", "monospace", "double_struck", "script", "fraktur", "sans", "greek"]]
    crown = "፝֟"
    extra_emojis = ["⚡", "👑", "💎", "🔥", "✨", "🦋", "🦁", "🧸", "💖", "🧿", "💀", "🍷"]
    templates = [
        "•⎯᪵⎯𐎓⃝꯭✨ ⃪꯭ {}{} ꯭𝄄𝆺𝆭💖", "✦⸙⃪𐎓꯭꯭✨ {}{} ꯭🜲𝆭💞", "🝐‌꯭᪳⸙⃪꯭ {}{} ⸩⃪🍁", "𓆩꯭♡┼ᶦϻ {}{} !!🌺𓆪",
        "𝆺꯭𝅥🦋« – {}{} – »🦋𝆺𝅥", "★彡 {}{} 彡★", "꧁༒☬ {}{} ☬༒꧂", "♡⃕🌙 {}{} 🌙♡",
        "✧₊⁺ {}{} ⁺₊✧", "𓆩✨ {}{} ✨𓆪", "❥⃝🌸 {}{} 🌸❥⃝", "𐌔𐌉𐌋𐌄𐌔𐌕 • {}{} •",
        "❦•°✿ {}{} ✿°•❦", "𖤐⚝ {}{} ⚝𖤐", "☾⋆⁺₊ {}{} ₊⋆☽", "✿◡ {}{} ◡✿",
        "✦✧ {}{} ✧✦", "❝ {}{} ❞", "✨𓆩𝒔𝒕𝒂𝒓𝒔𓆪 {}{}", "꒰⚘ {}{} ⚘꒱",
        "❁⃘ {}{} ❁⃘", "ꗃ꯭❀ {}{} ❀ꗃ", "꧁💎 {}{} 💎꧂", "✩₊˚. {}{} .˚₊✩",
        "꧁𖤐✨ {}{} ✨𖤐꧂", "꧁𖤍࿐ {}{} ࿐𖤍꧂", "⚚⟆ {}{} ⟅⚚", "❖⃝ {}{} ❖⃝",
        "☬༄ {}{} ༄☬", "𖤛𖤐 {}{} 𖤐𖤛", "★彡⭒ {}{} ⭒彡★", "⋆✹⃝ {}{} ✹⃝⋆",
        "ꗃ⋆˙ {}{} ˙⋆ꗃ", "𐂂𐂃 {}{} 𐂃𖠁", "❋₊˚ {}{} ˚₊❋", "✦‌‌ {}{} ‌‌✦",
        "𖣘࿐ {}{} ࿐𖣘", "✧∘₊ {}{} ₊∘✧", "†༺ {}{} ༻†", "➳❥ {}{} ❥➳",
        "𖥔˖ {}{} ˖𖥔", "❦꯭⭐ {}{} ⭐꯭❦", "⚝₊⌇ {}{} ⌇₊⚝", "✹𖤐 {}{} 𖤐✹"
    ]
    results = []
    for i in range(len(templates)):
        temp = templates[i]
        font = f_pool[i % len(f_pool)]
        emo = random.choice(extra_emojis)
        results.append(temp.format(crown + emo, font))
    return results

# --- FSUB CHECK ---
async def is_subscribed(c, m):
    btns = []
    for ch in [FSUB_1, FSUB_2]:
        try:
            await c.get_chat_member(ch, m.from_user.id)
        except UserNotParticipant:
            btns.append([InlineKeyboardButton(f"ᴊᴏɪɴ {ch.upper()}", url=f"https://t.me/{ch}")])
        except Exception: pass
    if btns:
        btns.append([InlineKeyboardButton("🔄 ᴛʀʏ ᴀɢᴀɪɴ", url=f"https://t.me/{(await c.get_me()).username}?start=true")])
        return False, InlineKeyboardMarkup(btns)
    return True, None

# --- HANDLERS ---
@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(c, m):
    sub, markup = await is_subscribed(c, m)
    if not sub:
        return await m.reply_text("❌ **𝐀ᴄᴄᴇ𝐬𝐬 𝐃ᴇɴɪᴇᴅ!**\n\nJoin both channels to use this bot.", reply_markup=markup)
    
    await add_user(m.from_user.id)
    try: await bot.send_message(LOG_GROUP, f"👤 **New User:** {m.from_user.mention}\n🆔 `{m.from_user.id}`")
    except: pass

    btn = InlineKeyboardMarkup([[InlineKeyboardButton("♻ 𝐀ᴅᴅ 𝐌𝝴 𝝸𝝶 𝐘𝞂𝞄𝐑 𝐆𝐑𝞂𝞄𝞀 ♻", url=f"https://t.me/{(await c.get_me()).username}?startgroup=true")]])
    await m.reply_photo(photo=START_IMG, caption=f"👋 Hello {m.from_user.first_name}!\n\nI am your ultimate **Crown Name Decorator**! 👑\nSend your name now!", reply_markup=btn)

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(c, m):
    if not m.reply_to_message: return await m.reply_text("Reply to a message!")
    all_users = await get_all_users()
    msg = await m.reply_text("🚀 Broadcasting...")
    done, blocked = 0, 0
    for u_id in all_users:
        try:
            await m.reply_to_message.copy(u_id)
            done += 1
            await asyncio.sleep(0.1)
        except UserIsBlocked:
            blocked += 1
            await remove_user(u_id)
            try: await bot.send_message(LOG_GROUP, f"🚫 **User Blocked:** `{u_id}`\nRemoved from DB.")
            except: pass
        except: pass
    await msg.edit(f"✅ **Done!**\nSent: `{done}`\nBlocked: `{blocked}`")

@bot.on_message(filters.text & filters.private)
async def styler(c, m):
    if m.text.startswith("/"): return
    sub, markup = await is_subscribed(c, m)
    if not sub: return await m.reply_text("❌ Join channels first!", reply_markup=markup)

    name = m.text
    styles = get_styles(name)
    res = f"✨ **ʜᴇʏ {m.from_user.first_name}**, ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴄʀᴏᴡɴ ᴅᴇsɪɢɴs:\n━━━━━━━━━━━━━━━━━━━━\n\n"
    for s in styles:
        res += f"👉 `{s}`\n\n"
    res += "━━━━━━━━━━━━━━━━━━━━\n⚡ **Tap to copy!**"
    await m.reply_text(res)

if __name__ == "__main__":
    keep_alive()
    loop = asyncio.get_event_loop()
    loop.create_task(update_bot_status())
    bot.run()
