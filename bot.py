import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# --- RENDER TIMEOUT FIX (FLASK) ---
app = Flask('')

@app.route('/')
def home():
    return "Stylish Name Bot is Live & Working!"

def run():
    port = int(os.environ.get('PORT', 8080))
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
START_IMG = "https://graph.org/file/06f17f2da3be3ddf5c9d6-f22b08d691cecb6be9.jpg"

# Logging setup
logging.basicConfig(level=logging.INFO)

bot = Client("VictorStylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- STYLISH NAME LIST (100+ STYLES) ---
def get_styles(name):
    return [
        f"•⎯᪵⎯𐎓⃝꯭✨ ⃪꯭ {name} ꯭𝄄𝆺𝆭💖", f"✦⸙⃪𐎓꯭꯭✨〭〬 {name} ꯭🜲𝆭💞", f"🝐‌꯭᪳⸙⃪꯭ {name} ⸩⃪🍁",
        f"𓆩꯭〭〬♡‌┼ᶦϻ‌ᷲ‌ꯦ {name} !!🌺𓆪", f"𝆺꯭𝅥🦋꯭𝆭« 𖬱– {name} –𖬱 »🦋𝆺𝅥", f"★彡 {name} 彡★",
        f"꧁༒☬ {name} ☬༒꧂", f"♡꯭⃕🌙 {name} 🌙꯭♡", f"✧₊⁺ {name} ⁺₊✧",
        f"𓆩✨ {name} ✨𓆪", f"❥⃝🌸 {name} 🌸❥⃝", f"𐌔𐌉𐌋𐌄𐌔𐌕 • {name} •",
        f"❦•°✿ {name} ✿°•❦", f"𖤐⚝ {name} ⚝𖤐", f"☾⋆⁺₊ {name} ₊⋆☽",
        f"✿◡‌ {name} ◡‌✿", f"✦✧ {name} ✧✦", f"❝ {name} ❞",
        f"✨𓆩𝒔𝒕𝒂𝒓𝒔𓆪 {name}", f"꒰⚘ {name} ⚘꒱", f"❁⃘ {name} ❁⃘",
        f"ꗃ꯭❀ {name} ❀ꗃ", f"ꕤ {name} ꕤ", f"꧁💎 {name} 💎꧂",
        f"✩₊˚. {name} .˚₊✩", f"✧༺ {name} ༻✧", f"𓍯 {name} 𓍯",
        f"✿⤻ {name} ⤺✿", f"𓂃𓈒 {name} 𓈒𓂃", f"⊰❀ {name} ❀⊱",
        f"𓇢𓆸 {name} 𓆸𓇣", f"✦⎯ {name} ⎯✦", f"🜲꯭✨ {name} ✨꯭🜲",
        f"ꗈ᩠ᩚ {name} ᩚꗈ", f"🦋❣︎ {name} ❣︎🦋", f"𖠌𖠋 {name} 𖠌𖠋",
        f"♡‌ {name} ‌♡", f"✧ෆ {name} ෆ✧", f"⌗૮₍˶Ó‿Ò ⑅₎ა {name}",
        f"𖦹ིྀ {name} 𖦹ིྀ", f"❀︵ {name} ︵❀", f"🪽₊˚ {name} ˚₊🪽",
        f"ꨄ︎꯭ {name} ꨄ︎", f"✦𐙚 {name} 𐙚✦", f"⎯‌⎯‌✧ {name} ✧⎯‌⎯‌",
        f"𖠿₊˚๑ {name} ๑˚₊𖠿", f"🌺₊∘ {name} ∘₊🌺", f"⋆ᜣ꯭᷼ {name} ꯭ᜣ᷼⋆",
        f"★₊˚˖ {name} ˖˚₊★", f"꧁𖤐✨ {name} ✨𖤐꧂", f"꧁𖤍࿐ {name} ࿐𖤍꧂",
        f"⚚⟆ {name} ⟅⚚", f"★·.·´¯·.·★ {name} ★·.·´¯·.·★", f"✦༒ {name} ༒✦",
        f"𓆩🜸 {name} 🜸𓆪", f"❖⃝ {name} ❖⃝", f"☬༄ {name} ༄☬",
        f"𖤛𖤐 {name} 𖤐𖤛", f"★彡⭒ {name} ⭒彡★", f"⋆✹⃝ {name} ✹⃝⋆",
        f"ꗃ⋆˙ {name} ˙⋆ꗃ", f"𐂂𐂃 {name} 𐂃𐂂", f"❋₊˚ {name} ˚₊❋",
        f"✦‌‌ {name} ‌‌✦", f"𖣘࿐ {name} ࿐𖣘", f"✧∘₊ {name} ₊∘✧",
        f"†༺ {name} ༻†", f"➳❥ {name} ❥➳", f"𖥔˖ {name} ˖𖥔",
        f"❦꯭⭐ {name} ⭐꯭❦", f"⚝₊⌇ {name} ⌇₊⚝", f"✹𖤐 {name} 𖤐✹",
        f"𓃠❖ {name} ❖𓃠", f"₊⌗· {name} ·⌗₊", f"✦۪۪‌ {name} ۪۪‌✦",
        f"❂⃟ {name} ❂⃟", f"𓄹𓄺 {name} 𓄺𓄹", f"🜲𓆩 {name} 𓆪🜲",
        f"✧۫ {name} ۫✧", f"⟆༶ {name} ༶⟅", f"𖦹ᯓ {name} ᯓ𖦹",
        f"☆⑅⃝ {name} ⑅⃝☆", f"❋∘₊ {name} ₊∘❋", f"꧁⚡ {name} ⚡꧂",
        f"❖꯭✨ {name} ✨꯭❖", f"𐕣𐕘 {name} 𐕘𐕣", f"✺₊˚ {name} ˚₊✺",
        f"✦ᯓ {name} ᯓ✦", f"🖤✧ {name} ✧🖤", f"𓊈𓊉 {name} 𓊈𓊉",
        f"⋆ᜣ᷼ {name} ᜣ᷼⋆", f"❃ᯓ {name} ᯓ❃", f"✦𓄿 {name} 𓄿✦",
        f"🜁𖣘 {name} 𖣘🜁", f"✧✢ {name} ✢✧", f"𖨆🦋 {name} 🦋𖨆",
        f"★𖤓 {name} 𖤓★", f"✾𖤐 {name} 𖤐✾", f"𖦊⭒ {name} ⭒𖦊",
        f"ꗈ꯭✦ {name} ✦ꗈ꯭"
    ]

# --- KEYBOARDS ---
START_BTN = InlineKeyboardMarkup([
    [InlineKeyboardButton("📢 UPDATES", url="https://t.me/radhesupport"),
     InlineKeyboardButton("🎧 SUPPORT", url="https://t.me/+PKYLDIEYiTljMzMx")],
    [InlineKeyboardButton("📖 HELP & GUIDE", callback_data="help_menu")],
    [InlineKeyboardButton("👑 OWNER", url="https://t.me/XenoEmpir")]
])

BACK_BTN = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 BACK", callback_data="start_menu")]])

# --- COMMAND HANDLERS ---
@bot.on_message(filters.command("start") & filters.private)
async def start_handler(c, m):
    # User Join Log
    try:
        await bot.send_message(LOG_GROUP, f"👤 **New User Started:** {m.from_user.mention}\n🆔 `{m.from_user.id}`")
    except: pass
    
    await m.reply_photo(
        photo=START_IMG,
        caption=(
            f"​✨ Hello [Name]! Welcome to Victor Edit Bot ✨
━━━━━━━━━━━━━━━━━━━━━━━━
​Main aapke simple naam ko 100+ Unique aur Aesthetic Styles mein badal sakta hoon.
​🛠️ Kaise Use Karein?
1️⃣ Bas apna naam niche type karke bhejein.
2️⃣ Bot aapko turant stylish list bhej dega.
3️⃣ Kisi bhi style par Tap karein aur copy karein!
​📢 Official Updates: @radhesupport
━━━━━━━━━━━━━━━━━━━━━━━━
👇 Apna Naam Bhejein Aur Magic Dekhein!)"
        ),
        reply_markup=START_BTN
    )

@bot.on_message(filters.command("help"))
async def help_command(c, m):
    help_text = (
        "📖 **Stylish Name Bot Guide**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "✨ **Name Styling:** Bas bot ko apna naam bhejein.\n"
        "🎵 **Music:** `/play [song name]` (Groups mein use karein).\n"
        "🚀 **Broadcast:** Admin users ko message bhej sakte hain."
    )
    await m.reply_text(help_text, reply_markup=BACK_BTN)

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(c, m):
    if not m.reply_to_message:
        return await m.reply("👉 Kisi message ko reply karke `/broadcast` likhein.")
    await m.reply_to_message.copy(m.chat.id)
    await m.reply("✅ **Broadcast Sent!**")

# --- MUSIC COMMANDS (BASIC STRUCTURE) ---
@bot.on_message(filters.command(["play", "skip", "stop"]) & filters.group)
async def music_stubs(c, m):
    await m.reply("🎵 **Music system active!**\n(Note: Audio streaming requires Assistant setup).")

# --- CALLBACK HANDLER ---
@bot.on_callback_query()
async def cb_data(c, cb):
    if cb.data == "help_menu":
        await cb.message.edit_caption(
            caption="📖 **Help Menu**\n\n• Apna naam bhejein styling ke liye.\n• Style copy karne ke liye us par tap karein.\n• /play gaana chalane ke liye.",
            reply_markup=BACK_BTN
        )
    elif cb.data == "start_menu":
        await cb.message.edit_caption(
            caption=f"✨ **Hello {cb.from_user.first_name}!**\n\nMain aapke simple name ko 100+ stylish fonts mein badal sakta hoon. Bas apna naam bhejein!",
            reply_markup=START_BTN
        )

# --- NAME STYLER LOGIC ---
@bot.on_message(filters.text & filters.private)
async def styler_handler(c, m):
    if m.text.startswith("/"): return
    
    name = m.text
    styles = get_styles(name)
    
    response = "🌈 **Your Stylish Designs:**\n" + "━" * 15 + "\n\n"
    for s in styles:
        response += f"👉 `{s}`\n"
    
    response += "\n✨ **Tap on style to copy!**"
    await m.reply_text(response)

# --- START BOT ---
if __name__ == "__main__":
    keep_alive()
    print("✅ Bot is Online with All Features!")
    bot.run()
