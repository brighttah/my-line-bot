from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, TextSendMessage
import os

app = Flask(__name__)

# --- แก้ไขตรงนี้ให้ถูกต้อง ---
# ใช้ชื่อ Key ให้ตรงกับที่ตั้งใน Render Environment Variables
CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')

# ตรวจสอบว่าดึงค่ามาได้จริงไหม (ถ้าไม่ได้จะ Error ตั้งแต่เริ่ม)
if CHANNEL_ACCESS_TOKEN is None or CHANNEL_SECRET is None:
    print("CRITICAL ERROR: Tokens not found in environment variables.")

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# โค้ด Flex Message (สินค้า)
flex_message_content = {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ Chat GPT Plus & Pro" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "Chat GPT Plus & Pro", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ Chat GPT", "text": "สนใจ Chat GPT Plus & Pro" } }
        ],
        "flex": 0
      }
    }
  ]
}

@app.route("/", methods=['GET'])
def hello():
    return "Hello! Bot is running.", 200

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_msg = event.message.text.lower()
    if "สินค้า" in user_msg or "ราคา" in user_msg or "สนใจ" in user_msg or "menu" in user_msg:
        flex_payload = FlexSendMessage(
            alt_text='เลือกสินค้า',
            contents=flex_message_content
        )
        line_bot_api.reply_message(event.reply_token, flex_payload)
    else:
        # ตอบกลับข้อความทั่วไป
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="พิมพ์คำว่า 'สินค้า' เพื่อดูเมนูครับ")
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
