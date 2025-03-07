# Auto-Approve-Bot
👾 Hey I'll Accept telegram join requests. Easy to use and simple.

## 🚀 Demo Bot
- [@StarkApprovedBot](https://t.me/StarkApprovedBot)

<h2>〽️ Deploy Me </h2> 

<details><summary>📌 Deploy to Koyeb </summary>

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=auto-approve-bot&repository=techshriyfra%2FAuto-Approve-bot&branch=main&run_command=gunicorn+app%3Aapp+%26+python3+bot.py&instance_type=free&regions=was&instances_min=0&env%5BAPI_HASH%5D=abcdefg&env%5BAPI_ID%5D=0112234&env%5BBOT_TOKEN%5D=1234567891%3AAdDfgFRFVVfDEhdhyjjvjjftSEW&env%5BCHID%5D=-1000112234&env%5BFSUB%5D=Tech_Shreyansh&env%5BMONGO_URI%5D=mongodb%2Bsrv%3A%2F%2F%3Cusername%3E%3A%3Cpassword%3E%40cluster.mongodb.net%2F%3Cdbname%3E%3FretryWrites%3Dtrue%26w%3Dmajority%26tls%3Dtrue&env%5BSUDO%5D=241845268)
</details>
  
<details><summary>📌 Deploy to Heroku </summary>
  
<a href="https://heroku.com/deploy?template=https://github.com/MrGhostsx/Auto-Approve-bot"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"></p></a>
</details>

<details><summary>📌 Deploy to Railway </summary>
  
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/w7jSPk)
</details>
  
<details><summary>📌 Deploy to Okteto </summary>
  
[![Deploy on Okteto](https://okteto.com/develop-okteto.svg)](https://cloud.okteto.com/deploy?repository=https://github.com/MrGhostsx/Auto-Approve-bot)
</details>

<details><summary>📌 Deploy to VPS/Local </summary>


  ```ssh
  git clone https://github.com/MrGhostsx/Auto-Approve-bot
  pip3 install -r requirements.txt
  # fill config.py vars
  python3 bot.py
  ```

</details>

## 🏷 Environment Variables
  - `API_ID` - Your Telegram API ID.Get it [Here](my.telegram.org)
  - `API_HASH` - Your Telegram API HASH.Get it [Here](my.telegram.org)
  - `MONGO_URI` - Add MongoDB Database URI.
  - `BOT_TOKEN` - Your Bot Token. Get it from [Here](https://t.me/BotFather)
  - `CHID` - Your Force subscribe channel id Get it from @MissRose_Bot
  - `FSUB` - Force subscribe channel username without `@`
  - `SUDO` - bot owners Id/ ids ( for broadcast and stats cmds). for multiple use space.

  ```Raw
API_HASH=abcdefg
API_ID=0112234
BOT_TOKEN=1234567891:AdDfgFRFVVfDEhdhyjjvjjftSEW
CHID=-1000112234
FSUB=Tech_Shreyansh
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<dbname>?retryWrites=true&w=majority&tls=true
SUDO=241845268
```
  
### 💫 Credits
 - [Mr.Ghosts](https://github.com/MrGhostsx) for pyrogram
 - [Me](https://github.com/TechyShreyansh) for Nothing 😅
