from .. import Riz, SUDO_USERS, rizoelversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/ba87c58f01a6fcb5ef512.jpg"
  

          
rizoel = "β§ πππππ π πππ΄π πΌππ π΄πΏπΌππΈπΈ β§\n\n"

rizoel += f"ββββββββββββββββββββ\n"

rizoel += f"β£β£ **α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `3.9.6`\n"

rizoel += f"β£β£ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `{version.__version__}`\n"

rizoel += f"β£β£ **π±πΎπ α΄ α΄ΚsΙͺα΄Ι΄**  : `{rizoelversion}`\n"
    
rizoel += f"β£β£ **sα΄α΄α΄α΄Κα΄** : [JOIN](https://t.me/RONIN_FIGHTERS_FD)\n"

rizoel += f"β£β£ **α΄Κα΄Ι΄Ι΄α΄Κ** : [JOIN](https://t.me/IMPERIAL_ARENA)\n"

rizoel += f"ββββββββββββββββββββ\n\n"

rizoel += f"π€ [πΌπ΄ππ° π±π°π°πΏ](https://t.me/dushmanxronin) π€"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
