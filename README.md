# line-bot-translator
Bot Line Translator

Bot Line deangan default menerjemahkan bahasa Inggris ke bahasa Indonesia, dengan command depan /trans. Bahasa yang digunakan adalah python, dengan API googletrans.

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

## Penggunaan dalam Line

Lakukan chat yang bot dapat terlibat, lalu gunakan "/trans" di awal pesan yang akan anda terjemahkan, dengan default bahasa Inggris ke bahasa Indonesia. Contoh:

```
/trans Hello World!
```
Maka bot akan membalas dengan pesan "Halo Dunia!"

Apabila ingin mennganti bahasa sumber atau yang dituju, dapat menggunakan command "sc={lang}," untuk sumber dan "to={lang}," untuk tujuan. Contoh:


```
/trans sc=ru, to=en, Привет мир!
```
Maka bot akan membalas dengan pesan "Hello World!"

Bahasa yang tersedia dapat di lihat pada file lang.txt

Best Regards, 

Admin.
