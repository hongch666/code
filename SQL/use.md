# How to make a database
1.sudo mysql<br/>
2.create database if not exist [database name]<br/>
3.use [database name]<br/>
4.create database
``` SQL
create table if not exists appList(
  id int auto_increment, 
  a varchar(50) not null, 
  b varchar(5), 
  c varchar(10) not null, 
  d int not null, 
  e DATE, 
  primary key(id)
);
```
5.desc [database name]
# Make a table
1.create a database
```SQL
CREATE DATABASE mydatabase;
```
2.change database
```SQL
USE mydatabase;
```
3.create table
```SQL
CREATE TABLE mytable (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  age INT
);
```
4.insert data
```SQL
INSERT INTO mytable (id, name, age)
VALUES (1, 'John', 25);
```
5.check data
```SQL
SELECT * FROM mytable;
```
# Quit from mysql
quit
# ERROR CONNECT
1. 打开命令行小黑屏，进入MySQL的bin目录，然后输入mysql -u root -p，输入密码
2. 依次输入
```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password' PASSWORD EXPIRE NEVER; 
-- (修改加密规则 （必写）)

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'; -- (更新用户密码 )

FLUSH PRIVILEGES; 
-- 刷新权限（不输入也可以）
```