# line-bot-translator
Bot Line Translator

Bot Line deangan default menerjemahkan Bahasa Inggris ke bahasa Indonesia, dengan command depan /trans. Bahasa yang digunakan adalah python, dengan API googletrans.

## Cara Menggunakan

Ganti bagian LINE_CHANNEL_SECRET & LINE_CHANNEL_ACCESS_TOKEN dengan Line Channel Secret dan Access Token yang Bot kalian miliki dari https://developers.line.me/en/

```
$ export LINE_CHANNEL_SECRET=YOUR_LINE_CHANNEL_SECRET
$ export LINE_CHANNEL_ACCESS_TOKEN=YOUR_LINE_CHANNEL_ACCESS_TOKEN

$ pip install -r requirements.txt
```
Deploy pada website atau www.heroku.com

lalu masukkan website di bagian webhook pada line developers bot anda, lalu cek.

Semoga berhasil.
