# Doorkeeper telegram bot
The bot welcomes new users.

## Getting Started
* Build image:
```
docker build . -t telegram_doorkeeper
```
* Run container:
```
docker run -d --restart unless-stopped \
--name telegram_doorkeeper_bot \
-e bot_token={TOKEN} \
telegram_doorkeeper
```
