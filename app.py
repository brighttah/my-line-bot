from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FlexSendMessage
import os

app = Flask(__name__)

# รับค่ารหัสจาก Environment Variable
CHANNEL_ACCESS_TOKEN = os.environ.get('CHANNEL_ACCESS_TOKEN')
CHANNEL_SECRET = os.environ.get('CHANNEL_SECRET')

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

# โค้ด Flex Message (สินค้า 8 ใบ)
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
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ Gemini Pro" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "Gemini Pro", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ Gemini Pro", "text": "สนใจ Gemini Pro" } }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ Canva Pro" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "Canva Pro", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ Canva Pro", "text": "สนใจ Canva Pro" } }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ Perplexity" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "Perplexity", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ Perplexity", "text": "สนใจ Perplexity" } }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ CapCut Pro" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "CapCut Pro", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ CapCut Pro", "text": "สนใจ CapCut Pro" } }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ Midjourney" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "Midjourney", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ Midjourney", "text": "สนใจ Midjourney" } }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สนใจ Claude Pro" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "Claude Pro", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "สนใจ Claude Pro", "text": "สนใจ Claude Pro" } }
        ],
        "flex": 0
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.postimg.cc/PrwnXSSB/sw-sd-p-him.jpg",
        "size": "full",
        "aspectRatio": "1:1",
        "aspectMode": "cover",
        "action": { "type": "message", "label": "สนใจ", "text": "สอบถามเพิ่มเติม" }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          { "type": "text", "text": "บริการอื่นๆ / สอบถาม", "weight": "bold", "size": "xl", "color": "#000000", "wrap": True }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "spacing": "sm",
        "contents": [
          { "type": "button", "style": "primary", "height": "md", "color": "#42659C", "action": { "type": "message", "label": "ติดต่อแอดมิน", "text": "ติดต่อแอดมิน" } }
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

# แก้ไขจุดผิด: เปลี่ยนจาก @app.event เป็น @handler.add
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_msg = event.message.text.lower()
    if "สินค้า" in user_msg or "ราคา" in user_msg or "สนใจ" in user_msg or "menu" in user_msg:
        flex_payload = FlexSendMessage(
            alt_text='เลือกสินค้าโปรแกรมพรีเมียม',
            contents=flex_message_content
        )
        line_bot_api.reply_message(event.reply_token, flex_payload)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
