import os
import openai
import requests

# OpenAI APIとX（Twitter）APIのキーを環境変数から取得
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
TWITTER_BEARER_TOKEN = os.environ['TWITTER_BEARER_TOKEN']

# OpenAIのAPIを使用して、文章を生成する関数
def generate_tweet_content():
    openai.api_key=OPENAI_API_KEY
    # ChatGPTを使ってツイートを生成
    response = openai.chat.completions.create(
    model="text-embedding-3-small", # model = "deployment_name"
    messages=[
        {"role": "user", "content": "あなたは短いツイートを書く役に立つアシスタントです。最新の技術トレンドについて、130文字以内の興味深いツイートを作成してください。"}
    ],
    max_tokens=50  # トークン数を制限して文字数を調整
)
    
    # 応答から生成されたツイートを取得
    tweet_content = response['choices'][0]['message']['content'].strip()
    
    # 130文字以内に切り詰める
    if len(tweet_content) > 130:
        tweet_content = tweet_content[:130]
    
    return tweet_content

# X（Twitter）にポストする関数
def post_to_twitter(tweet_content):
    url = "https://api.twitter.com/2/tweets"
    headers = {
        "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": tweet_content
    }
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        return "Successfully posted to Twitter!"
    else:
        return f"Failed to post: {response.status_code}, {response.text}"

def lambda_handler(event, context):
    # 1. ChatGPTでツイートの内容を生成
    tweet_content = generate_tweet_content()
    
    # 2. 生成したツイートをX（Twitter）にポスト
    result = post_to_twitter(tweet_content)
    
    return {
        'statusCode': 200,
        'body': result
    }
