from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  

          
rizoel = "✧ 𝘙𝘖𝘕𝘐𝘕 𝑋 𝑆𝑃𝐴𝑀 𝐼𝑍𝑍 𝐴𝐿𝐼𝑉𝐸𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ **𝙱𝙾𝚃 ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"
    
rizoel += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [JOIN](https://t.me/RONIN_FIGHTERS_FD)\n"

rizoel += f"┣➣ **ᴄʜᴀɴɴᴇʟ** : [JOIN](https://t.me/IMPERIAL_ARENA)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [𝙼𝙴𝚁𝙰 𝙱𝙰𝙰𝙿](https://t.me/dushmanxronin) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
