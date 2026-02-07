import os
import random
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from flask import Flask
from threading import Thread
from motor.motor_asyncio import AsyncIOMotorClient

# --- RENDER TIMEOUT FIX (FLASK SERVER) ---
app = Flask('')

@app.route('/')
def home():
    return "Stylish Crown Bot is Live!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- CONFIGURATION ---
API_ID = 34135757
API_HASH = "d3d5548fe0d98eb1fb793c2c37c9e5c8"
BOT_TOKEN = "8583239839:AAHsTIG-8b4Fnk3Q9t-h6N4zBoX_1yfQC8k"
OWNER_ID = 8482447535
LOG_GROUP = -1003867805165
MONGO_URL = "mongodb+srv://misssqn:VICTOR01@cluster0.3otqmso.mongodb.net/?appName=Cluster0"
START_IMG = "https://graph.org/file/06f17f2da3be3ddf5c9d6-f22b08d691cecb6be9.jpg"
FSUB_CHANNEL = "radhesupport" # Channel username without @

bot = Client("VictorStylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# MongoDB Setup
db_client = AsyncIOMotorClient(MONGO_URL)
db = db_client["StylishBotDB"]
users_col = db["users"]

# --- DATABASE FUNCTIONS ---
async def add_user(user_id):
    if not await users_col.find_one({"user_id": user_id}):
        await users_col.insert_one({"user_id": user_id})

async def get_all_users():
    return [doc["user_id"] async for doc in users_col.find({})]

# --- FONT CHANGER MAPPING ---
def get_font(text, font_type):
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fonts = {
        "bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "italic": "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍",
        "monospace": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
        "double_struck": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ\Oℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "script": "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓌𝓍𝓎𝒿𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳℒ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "fraktur": "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "sans": "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭",
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
    for i in range(100):
        temp = templates[i % len(templates)]
        font = f_pool[i % len(f_pool)]
        emo = random.choice(extra_emojis)
        results.append(temp.format(crown + emo, font))
    return results

# --- KEYBOARDS ---
START_BTN = InlineKeyboardMarkup([
    [InlineKeyboardButton("♻ 𝐀ᴅᴅ 𝐌𝝴 𝝸𝝶 𝐘𝞂𝞄𝐑 𝐆𝐑𝞂𝞄𝞀 ♻", url="https://t.me/StylishNamBot?startgroup=true")],
    [InlineKeyboardButton("❂ 𝐔𝛒ᴅ𝛂𝛕𝛆 ❂", url="https://t.me/radhesupport"),
     InlineKeyboardButton("❂ 𝐒𝛖𝛒𝛒𝛔ʀ𝛕 ❂", url="https://t.me/+PKYLDIEYiTljMzMx")],
    [InlineKeyboardButton("❂ 𝐇𝛆𝛊𝛒 & 𝐆𝛖𝛊ᴅ𝛆 ❂", callback_data="help_data")]
])

BACK_BTN = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 𝐁𝐀𝐂𝐊", callback_data="start_data")]])

# --- FSUB CHECK ---
async def is_subscribed(c, m):
    if not FSUB_CHANNEL: return True
    try:
        user = await c.get_chat_member(FSUB_CHANNEL, m.from_user.id)
        if user.status == "kicked": return False
        return True
    except UserNotParticipant: return False
    except Exception: return True

# --- HANDLERS ---
@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(c, m):
    if not await is_subscribed(c, m):
        join_btn = InlineKeyboardMarkup([[InlineKeyboardButton("✨ 𝐉ᴏɪɴ 𝐂ʜᴀɴɴᴇʟ ✨", url=f"https://t.me/{FSUB_CHANNEL}")]])
        return await m.reply_text(
            f"❌ **𝐀ᴄᴄᴇ𝐬𝐬 𝐃ᴇɴɪᴇᴅ!**\n\n𝐏ʟᴇᴀ𝐬ᴇ 𝐉ᴏɪɴ 𝐎ᴜʀ 𝐂ʜᴀɴɴᴇʟ 𝐓ᴏ 𝐔𝐬ᴇ 𝐓ʜɪ𝐬 𝐁ᴏᴛ.",
            reply_markup=join_btn
        )

    await add_user(m.from_user.id)
    try:
        await bot.send_message(LOG_GROUP, f"👤 **New User:** {m.from_user.mention}\n🆔 `ID: {m.from_user.id}`")
    except: pass

    stylish_caption = (
        f"╔══════════════════════╗\n"
        f"   ✨ 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠 𝕊𝕥𝕪𝕝𝕚𝕤𝕙 𝔹𝕠𝕥 ✨\n"
        f"╚══════════════════════╝\n\n"
        f"👋 ʜᴇʏ {m.from_user.first_name} ! \n\n"
        f"I am your ultimate **Crown Name Decorator**! ፝֟👑\n"
        f"I can turn your boring name into **100+ Unique & Aesthetic Styles** instantly. ❤️‍🔥\n\n"
        f"🚀 **Send your name now and see the magic!**"
    )
    await m.reply_photo(photo=START_IMG, caption=stylish_caption, reply_markup=START_BTN)

@bot.on_callback_query()
async def cb_handler(c, cb):
    if cb.data == "help_data":
        help_text = "📖 **𝐇ᴇʟᴘ & 𝐆ᴜɪᴅᴇ**\n\n1️⃣ Send your name in the chat.\n2️⃣ Bot will generate 100+ styles.\n3️⃣ Tap to copy."
        await cb.message.edit_caption(caption=help_text, reply_markup=BACK_BTN)
    elif cb.data == "start_data":
        await start_cmd(c, cb.message)

@bot.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats_handler(c, m):
    count = await users_col.count_documents({})
    await m.reply_text(f"📊 **Total Users:** `{count}`")

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(c, m):
    if not m.reply_to_message: return await m.reply_text("Reply to a message!")
    all_users = await get_all_users()
    msg = await m.reply_text("🚀 Broadcasting...")
    done = 0
    for user_id in all_users:
        try:
            await m.reply_to_message.copy(user_id)
            done += 1
        except: pass
    await msg.edit(f"✅ **Broadcast Done!**\nSent to `{done}` users.")

@bot.on_message(filters.text & filters.private)
async def styler(c, m):
    if m.text.startswith("/"): return
    if not await is_subscribed(c, m):
        return await m.reply_text("❌ Join @radhesupport first!")

    name = m.text
    styles = get_styles(name)
    res = f"✨ **ʜᴇʏ {m.from_user.first_name}**, ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴄʀᴏᴡɴ ᴅᴇsɪɢɴs:\n━━━━━━━━━━━━━━━━━━━━\n\n"
    
    for s in styles[:50]:
        res += f"👉 `{s}`\n\n"
    
    res += "━━━━━━━━━━━━━━━━━━━━\n⚡ **Tap to copy!**"
    await m.reply_text(res)

if __name__ == "__main__":
    keep_alive()
    bot.run()
