DROP TABLE IF EXISTS goods;
create table goods(
	id integer primary key autoincrement,
	name char(20) not null,
	type char(20) default '未分类',
	price real not null,
	discount real default 1.0,
	picture char(20) default 'blank.png',
	description varchar(100) default '还没有描述哦'
);
INSERT INTO goods(name,type,price,discount,picture) VALUES ('汉堡',"food",6,0.9,"Hamburger.png"),('八音盒',"toy",12,0.8,"MusicBox.jpg");

DROP TABLE IF EXISTS client;
create table client(
    id integer primary key autoincrement,
    name char(20) not null UNIQUE,
    pass char(20) not null
);
INSERT INTO client(name,pass) VALUES ('ding','123');


DROP TABLE IF EXISTS orders;
create table orders(
    id integer primary key autoincrement,
    time datetime default (datetime('now', 'localtime')),
    count int,
    amount real,
    c_id int,
    -- 0 未付款 1 已付款 2 无效
    state int check(state=0 or state=1 or state=2) default(0)
);
DROP TABLE IF EXISTS payment;
create table payment(
    id integer primary key autoincrement,
    time datetime default (datetime('now', 'localtime')),
    o_id int,
    amount real,
    -- 0 未到账 1 已到账 2 无效
    state int check(state=0 or state=1 or state=2) default(0)
);

DROP TABLE IF EXISTS trading;
create table trading(
    id integer primary key autoincrement,
    g_id int,
    number int,
    o_id int
);
DROP TABLE IF EXISTS merchant;
create table merchant(
    id integer primary key autoincrement,
    name char(20) not null UNIQUE,
    pass char(20) not null
)

