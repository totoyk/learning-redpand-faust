# 1. RedpandaをDockerで起動
# 2. rpkコマンドを使用してTopicを作成
# 3. rpkコマンドを使用してTopicにメッセージを送信
# 4. Faustを使用してメッセージを受信
# 5. メッセージをコンソールに出力

import faust

# Faustアプリケーションの設定
app = faust.App(
    'redpanda-faust-app',  # アプリケーション名
    broker='kafka://localhost:9092',  # RedpandaのブローカーURL
)

# トピックの定義
topic = app.topic('example-topic', value_type=str)

# メッセージ処理用のエージェント


@app.agent(topic)
async def process(messages):
    async for message in messages:
        print(f'Received message: {message}')  # メッセージをコンソールに出力
