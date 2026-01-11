create database MT;

create table manning_table (
id SERIAL primary key,
position varchar,
name varchar,
sex varchar,
salary int,
perc_qua_bonus int,
perc_annnual_bonus int,
annual_salary int,
monthly_aver_salary int,
branch varchar
);
insert into manning_table (id,position,name,sex,salary,perc_qua_bonus,perc_annnual_bonus,annual_salary,monthly_aver_salary,branch)
values
(1,'Директор департмента','Лебедева Ольга Алексеевна','Ж',500000,0,60,9600000,800000,'Корпоративный центр'),
(2,'Директор департмента','Онежкин Сергей Владимирович','М',300000,0,50,5400000,450000,'Дальний Восток'),
(3,'Директор департмента','Васильева Наталья Петровна','Ж',280000,0,50,5040000,420000,'Юг'),
(4,'Менеджер проектов','Ли Андрей Вадимович','М',270000,30,20,4617000,384750,'Корпоративный центр'),
(5,'Менеджер проектов','Петрова Алеся Михайловна','Ж',180000,30,20,3078000,256500,'Дальний Восток'),
(6,'Менеджер проектов','Неркина Мария Ивановна','Ж',150000,30,20,2565000,213750,'Юг'),
(7,'Главный специалист','Сивцева Наталья Петровна','Ж',160000,25,20,2664000,222000,'Корпоративный центр'),
(8,'Главный специалист','Хурма Виктория Романовна','Ж',140000,25,20,2331000,194250,'Дальний Восток'),
(9,'Главный специалист','Иванова Алина Владимировна','Ж',120000,25,20,1998000,166500,'Юг');

select* from manning_table mt;
select position,name,sex,salary,perc_qua_bonus,perc_annnual_bonus,annual_salary,monthly_aver_salary,branch from manning_table mt;







