from .. import Riz, SUDO_USERS
from telethon import events
from time import time
from datetime import datetime

    
HELP_PIC = "https://telegra.ph/file/d0c52ab731fce56412fdd.jpg"

RiZoeLX = "π₯ πππππ π πππΌππ₯\n\n"
 
RiZoeLX += f"__α΄α΄α΄s α΄α΄ α΄ΙͺΚα΄ΚΚα΄ ΙͺΙ΄ βπβπβ π πβπΈπ__\n\n"

RiZoeLX += f" β§ πππ΄ππ±πΎπ π²πΌπ³π β§\n\n"

RiZoeLX += f" `.ping` - to check ping\n `.alive` - to check bot alive/version (only main userbot will reply)\n `.setname` - to change Name\n .`inviteall` - to add members using spam bots\n .`restart` - to restart all spam bots\n\n"
 
RiZoeLX += f" β§ πΉπΎπΈπ½/π»π΄π°ππ΄ π²πΌπ³π β§\n\n"

RiZoeLX += f" `.join` - to join public channel/groups\n `.pjoin` - to join public channel/groups\n `.leave` - to leave public/private channel/groups\n\n"
 
RiZoeLX += f" β§ ππΏπ°πΌ π²πΌπ³π β§\n\n"

RiZoeLX += f" `.raid` - to raid\n `.replyraid` - to active reply raid\n `.dreplyraid` - to de-active reply raid\n `.spam` - this cmd use for Normal spam\n `.bigspam` - this cmd use for big spam\n `.delayspam` - this cmd use for delay spam\n\n"
 
RiZoeLX += f"ALL CMDS WITH DETAILS [HERE.](https://telegra.ph/%F0%9D%97%A5%F0%9D%97%9C%F0%9D%97%AD%F0%9D%97%A2%F0%9D%97%98%F0%9D%97%9F-%F0%9D%97%AB-%F0%9D%97%A6%F0%9D%97%A3%F0%9D%97%94%F0%9D%97%A0-10-15)\n\n"
 
RiZoeLX += f"Β© @DUSHMANXRONIN | @IMPERIAL_ARENA\n"


@Riz.on(events.NewMessage(pattern=r"\.help"))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=RiZoeLX)                                                         
