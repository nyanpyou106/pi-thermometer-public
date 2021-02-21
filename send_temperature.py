from bottle import run, route, response, view, static_file
import time
import os
import webbrowser
import scraping_outside_temperature
import sht31
import json

# ルーティングのパスはラズパイ上の絶対パスに変更する
@route("/")
@view("thermometer.html")
def index():
    return

@route("/img/<file_path:path>")
def server_static(file_path):
    return static_file(file_path, root="./img")

@route("/static/<file_path:path>")
def css(file_path):
    return static_file(file_path, root="./static")

@route("/sse")
def sse():
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Content_Type'] = "text/event-stream"

    temperature_json = sht31.get_temperature_data()
    outside_temperature = scraping_outside_temperature.scraping_currentlocation_outside_temp()
    temperature_json["outside"] = outside_temperature
    temperature_json_str = json.dumps(temperature_json)

    # 初回も10秒待たせると読み込み途中の動画も10秒止まってしまうので、初回は待ち時間なしにする
    # FIXME 正しい処理をしているとは思えない　うまいやり方を知りたい
    first = True
    if first:
        first = False
    else:
        time.sleep(10)
    return "data: {}\n\n".format(temperature_json_str)

myport = os.getenv("PORT", 8080)
myaddr = os.getenv("IP", "localhost")
run(host=myaddr, port=myport, quiet=True)