create table dim_date(
date_id int primary key not null,
yy_mm_dd date not null,
week_num int not null,
day_type varchar(20) null
);

create table dim_hotel(
property_id int primary key not null,
property_name varchar(25) not null,
category varchar(25) not null,
city varchar(25) null
);

create table dim_rooms(
room_id varchar(10) primary key not null,
room_class varchar(20) not null
);

create table fact_properties_operations(
property_id int FOREIGN KEY REFERENCES dim_hotel (property_id),
check_in_date_id int FOREIGN KEY REFERENCES dim_date (date_id),
check_in_date date not null,
room_category varchar(10) FOREIGN KEY REFERENCES dim_rooms (room_id),
successful_booking int not null,
capacity int not null
);

create table fact_booking(
booking_id varchar(30) primary key,
property_id int FOREIGN KEY REFERENCES dim_hotel (property_id),
booking_date_id int FOREIGN KEY REFERENCES dim_date (date_id),
check_in_date_id int FOREIGN KEY REFERENCES dim_date (date_id),
checkout_date_id int FOREIGN KEY REFERENCES dim_date (date_id),
booking_date date not null,
check_in_date date not null,
checkout_date date not null,
no_guests int not null,
room_category varchar(10) FOREIGN KEY REFERENCES dim_rooms (room_id),
booking_platform varchar(20) not null,
ratings_given decimal(2,1) null,
booking_status varchar(15) not null,
revenue_generated int not null,
revenue_realized int not null
);
