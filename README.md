## 練習

これを試してみたものです。

https://a3rt.recruit-tech.co.jp/product/proofreadingAPI/

## 実行

- ターミナル上で実行
- 第1引数にチェックしたい文を入力
- 第2引数にチェック感度を以下指定（未指定の場合は`medium`となる）
  - `low`
  - `medium`
  - `high`

```
python .\run.py 'システムの企画から開発・運用まで幅拾く関われまs' 'high'
```

### 必要なもの

- APIキー
  - 上リンクから取得
  - 同階層のディレクトリに`api_key.py`とファイル名を指定し、以下のように保存

```python
# coding: utf-8

API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
```

- pip
  - `requests`を`pip install`する

### 実行イメージ

```powershell
(env) PS C:\work> python .\run.py 'システムの企画から開発・運用まで幅拾く関われまs' 'high'{
'alerts': [{'pos': 16,
             'score': 0.26520141282643983,
             'suggestions': ['を', 'が', 'で'],
             'word': '幅'},
            {'pos': 17,
             'score': 1.0,
             'suggestions': ['広', '深', '全'],
             'word': '拾'},
            {'pos': 22,
             'score': 0.31887853914691555,
             'suggestions': ['る', '、', 'た'],
             'word': 'ま'},
            {'pos': 23,
             'score': 0.999998504773976,
             'suggestions': ['で', 'す', 'し'],
             'word': 's'}],
 'checkedSentence': 'システムの企画から開発・運用まで <<幅>>  <<拾>> く関われ <<ま>>  <<s>> ',
 'inputSentence': 'システムの企画から開発・運用まで幅拾く関われまs', 'message': 'pointed out',
 'normalizedSentence': 'システムの企画から開発・運用まで幅拾く関われまs',
 'resultID': '3eea7f5424b3',
 'status': 1}
```
