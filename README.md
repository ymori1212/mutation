# mutmut Mutation Testing Example

## はじめに
このリポジトリは、Python 用ミューテーションテストツール **mutmut** の使い方を紹介するサンプルプロジェクトです。

### 注意
mutmut はプロセスのフォークを多用するため、Windows 上での実行は困難です。本プロジェクトでは **Docker** を利用して Linux 環境を構築し、そこからミューテーションテストを実施します。

## テストの実行手順
### 1. Docker コンテナの起動
以下のコマンドでコンテナを起動してください：
```bash
docker compose up -d --build
docker compose exec mutmut bash
```

### 2. ミューテーションテストの実行
コンテナ内で以下を実行します：
```bash
mutmut run
```

### 3. ミューテーション結果の確認
結果をブラウザで確認するには：
```bash
mutmut browse
```


## Qiita記事
詳細な解説については、以下の Qiita 記事を参照してください

- [ロバストなテストを実現するミューテーションテストの魅力](https://qiita.com/ymori1212/items/4077440b6eac882d0f7a)
- [ミューテーションテストにおける小さな変更（ミュータント）の種類](https://qiita.com/ymori1212/items/f806fe7e1bf76dcb89e1)
- [Pythonでミューテーションテストを行うmutmutを動かしてみた](https://qiita.com/ymori1212/items/8c85f44c324a69b7ac0f)

