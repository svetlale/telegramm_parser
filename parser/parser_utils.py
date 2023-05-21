from telethon import TelegramClient
from config import LoginCfg


login_cfg = LoginCfg()
channels = ["https://t.me/hammspub"]
messages = []

with TelegramClient(login_cfg.phone_number, api_id=login_cfg.api_id, api_hash=login_cfg.api_hash) as client:
    for num, message in enumerate(client.iter_messages(*channels)):
        print(f"Message number {num} from last.")
        print(message.sender_id, ':', message.text)
        print("____________________________________________________________________________\n\n")
        messages.append(message.text)
