create table goods(
	id integer primary key auto_increment,
	name char(20) not null,
	type char(20) default '未分类',
	price real not null,
	discount real default 1.0,
	picture char(20) default 'blank.png',
	description varchar(100) default '还没有描述哦'
);

create table client(
    id integer primary key auto_increment,
    name char(20) not null UNIQUE,
    pass char(20) not null
);

create table orders(
    id integer primary key auto_increment,
    time datetime default (datetime('now', 'localtime')),
    count int,
    amount real,
    c_id int,
    -- 0 未付款 1 已付款 2 无效
    state int check(state=0 or state=1 or state=2) default(0),
    constraint fk_orders_cid foreign key(c_id) references client(id)
);

create table payment(
    id integer primary key auto_increment,
    time datetime default (datetime('now', 'localtime')),
    o_id int,
    amount real,
    -- 0 未到账 1 已到账 2 无效
    state int check(state=0 or state=1 or state=2) default(0),
    constraint fk_payment_oid foreign key(o_id) references orders(id)
);

create table trading(
    id integer primary key auto_increment,
    g_id int,
    number int,
    o_id int,
    constraint fk_trading_gid foreign key(g_id) references goods(id),
    constraint fk_trading_oid foreign key(o_id) references orders(id)
);

create table merchant(
    id integer primary key auto_increment,
    name char(20) not null UNIQUE,
    pass char(20) not null
);