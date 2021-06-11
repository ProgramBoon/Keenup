import requests


def send_telegram(text: str):
    token = "1824921429:AAGqNoOQJGjRVjM0liY_oB5ERKqJsd6NBig"
    url = "https://api.telegram.org/bot"
    channel_id = "-1001419152223"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram("hello world!")