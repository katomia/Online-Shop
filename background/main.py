import sqlite3

from flask import Flask, g
from flask.globals import request

from flask_cors import CORS
import json
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            'test.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # 可以用keys() 但每行不再转换成元祖，必须主动遍历
        g.db.row_factory = sqlite3.Row

    return g.db

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/',methods=['GET', 'POST'])
def hello():
    return 'hello'

@app.route('/signup',methods=['GET', 'POST'])
def signup():
    db=get_db()
    db.execute('''
    insert into client(name,pass)
    values(?,?)
    ''',(request.json['name'],request.json['pass']))
    db.commit()
    app.logger.info('request data')
    app.logger.info(request.json['name'])
    return {"state":"ok"}

@app.route('/login',methods=['GET', 'POST'])
def login():
    db=get_db()
    c=db.execute('''
    select * from client
    where name=? and pass=?
    ''',(request.json['name'],request.json['pass']))
    dic={}
    if(row:=c.fetchone()):   
        return {"state":"true"}
    else:
        return {"state":"false"}


@app.route('/getGoods')
def getGoods():
    db=get_db()
    c=db.execute('''
    select *
    from goods
    ''')
    arr=[]
    while(row:=c.fetchone()):
        keys=row.keys()
        dic={key : value for key,value in zip(keys,row)}
        arr.append(dic)
        
    return {"goods":arr}

@app.route('/placeOrder',methods=['GET', 'POST'])
def placeOrder():
    db=get_db()
    count=request.json["count"]
    amont=request.json["amount"]
    c_name=request.json["c_name"]
    trading=request.json["trading"]
    db.execute('''
    insert into orders('count','amount','c_id')
    values(?,?,(
        select id from client where name=?
    ))
    ''',(count,amont,c_name))
    l=[(t['name'],c_name,t['number']) for t in trading]
    db.executemany('''
    insert into trading('g_id','o_id','number')
    values(
        (select goods.id from goods where goods.name=?),
        (select orders.id from orders inner join client on client.id=orders.c_id where client.name=? order by time desc limit 1),
        ?)
    ''',l)
    db.commit()
    return {'state':'ok'}

@app.route('/getOrders',methods=['GET', 'POST'])
def getOrders():
    db=get_db()
    c=db.execute('''
    select id,time,count,amount,state
    from orders
    where c_id=(
        select id from client where name=?
    )
    ''',(request.json['c_name'],))
    arr=[]
    while(row:=c.fetchone()):
        keys=row.keys()
        dic={key : value for key,value in zip(keys,row)}
        arr.append(dic)
        
    return {"orders":arr}

@app.route('/pay',methods=['GET', 'POST'])
def pay():
    db=get_db()
    db.execute('''
    insert into payment(o_id,amount)
    values(?,?)
    ''',(request.json['o_id'],request.json['amount']))
    db.execute('''
    update orders
    set state = 1
    where id=?
    ''',(request.json['o_id'],))
    db.commit()
    return {'state':'ok'}

@app.route('/getPayment',methods=['GET', 'POST'])
def getPayment():
    db=get_db()
    c=db.execute('''
    select id,time,o_id,amount,state
    from payment
    where o_id in (
        select orders.id 
        from orders inner join client on orders.c_id=client.id 
        where client.name=?
    )
    ''',(request.json['c_name'],))
    arr=[]
    while(row:=c.fetchone()):
        keys=row.keys()
        dic={key : value for key,value in zip(keys,row)}
        arr.append(dic)
        
    return {"payment":arr}

@app.route('/getUserInfo',methods=['GET', 'POST'])
def getUserInfo():
    db=get_db()
    c=db.execute('''
    select id,name,pass
    from client
    where name=?
    ''',(request.json['c_name'],))

    if(row:=c.fetchone()):
        keys=row.keys()
        dic={key : value for key,value in zip(keys,row)}
        
    return {"userInfo":dic}
 # close_connection()
@app.teardown_appcontext 
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
    app.run(debug=True)