# Instagram-AUTO-LIKE for Windows
インスタグラムの自動いいねアルゴリズムです。簡単にPythonのルールを理解している人向けです。ご自由にお使いください。Macでは試していません。

時々Metaが仕様を変更すると使えなくなることがありますが、気が向けば対応します。中身は簡単ですので変更してみてください。

# 仕様方法
実行前にPythonを導入しておいてください。

1. setup.batを実行またはコマンドプロンプトで以下を実行
```
pip install --upgrade pip && pip install -r requirements.txt --user
```
2. config.example.pyをコピーしてconfig.pyを作成。アカウント名とパスワードを変更。
2. insta-auto-likeディレクトリに移動し、以下を実行。アカウントを選択、ハッシュタグの指定、スリープ処理の選択後いいねが自動で始まります。
```cmd
python like.py
```
もしくは
```cmd
python3 like.py
```

<a href="http://instagram.com/hoboki.jp" target="_blank">【ほぼきのインスタグラム】</a>

# 実行環境
Python 3.9.4