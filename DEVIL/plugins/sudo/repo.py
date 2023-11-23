import asyncio

from pyrogram import filters

import config
from DEVIL import app
from DEVIL.utils.formatters import convert_bytes





@app.on_message(filters.command("repo"))
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "Please wait.."
    )
    up_r = f"[𝗥𝗘𝗣𝗢]({config.UPSTREAM_REPO})"
    up_b = f"[𝗠𝗔𝗦𝗧𝗘𝗥]({config.UPSTREAM_BRANCH})"
    sp_c = f"[𓆩𓆩〭〬𝗗𝗔𝗫𝗫𝗖𝗖 💳]({config.SUPPORT_CHANNEL})"
    sp_g = f"[𓊈𒆜彡[𝐃ҽѵíl 𝐃ҽcմs]彡𒆜𓊉]({config.SUPPORT_CHAT})"
    ow_i = f"⏤͟͟͞͞ 🇩 𝐞𝐯𝐢𝐥𝐞𝐚𝐫𝐬 🇴 𝐰𝐧𝐞𝐫](https://t.me/official_adarsh_op)"

 ##############
 
    text = f"""𝐇𝐞𝐚𝐫𝐭𝐛𝐞𝐞𝐭 𝐁𝐨𝐭 𝐑𝐞𝐩𝐨⌫

    
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎MR White Devil:</u>

𝗥𝗘𝗣𝗢 ❥︎ {up_r}

𝗕𝗥𝗔𝗡𝗖𝗘 ❥︎ {up_b}

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ {sp_c}

𝗚𝗥𝗢𝗨𝗣 ❥︎ {sp_g}

𝗢𝗪𝗡𝗘𝗥 ❥︎ {ow_i}

    """
    await asyncio.sleep(1)
    await mystic.edit_text(text)
