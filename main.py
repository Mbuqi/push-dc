import requests
import time
import os
from colorama import Fore

channel_id = input("Masukkan ID channel: ")
waktu1 = int(input("Set Kirim Pesan: "))

time.sleep(1)
print("MULAI")
time.sleep(1)

payload = {
         "content" : """⛔ALERTA⛔ALERTA⛔
✅CHEAP STOCK 100K SSP  <:Arrow:850540193626193941> AT VII23✅
✅CHEAP STOCK 100K SSP  <:Arrow:850540193626193941> AT VII23✅
✅CHEAP STOCK 100K SSP  <:Arrow:850540193626193941> AT VII23✅"""
}
headers = {
          "Authorization" : "OTg0NDY3MzY0NzQ3ODI5MjQ4.GVOQ19.gjkcSLuR_RsB-j41Pcsfh6E_qVlLP0tpVE5uS0"
}
r = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", data=payload, headers=headers)
        print(Fore.BLUE + "Sent message: ")
        print(Fore.YELLOW + payload['content'])
else:
time.sleep(waktu1)
