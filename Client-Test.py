import requests

def send_post_request(data):
    r = requests.post('http://127.0.0.1:8000',data)

    print(r.text)

if __name__ == '__main__':
    send_post_request('Yo!')