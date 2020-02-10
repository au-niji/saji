# saji
## 概要
このアプリは、テキストに記述された複数のURLからHTMLを取得し、CSV形式で保存することができます。
`$ git clone https://github.com/au-niji/saji`して、SeleniumとPython、Headless Chrome環境を整えることで利用することができ、CUI環境だけで実行することができます。

## 準備
- Selenium
- Chrome Canary
- Chrome driver

```
$ pip install selenium
$ pip install chromedriver-binary
```

## 使い方
### URLを記述するurl.csvを作る
`$ echo 'http://example.com/' >> url.csv`

### コードを実行する
`$ python search.py`

正常に実行できた場合、下記のようになります。

```bash
$ python search.py 
Open: https://www.example.com/
Open: https://www.example1.co.jp/
```

そして、`CSV/page_info.csv`に、取得内容が記述されます。
