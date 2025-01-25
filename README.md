## 仮想環境
### 作成
```
python3 -m venv env
```
### 仮想環境に入る
```
source env/bin/activate
```
### ライブラリのインストール
```
pip install -r requirements.txt
```
### 抜ける
```
deactivate
```
## Atcode CLI
### 
```
acc config default-task-choice all
```
### テストケース取得
```
acc new abc???
```
### テストケース実行
e. g ) a 問題を提出する場合
```
teisyutu a/main.py
```
teisyutu は[zshrc](https://github.com/seesaw-monster/zsh)にて定義
