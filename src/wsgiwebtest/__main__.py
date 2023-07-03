from wsgiref.simple_server import make_server

from wsgiwebtest import Application


def main():
    app = Application()
    with make_server('', 8000, app) as httpd:
        print("Serwer nasłuchuje na porcie 8000...")
        httpd.serve_forever()

main()