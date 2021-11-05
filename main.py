import threading
import requests
from time import sleep
from json import loads

def sender(webhook_id, webhook_token, username, content):
    payload = {"content": content, "username": username}
    req = requests.post('https://discord.com/api/v9/webhooks/' + webhook_id + "/" + webhook_token, data=payload)
    try:
        parsed = loads(req.text)
        if parsed["message"] == "You are being rate limited.":
            sleep(int(parsed["retry_after"]))
            requests.post('https://discord.com/api/v9/webhooks/' + webhook_id + "/" + webhook_token, data=payload)
    except Exception as e:
        pass
def send():
    times = input("How many messages you want to send? ")
    webhook_id = input("Insert here webhook id: ")
    webhook_token = input("Insert here webhook token: ")
    username = input("Insert here webhook username that you want to use: ")
    content = input("Insert here message content: ")
    for i in range(int(times)):
        if i > 4:
            sleep(1.8)
        t = threading.Thread(target=sender, args=(webhook_id, webhook_token, username, content))
        t.start()
        
send()