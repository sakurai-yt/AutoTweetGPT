# **AutoTweetGPT**

## 概要
**AutoTweetGPT**は、ChatGPTAIを活用して自動で興味深いツイートを生成するツールです。
最新の技術トレンドに基づいたツイートを、OpenAIのAPIを利用して自動的に作成し、X（旧Twitter）に投稿します。
このツールは、定期的な投稿やマーケティングの自動化に役立ちます。

### 特徴
- **AI生成ツイート**: ChatGPTを使って興味深いツイートを自動生成。
- **X（Twitter）との連携**: APIを使用して自動でツイートをポスト。
- **カスタマイズ可能なプロンプト**: プロンプトを自由にカスタマイズして、さまざまなジャンルのツイートを生成。

## インストール

### 環境変数を設定

環境変数にAPIキーを設定してください。

- `OPENAI_API_KEY`: OpenAIのAPIキー
- `TWITTER_BEARER_TOKEN`: X（Twitter）の認証トークン

## 環境要件

- **Python 3.9**
- **依存ライブラリ**: openai, requests, etc.

## 貢献

1. リポジトリをフォーク
2. フィーチャーブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. プッシュ (`git push origin feature/AmazingFeature`)
5. プルリクエストを作成

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご確認ください。