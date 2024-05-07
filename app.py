import os
from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import random
import time
# 实例化，可视为固定格式
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
# 在扩展类实例化前加载配置
db = SQLAlchemy(app)

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字
    pwd = db.Column(db.String(20))  # 密码

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))
    data = db.Column(db.Text)

class UG(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))
    game_id = db.Column(db.Integer)

# route()方法用于设定路由；类似spring路由配置
@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'

@app.route('/registor', methods=['GET'])
def registor():
    name = request.args.get('name')  # args取get方式参数
    pwd = request.args.get('pwd')  # args取get方式参数
    u = User.query.filter_by(name=name).first()
    if u is None:
        user = User(name=name, pwd=pwd)
        db.session.add(user)
        db.session.commit()
        resp = {'status': 'success',
                'data': {'status': 'success'}}
        return jsonify(resp)
    resp = {'status': 'success',
            'data': {'status': 'fail'}}
    return jsonify(resp)

@app.route('/login', methods=['GET'])
def login():
    name = request.args.get('name')  # args取get方式参数
    pwd = request.args.get('pwd')  # args取get方式参数
    u = User.query.filter_by(name=name).first()
    if u is not None:
        if u.pwd == pwd:
            resp = {'status': 'success',
                    'data': {'status': 'success'}}
            return jsonify(resp)
        else:
            resp = {'status': 'success',
                    'data': {'status': 'passwordError'}}
            return jsonify(resp)
    else:
        resp = {'status': 'success',
                'data': {'status': 'account is not exist'}}
        return jsonify(resp)

def create_map(number):
    if number == 1:
        str_a = 'y00m00000000m00b' \
                '0000000000000000'\
                '0000000000000000' \
                'm000000vv000000m' \
                '0000000000000000' \
                '0000000000000000' \
                '0000000000000000' \
                '000v000tt000v000' \
                '000v000tt000v000' \
                '0000000000000000' \
                '0000000000000000'\
                '0000000000000000' \
                'm000000vv000000m' \
                '0000000000000000' \
                '0000000000000000' \
                'r00m00000000m00g'
        building = [{"points": [3], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [48], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [12], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [63], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [192], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [207], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [228], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [237], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [55, 56], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 1},
                    {"points": [199, 200], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 2},
                    {"points": [115, 131], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 3},
                    {"points": [124, 140], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 4},
                    {"points": [119, 120, 135, 136], "belongs": [0, 0, 0, 0], "type": "town"}]
    else:
        str_a = 'y00m00000000m00b' \
                '0000000000000000'\
                '0000000000000000' \
                'm000000vv000000m' \
                '0000000000000000' \
                '0000000000000000' \
                '0000000000000000' \
                '000v000tt000v000' \
                '000v000tt000v000' \
                '0000000000000000' \
                '0000000000000000'\
                '0000000000000000' \
                'm000000vv000000m' \
                '0000000000000000' \
                '0000000000000000' \
                'r00m00000000m00g'
        building = [{"points": [3], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [48], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [12], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [63], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [192], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [207], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [228], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [237], "belongs": [0, 0, 0, 0], "type": "mine"},
                    {"points": [55, 56], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 1},
                    {"points": [199, 200], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 2},
                    {"points": [115, 131], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 3},
                    {"points": [124, 140], "belongs": [0, 0, 0, 0], "type": "vil", 'number': 4},
                    {"points": [119, 120, 135, 136], "belongs": [0, 0, 0, 0], "type": "town"}]

    return str_a, building

def init_hand(type):
    if type == 2:
        return [0,0,-1,-1]
    if type == 3:
        return [0,0,0,-1]
    if type == 4:
        return [0,0,0,0]

@app.route('/get_game', methods=['GET'])
def get_game():
    id = request.args.get('id')  # args取get方式参数
    game = Game.query.filter(Game.id == id).first()
    res = {'status': 'success',
            'data': json.loads(game.data)}
    return jsonify(res)

@app.route('/get_game_list', methods=['GET'])
def get_game_list():
    id = request.args.get('id')  # args取get方式参数
    ugs = UG.query.filter(UG.name == id).all()
    list = []
    for ug in ugs:
        list.append(ug.game_id)
    res = {'status': 'success',
            'data': {'list': list}}
    return jsonify(res)

@app.route('/push_game', methods=['POST'])
def push_game():
    datas = json.loads(request.data) # 将json字符串转为dict
    id = datas['id']
    data = datas['data']
    game = Game.query.filter(Game.id == id).first()
    if game is None:
        res = {'status': 'success',
               'data': {'status': 'game id is not exist'}}
    else:
        game.data = data
        db.session.commit()
        res = {'status': 'success',
                'data': {'status': 'success'}}
    return jsonify(res)


@app.route('/create_game', methods=['GET'])
def create_game():
    name1 = request.args.get('name1')  # args取get方式参数
    initHands = random.randint(2, 4)
    usr1 = {'deck': init_hand(6 - initHands), 'hands': init_hand(initHands), 'discard': [], 'point': 4, 'gold': 0,
            'prosperity': 0, 'color': 'r', 'order': 0, 'id': name1}
    name2 = request.args.get('name2')  # args取get方式参数
    initHands = random.randint(2, 4)
    usr2 = {'deck': init_hand(6 - initHands), 'hands': init_hand(initHands), 'discard': [], 'point': 4, 'gold': 1,
            'prosperity': 0, 'color': 'y', 'order': 1, 'id': name2}
    name3 = request.args.get('name3')  # args取get方式参数
    initHands = random.randint(2, 4)
    usr3 = {'deck': init_hand(6 - initHands), 'hands': init_hand(initHands), 'discard': [], 'point': 4, 'gold': 2,
            'prosperity': 0, 'color': 'b', 'order': 2, 'id': name3}
    name4 = request.args.get('name4')  # args取get方式参数
    initHands = random.randint(2, 4)
    usr4 = {'deck': init_hand(6 - initHands), 'hands': init_hand(initHands), 'discard': [], 'point': 4, 'gold': 3,
            'prosperity': 0, 'color': 'g', 'order': 3, 'id': name4}
    game_map = request.args.get('map')  # args取get方式参数
    name = request.args.get('name')  # args取get方式参数
    game, builds = create_map(game_map)
    resp = {
        'game': game,
        'map': int(game_map),
        'disturb': [],
        'current': 0,
        'discard':[],
        'legend': [],
        'normal': [3,4,5,4,4,4,6,3,4],
        'play':[],
        'deck':[3,4,5,4,4,4,6,3,4],
        'user':[usr1, usr2, usr3, usr4],
        'building': builds,
    }

    j = json.dumps(resp)

    t = str(int(round(time.time())))
    rn = name + '/' + t
    gameDB = Game(name=rn, data=j)
    db.session.add(gameDB)
    db.session.commit()
    gameS = Game.query.filter(Game.name == rn).first()
    ug1 = UG(name=name1, game_id=gameS.id)
    db.session.add(ug1)
    ug2 = UG(name=name2, game_id=gameS.id)
    db.session.add(ug2)
    ug3 = UG(name=name3, game_id=gameS.id)
    db.session.add(ug3)
    ug4 = UG(name=name4, game_id=gameS.id)
    db.session.add(ug4)
    db.session.commit()

    res = {'status': 'success',
            'data': resp}
    return jsonify(res)

if __name__ == '__main__':
    # app.run(host, port, debug, options)
    # 默认值：host="127.0.0.1", port=5000, debug=False
    app.run(host="0.0.0.0", port=8090, debug=False)
