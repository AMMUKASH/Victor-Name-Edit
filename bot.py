import os
import logging
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# --- RENDER PORT FIX (FLASK SERVER) ---
app = Flask('')
@app.route('/')
def home(): return "Stylish Name Bot is Live!"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    Thread(target=run).start()

# --- CONFIGURATION ---
API_ID = 34135757
API_HASH = "d3d5548fe0d98eb1fb793c2c37c9e5c8"
BOT_TOKEN = "8583239839:AAHsTIG-8b4Fnk3Q9t-h6N4zBoX_1yfQC8k"
OWNER_ID = 8482447535
LOG_GROUP = -1003867805165
START_IMG = "https://graph.org/file/06f17f2da3be3ddf5c9d6-f22b08d691cecb6be9.jpg"

bot = Client("StylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- STYLISH NAME LIST ---
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
    [InlineKeyboardButton("📢 Updates", url="https://t.me/radhesupport"),
     InlineKeyboardButton("🎧 Support", url="https://t.me/+PKYLDIEYiTljMzMx")],
    [InlineKeyboardButton("📖 Help & Guide", callback_data="help_guide")],
    [InlineKeyboardButton("👤 Developer", url="https://t.me/XenoEmpir")]
])

HELP_BTN = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Back", callback_data="start_back")]])

# --- COMMANDS ---
@bot.on_message(filters.command("start") & filters.private)
async def start(c, m):
    await bot.send_message(LOG_GROUP, f"👤 **New User Started:** {m.from_user.mention}\n🆔 `ID: {m.from_user.id}`")
    await m.reply_photo(
        photo=START_IMG,
        caption=(
            f"✨ **Hello {m.from_user.first_name}!** ✨\n\n"
            "Main aapke simple name ko **100+ Aesthetic aur Unique Fonts** mein badal sakta hoon.\n\n"
            "**🛠 Kaise Use Karein?**\n"
            "Bas niche apna naam type karke bhejein aur magic dekhein!\n\n"
            "👇 **Apna Naam Bhejein:**"
        ),
        reply_markup=START_BTN
    )

@bot.on_message(filters.command("help") & filters.private)
async def help_cmd(c, m):
    help_text = (
        "📖 **Stylish Name Bot Guide**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "1️⃣ **Fonts Kaise Banayein?**\n"
        "Sirf bot ko apna naam text message mein bhejein.\n\n"
        "2️⃣ **Copy Kaise Karein?**\n"
        "Bot aapko ek list bhejega, usme se kisi bhi style par **Tap** karke aap copy kar sakte hain.\n\n"
        "3️⃣ **Limit:**\n"
        "Koi limit nahi hai! Jitne chahe utne stylish names banayein."
    )
    await m.reply_text(help_text, reply_markup=HELP_BTN)

# --- BROADCAST (OWNER ONLY) ---
@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast(c, m):
    if not m.reply_to_message:
        return await m.reply_text("👉 Kisi message ko reply karke `/broadcast` likhein.")
    
    msg = await m.reply_text("🚀 **Broadcasting in progress...**")
    # Note: Simple reply for now. Mass broadcast requires DB.
    await m.reply_to_message.copy(m.chat.id) 
    await msg.edit("✅ **Broadcast Completed!**")

# --- CALLBACK HANDLER ---
@bot.on_callback_query()
async def cb_handler(c, cb):
    if cb.data == "help_guide":
        await cb.message.edit_caption(
            caption="📖 **Help & Guide**\n\n• Bot ko apna naam bhejein.\n• Stylish list se apna fav style copy karein.\n• Use /help for more info.",
            reply_markup=HELP_BTN
        )
    elif cb.data == "start_back":
        await cb.message.edit_caption(
            caption=f"✨ **Hello {cb.from_user.first_name}!** ✨\n\nMain aapke simple name ko 100+ Aesthetic fonts mein badal sakta hoon. Bas apna naam bhejein!",
            reply_markup=START_BTN
        )

# --- NAME STYLER LOGIC ---
@bot.on_message(filters.text & filters.private)
async def style_name(c, m):
    if m.text.startswith("/"): return
    
    name = m.text
    styles = get_styles(name)
    
    res = "🌈 **Your Stylish Designs:**\n" + "━" * 15 + "\n\n"
    for s in styles:
        res += f"👉 `{s}`\n"
    
    res += "\n✨ **Tap on style to copy!**"
    await m.reply_text(res)

if __name__ == "__main__":
    keep_alive() # Starts Flask server for Render
    print("✅ Bot is Online & Stylish!")
    bot.run()
