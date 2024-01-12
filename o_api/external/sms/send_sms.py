import json
import message
# NCSYAABLAXP6OSTS
# NEZHPYCLHNTKLQSVVBEZTD6H7XFKKZET

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01085146207',
                'from': '01029779548',
                'text': '멍충이!'
            },
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
