import errno
import os
import sys
from googletrans import Translator

from flask import Flask, request, abort

from linebot import (
	LineBotApi, WebhookHandler
)
from linebot.exceptions import (
	InvalidSignatureError
)
from linebot.models import (
	MessageEvent, TextMessage, TextSendMessage, SourceGroup, SourceRoom,
)

translator = Translator()
wiki_settings = {}


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
	print('Specify LINE_CHANNEL_SECRET as environment variable.')
	sys.exit(1)
if channel_access_token is None:
	print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
	sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookParser(channel_secret)

# function for create tmp dir for download content
def make_static_tmp_dir():
	try:
		os.makedirs(static_tmp_path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(static_tmp_path):
			pass
		else:
			raise

@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']

	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)

	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)

	return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):

	text=event.message.text
	
	if isinstance(event.source, SourceGroup):
		subject = line_bot_api.get_group_member_profile(event.source.group_id,
														event.source.user_id)
		set_id = event.source.group_id
	elif isinstance(event.source, SourceRoom):
		subject = line_bot_api.get_room_member_profile(event.source.room_id,
                                                   event.source.user_id)
		set_id = event.source.room_id
	else:
		subject = line_bot_api.get_profile(event.source.user_id)
		set_id = event.source.user_id
	
	def split(text):
		return text.split('/trans ', 1)[-1]

	def trans(word):
		sc = 'en'
		to = 'id'
		
		if word[0:].lower().strip().startswith('sc='):
			sc = word.split(', ', 1)[0]
			sc = sc.split('sc=', 1)[-1]
			word = word.split(', ', 1)[1]
	
		if word[0:].lower().strip().startswith('to='):
			to = word.split(', ', 1)[0]
			to = to.split('to=', 1)[-1]
			word = word.split(', ', 1)[1]
			
		if word[0:].lower().strip().startswith('sc='):
			sc = word.split(', ', 1)[0]
			sc = sc.split('sc=', 1)[-1]
			word = word.split(', ', 1)[1]
			
		return translator.translate(word, src=sc, dest=to).text

	if text[0:].lower().strip().startswith('/trans ') :
		line_bot_api.reply_message(
			event.reply_token,
			TextSendMessage(trans(split(text))))
	
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)