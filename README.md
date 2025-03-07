# Auto-Approve-Bot
👾 Hey I'll Accept telegram join requests. Easy to use and simple.

## 🚀 Demo Bot
- [@StarkApprovedBot](https://t.me/StarkApprovedBot)

<h2>〽️ Deploy Me </h2> 
  
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
