import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant

# --- CONFIGURATION (UPDATED) ---
API_ID = 34135757  # Corrected: Numbers only
API_HASH = "d3d5548fe0d98eb1fb793c2c37c9e5c8"  # Corrected: Inside quotes
BOT_TOKEN = "8583239839:AAH6JyFb1cRqmq-XKf0Z6ns7yRYPoL9_nU8"

OWNER_ID = 8482447535
LOG_GROUP = -1003867805165
START_IMG = "https://graph.org/file/06f17f2da3be3ddf5c9d6-f22b08d691cecb6be9.jpg"
FSUB_CHANNEL = "radhesupport" 

app = Client("StylishBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- CUSTOM STYLES LIST ---
def get_styles(name):
    return [
        f"•⎯᪵⎯𐎓⃝꯭✨ ⃪꯭ {name} ꯭𝄄𝆺𝆭💖", f"✦⸙⃪𐎓꯭꯭✨〭〬 {name} ꯭🜲𝆭💞",
        f"🝐꯭̽᪳⸙⃪꯭ {name} ⸩⃪🍁", f"𓆩꯭〭〬♡͢┼ᶦϻ‌ᷲ‌ꯦ {name} !!🌺𓆪",
        f"𝆺꯭𝅥🦋꯭𝆭« 𖬱– {name} –𖬱 »🦋𝆺𝅥", f"★彡 {name} 彡★",
        f"꧁༒☬ {name} ☬༒꧂", f"♡꯭⃕🌙 {name} 🌙꯭♡",
        f"✧₊⁺ {name} ⁺₊✧", f"𓆩✨ {name} ✨𓆪",
        f"❥⃝🌸 {name} 🌸❥⃝", f"𐌔𐌉𐌋𐌄𐌔𐌕 • {name} •",
        f"❦•°✿ {name} ✿°•❦", f"𖤐⚝ {name} ⚝𖤐",
        f"☾⋆⁺₊ {name} ₊⋆☽", f"✿◡̈ {name} ◡̈✿",
        f"✦✧ {name} ✧✦", f"✨𓆩𝒔𝒕𝒂𝒓𝒔𓆪 {name}",
        f"꒰⚘ {name} ⚘꒱", f"ꗃ꯭❀ {name} ❀ꗃ",
        f"꧁💎 {name} 💎꧂", f"✩₊˚. {name} .˚₊✩",
        f"𓇢𓆸 {name} 𓆸𓇣", f"🜲꯭✨ {name} ✨꯭🜲",
        f"🦋❣︎ {name} ❣︎🦋", f"🪽₊˚ {name} ˚₊🪽",
        f"✦𐙚 {name} 𐙚✦", f"꧁𖤐✨ {name} ✨𖤐꧂",
        f"★·.·´¯·.·★ **{name}** ★·.·´¯·.·★", f"𓆩🜸 {name} 𓆪🜲",
        f"☬༄ {name} ༄☬", f"★彡⭒ {name} ⭒彡★",
        f"𖣘࿐ {name} ࿐𖣘", f"†༺ {name} ༻†",
        f"❦꯭⭐ {name} ⭐꯭❦", f"𓃠❖ {name} ❖𓃠",
        f"🜲𓆩 {name} 𓆪🜲", f"꧁⚡ {name} ⚡꧂",
        f"❖꯭✨ {name} ✨꯭❖"
    ]

# --- START HANDLER ---
@app.on_message(filters.command("start") & filters.private)
async def start(bot, message):
    try:
        await bot.get_chat_member(FSUB_CHANNEL, message.from_user.id)
    except UserNotParticipant:
        return await message.reply_text(
            f"❌ **ᴀᴄᴄᴇss ᴅᴇɴɪᴇᴅ!**\n\nᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ ᴊᴏɪɴ ᴜᴘᴅᴀᴛᴇs ✨", url=f"https://t.me/{FSUB_CHANNEL}")]])
        )

    log_text = (
        f"🚀 **#NewUser**\n\n"
        f"👤 **Name:** {message.from_user.first_name}\n"
        f"🆔 **ID:** `{message.from_user.id}`\n"
        f"🔗 **User Link:** [Click Here](tg://user?id={message.from_user.id})"
    )
    await bot.send_message(LOG_GROUP, log_text)
    
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("✨ ᴜᴘᴅᴀᴛᴇ ✨", url="https://t.me/radhesupport"),
         InlineKeyboardButton("🎧 sᴜᴘᴘᴏʀᴛ 🎧", url="https://t.me/+PKYLDIEYiTljMzMx")],
        [InlineKeyboardButton("👑 ᴏᴡɴᴇʀ 👑", url="https://t.me/XenoEmpir")]
    ])
    
    start_caption = (
        f"👋 **ʜᴇʏ {message.from_user.first_name}!**\n\n"
        "⚡ **ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ sᴛʏʟɪsʜ ɴᴀᴍᴇ ᴇᴅɪᴛ ʙᴏᴛ** ⚡\n\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🎨 **ɪ ᴄᴀɴ ᴄᴏɴᴠᴇʀᴛ ʏᴏᴜʀ sɪᴍᴘʟᴇ ɴᴀᴍᴇ ɪɴᴛᴏ 50+ ᴀᴇsᴛʜᴇᴛɪᴄ ᴀɴᴅ sᴛʏʟɪsʜ ғᴏɴᴛs.**\n\n"
        "🛠 **ʜᴏᴡ ᴛᴏ ᴜsᴇ:**\n"
        "ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ɴᴀᴍᴇ ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ʙᴇsᴛ ᴅᴇsɪɢɴs.\n"
        "━━━━━━━━━━━━━━━━━━━━━━━━"
    )
    
    await message.reply_photo(photo=START_IMG, caption=start_caption, reply_markup=buttons)

# --- STYLISH NAME GENERATOR ---
@app.on_message(filters.text & filters.private)
async def send_styles(bot, message):
    if message.text.startswith("/"): return
    
    name = message.text
    all_styles = get_styles(name)
    
    response = "🎭 **ʏᴏᴜʀ sᴛʏʟɪsʜ ɴᴀᴍᴇs:**\n━━━━━━━━━━━━━━━\n\n"
    for s in all_styles:
        response += f"`{s}`\n\n"
    
    response += "━━━━━━━━━━━━━━━\n💡 *ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ!*"
    await message.reply_text(response)

print("Bot is Started Successfully!")
app.run()
