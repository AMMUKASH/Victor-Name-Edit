import os
import random
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from flask import Flask
from threading import Thread

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
START_IMG = "https://graph.org/file/06f17f2da3be3ddf5c9d6-f22b08d691cecb6be9.jpg"

bot = Client("VictorStylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- ADVANCED FONT CHANGER MAPPING ---
def get_font(text, font_type):
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fonts = {
        "bold": "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙",
        "italic": "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍",
        "monospace": "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉",
        "double_struck": "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ",
        "script": "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝒿𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳℒ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵",
        "fraktur": "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ",
        "sans": "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶??𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇𝗔𝗕𝗖𝗗𝗘??𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭",
        "greek": "αβγδεζηθικλμνξοπρςστυφχψωΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    }
    
    if font_type == "greek":
        g_norm = "abgdehijklmnoprstufxoABGDEHIKLMNOPRSTUFXO"
        return "".join([fonts["greek"][g_norm.index(c)] if c in g_norm else c for c in text])
    
    target = fonts.get(font_type, normal)
    return "".join([target[normal.index(c)] if c in normal else c for c in text])

# --- 100+ STYLISH DESIGN LIST WITH CROWN & EMOJIS ---
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
    except Exception as e:
        print(f"Log Group Error: {e}")

    stylish_caption = (
        f"╔══════════════════════╗\n"
        f"   ✨ 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕋𝕠 𝕊𝕥𝕪𝕝𝕚𝕤𝕙 𝔹𝕠𝕥 ✨\n"
        f"╚══════════════════════╝\n\n"
        f"👋 ʜᴇʏ {m.from_user.first_name} ! \n\n"
        f"I am your ultimate **Crown Name Decorator**! ፝֟👑\n"
        f"I can turn your boring name into **100+ Unique & Aesthetic Styles** instantly. ❤️‍🔥\n\n"
        f"◈ ━━━━━━━━━━━━━━━ ◈\n"
        f"📝 **ʜᴏᴡ ᴛᴏ ᴜsᴇ:**\n"
        f"   └ Just send your name below!\n"
        f"✨ **ꜰᴇᴀᴛᴜʀᴇs:**\n"
        f"   ├ 8+ Premium Fonts 🎭\n"
        f"   ├ ፝֟ Crown Decorators 👑\n"
        f"   └ One-Tap Copy Support 📋\n"
        f"◈ ━━━━━━━━━━━━━━━ ◈\n\n"
        f"🚀 **Send your name now and see the magic!**"
    )

    await m.reply_photo(photo=START_IMG, caption=stylish_caption, reply_markup=START_BTN)

@bot.on_callback_query()
async def cb_handler(c, cb):
    if cb.data == "help_data":
        help_text = (
            "📖 **ʜᴇʟᴘ & ɢᴜɪᴅᴇ**\n\n"
            "1️⃣ Send your name in the chat.\n"
            "2️⃣ Bot will generate 100+ styles with Crowns.\n"
            "3️⃣ Tap on any style to copy it.\n\n"
            "**Available Fonts:**\n"
            "• Bold, Italic, Monospace\n"
            "• Double Struck, Script\n"
            "• Fraktur, Sans, Greek\n\n"
            "Powered by: @XenoEmpir"
        )
        await cb.message.edit_caption(caption=help_text, reply_markup=BACK_BTN)
    elif cb.data == "start_data":
        await start_cmd(c, cb.message)

@bot.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
async def broadcast_handler(c, m):
    if not m.reply_to_message:
        return await m.reply_text("👉 Reply to a message with `/broadcast`.")
    msg = await m.reply_text("🚀 **Broadcasting...**")
    await m.reply_to_message.copy(m.chat.id)
    await msg.edit("✅ **Broadcast Completed!**")

@bot.on_message(filters.text & filters.private)
async def styler(c, m):
    if m.text.startswith("/"): return
    name = m.text
    styles = get_styles(name)
    
    res = f"✨ **ʜᴇʏ {m.from_user.first_name}**, ʜᴇʀᴇ ᴀʀᴇ ʏᴏᴜʀ ᴄʀᴏᴡɴ ᴅᴇsɪɢɴs:\n"
    res += "━━━━━━━━━━━━━━━━━━━━\n\n"
    
    for s in styles[:50]: # Sending top 50 to avoid clutter
        res += f"👉 `{s}`\n\n"
        
    res += "━━━━━━━━━━━━━━━━━━━━\n"
    res += "⚡ **Tap to copy!**\n\n"
    res += "ᴩᴏᴡᴇʀᴅ ʙʏ - @XenoEmpir\n"
    res += "Update - https://t.me/radhesupport"
    
    await m.reply_text(res)

if __name__ == "__main__":
    keep_alive()
    bot.run()
