import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

# --- RENDER TIMEOUT FIX (FLASK SERVER) ---
app = Flask('')

@app.route('/')
def home():
    return "Stylish Font Bot is Live!"

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

bot = Client("VictorStylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- REAL FONT CHANGER MAPPING ---
def get_font(text, font_type):
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fonts = {
        "small_caps": "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",
        "script": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
        "bold_serif": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "double_struck": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
    }
    target = fonts.get(font_type, normal)
    return "".join([target[normal.index(c)] if c in normal else c for c in text])

# --- REAL FONT CHANGER MAPPING (UPGRADED) ---
def get_font(text, font_type):
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fonts = {
        "small_caps": "ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ",
        "script": "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩",
        "bold_serif": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "double_struck": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "bubble": "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
    }
    target = fonts.get(font_type, normal)
    return "".join([target[normal.index(c)] if c in normal else c for c in text])

# --- 100+ STYLISH DESIGN LIST (YOUR NEW TEMPLATES) ---
def get_styles(name):
    # Generating different font versions
    f_sc = get_font(name, "small_caps")
    f_sr = get_font(name, "script")
    f_bs = get_font(name, "bold_serif")
    f_ds = get_font(name, "double_struck")
    f_bb = get_font(name, "bubble")

    # Aapki di hui 100 designs ki list
    templates = [
        "•⎯᪵⎯𐎓⃝꯭✨ ⃪꯭ {} ꯭𝄄𝆺𝆭💖", "✦⸙⃪𐎓꯭꯭✨〭〬 {} ꯭🜲𝆭💞", "🝐‌꯭᪳⸙⃪꯭ {} ⸩⃪🍁", "𓆩꯭〭〬♡‌┼ᶦϻ‌ᷲ‌ꯦ {} !!🌺𓆪",
        "𝆺꯭𝅥🦋꯭𝆭« 𖬱– {} –𖬱 »🦋𝆺𝅥", "★彡 {} 彡★", "꧁༒☬ {} ☬༒꧂", "♡꯭⃕🌙 {} 🌙꯭♡",
        "✧₊⁺ {} ⁺₊✧", "𓆩✨ {} ✨𓆪", "❥⃝🌸 {} 🌸❥⃝", "𐌔𐌉𐌋𐌄𐌔𐌕 • {} •",
        "❦•°✿ {} ✿°•❦", "𖤐⚝ {} ⚝𖤐", "☾⋆⁺₊ {} ₊⋆☽", "✿◡‌ {} ◡‌✿",
        "✦✧ {} ✧✦", "❝ {} ❞", "✨𓆩𝒔𝒕𝒂𝒓𝒔𓆪 {}", "꒰⚘ {} ⚘꒱",
        "❁⃘ {} ❁⃘", "ꗃ꯭❀ {} ❀ꗃ", "ꕤ {} ꕤ", "꧁💎 {} 💎꧂",
        "✩₊˚. {} .˚₊✩", "✧༺ {} ༻✧", "𓍯 {} 𓍯", "✿⤻ {} ⤺✿",
        "𓂃𓈒 {} 𓈒𓂃", "⊰❀ {} ❀⊱", "𓇢𓆸 {} 𓆸𓇣", "✦⎯ {} ⎯✦",
        "🜲꯭✨ {} ✨꯭🜲", "ꗈ᩠ᩚ {} ᩚꗈ", "🦋❣︎ {} ❣︎🦋", "𖠌𖠋 {} 𖠌𖠋",
        "♡‌ {} ‌♡", "✧ෆ {} ෆ✧", "⌗૮₍˶Ó‿Ò ⑅₎ა {}", "𖦹ིྀ {} 𖦹ིྀ",
        "❀︵ {} ︵❀", "🪽₊˚ {} ˚₊🪽", "ꨄ︎ꯄ {} ꨄ︎", "✦𐙚 {} 𐙚✦",
        "⎯‌⎯‌✧ {} ✧⎯‌⎯‌", "𖠿₊˚๑ {} ๑˚₊𖠿", "🌺₊∘ {} ∘₊🌺", "⋆ᜣ꯭᷼ {} ꯭ᜣ᷼⋆",
        "★₊˚˖ {} ˖˚₊★", "꧁𖤐✨ {} ✨𖤐꧂", "꧁𖤍࿐ {} ࿐𖤍꧂", "⚚⟆ {} ⟅⚚",
        "★·.·´¯·.·★ {} ★·.·´¯·.·★", "✦༒ {} ༒✦", "𓆩🜸 {} 🜸𓆪", "❖⃝ {} ❖⃝",
        "☬༄ {} ༄☬", "𖤛𖤐 {} 𖤐𖤛", "★彡⭒ {} ⭒彡★", "⋆✹⃝ {} ✹⃝⋆",
        "ꗃ⋆˙ {} ˙⋆ꗃ", "𐂂𐂃 {} 𐂃𐂂", "❋₊˚ {} ˚₊❋", "✦‌‌ {} ‌‌✦",
        "𖣘࿐ {} ࿐𖣘", "✧∘₊ {} ₊∘✧", "†༺ {} ༻†", "➳❥ {} ❥➳",
        "𖥔˖ {} ˖𖥔", "❦꯭⭐ {} ⭐꯭❦", "⚝₊⌇ {} ⌇₊⚝", "✹𖤐 {} 𖤐✹",
        "𓃠❖ {} ❖𓃠", "₊⌗· {} ·⌗₊", "✦۪۪‌ {} ۪۪‌✦", "❂⃟ {} ❂⃟",
        "𓄹𓄺 {} 𓄺𓄹", "🜲𓆩 {} 𓆪🜲", "✧۫ {} ۫✧", "⟆༶ {} ༶⟅",
        "𖦹ᯓ {} ᯓ𖦹", "☆⑅⃝ {} ⑅⃝☆", "❋∘₊ {} ₊∘❋", "꧁⚡ {} ⚡꧂",
        "❖꯭✨ {} ✨꯭❖", "𐕣𐕘 {} 𐕘𐕣", "✺₊˚ {} ˚₊✺", "✦ᯓ {} ᯓ✦",
        "🖤✧ {} ✧🖤", "𓊈𓊉 {} 𓊈𓊉", "⋆ᜣ᷼ {} ᜣ᷼⋆", "❃ᯓ {} ᯓ❃",
        "✦𓄿 {} 𓄿✦", "🜁𖣘 {} 𖣘🜁", "✧✢ {} ✢✧", "𖨆🦋 {} 🦋𖨆",
        "★𖤓 {} 𖤓★", "✾𖤐 {} 𖤐✾", "𖦊⭒ {} ⭒𖦊", "ꗈ꯭✦ {} ✦ꗈ꯭"
    ]

    results = []
    font_pool = [f_sc, f_sr, f_bs, f_ds, f_bb]
    
    # Mixing fonts with templates (100+ Styles)
    for i, temp in enumerate(templates):
        # Round-robin font selection
        selected_font = font_pool[i % len(font_pool)]
        # Result ko mono font (clickable) mein rakha hai
        results.append(temp.format(selected_font))
        
    return results

# --- UPDATED STYLER HANDLER (TO SHOW ALL) ---
@bot.on_message(filters.text & filters.private)
async def styler(c, m):
    if m.text.startswith("/"): return
    name = m.text
    styles = get_styles(name)
    
    res = f"✨ **ʜᴇʏ {m.from_user.first_name}**, ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴅᴇsɪɢɴs:\n"
    res += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    for s in styles:
        # Code tag ` ` helps in tap-to-copy
        res += f"👉 `{s}`\n\n"
        
    res += "━━━━━━━━━━━━━━━━━━━━\n"
    res += "⚡ **Tap on any style to copy it!**"
    
    # Message length check (Telegram has 4096 char limit)
    if len(res) > 4096:
        for x in range(0, len(res), 4096):
            await m.reply_text(res[x:x+4096])
    else:
        await m.reply_text(res)

# --- KEYBOARDS ---
START_BTN = InlineKeyboardMarkup([
    [InlineKeyboardButton("📢 UPDATES", url="https://t.me/radhesupport"),
     InlineKeyboardButton("🎧 SUPPORT", url="https://t.me/+PKYLDIEYiTljMzMx")],
    [InlineKeyboardButton("📖 HELP & GUIDE", callback_data="help_data")],
    [InlineKeyboardButton("👑 OWNER", url="https://t.me/XenoEmpir")]
])

BACK_BTN = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 BACK", callback_data="start_data")]])

# --- HANDLERS ---
@bot.on_message(filters.command("start") & filters.private)
async def start_cmd(c, m):
    try:
        await bot.send_message(LOG_GROUP, f"👤 **New User:** {m.from_user.mention}\n🆔 `ID: {m.from_user.id}`")
    except: pass

    await m.reply_photo(
        photo=START_IMG,
        caption=(
            f"✨ **ʜᴇʟʟᴏ {m.from_user.first_name} !** ✨\n\n"
            "**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴛʏʟɪsʜ ɴᴀᴍᴇ ᴇᴅɪᴛ ʙᴏᴛ**\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "I can transform your simple name into **100+ Aesthetic** \n"
            "and **Unique Fonts** within seconds! ❤️‍🔥\n\n"
            "**ʜᴏᴡ ᴛᴏ ᴜsᴇ:**\n"
            "● Just type and send your name below.\n"
            "● You will receive a list of amazing designs.\n"
            "● Tap on any style to copy it instantly! 📋\n\n"
            "━━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🚀 **ᴜᴘᴅᴀᴛᴇs:** @radhesupport\n"
            "👑 **ᴏᴡɴᴇʀ:** @XenoEmpir"
        ),
        reply_markup=START_BTN
    )

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(c, m):
    if not m.reply_to_message:
        return await m.reply_text("👉 Reply to a message with `/broadcast`.")
    msg = await m.reply_text("🚀 **Broadcasting...**")
    await m.reply_to_message.copy(m.chat.id)
    await msg.edit("✅ **Broadcast Completed!**")

@bot.on_callback_query()
async def cb_handler(c, cb):
    if cb.data == "help_data":
        await cb.message.edit_caption(
            caption=(
                "📖 **ʜᴇʟᴘ & ɢᴜɪᴅᴇ**\n\n"
                "1️⃣ Send your name in the chat.\n"
                "2️⃣ Bot will auto-change your **Font** & **Style**.\n"
                "3️⃣ Tap on the design to copy it.\n"
                "4️⃣ Use it on Telegram, Instagram, or Games!\n\n"
                "Need more help? Contact @XenoEmpir"
            ),
            reply_markup=BACK_BTN
        )
    elif cb.data == "start_data":
        await start_cmd(c, cb.message)

@bot.on_message(filters.text & filters.private)
async def styler(c, m):
    if m.text.startswith("/"): return
    name = m.text
    styles = get_styles(name)
    res = "🌈 **Your Stylish Fonts:**\n" + "━" * 15 + "\n\n"
    for s in styles:
        res += f"👉 `{s}`\n"
    res += "\n✨ **Tap on style to copy!**"
    await m.reply_text(res)

if __name__ == "__main__":
    keep_alive()
    print("✅ Bot is Online with Font Changer!")
    bot.run()
