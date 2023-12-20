import sys
import requests
import json


def main(argv):
    key = argv[0]
    b = argv[1]
    # payload={'token':key}
    url=f'https://challenge-server.code-check.io/api/kidnapper/start?token={key}'

    r=requests.get(url)
    # r=requests.get(url, params=payload)
    dist=eval(r.text)

    while True:
        url=f'https://challenge-server.code-check.io/api/kidnapper/deliver?token={key}&to={dist[list(dist)[0]]}'
        if list(dist)[0]=='put_the_bag':
            return dist[list(dist)[0]]
        r=requests.get(url)
        dist=eval(r.text)

if __name__ == '__main__':
    main(sys.argv[1:])
