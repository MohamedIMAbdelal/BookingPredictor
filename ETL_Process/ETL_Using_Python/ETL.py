import pandas as pd
from sqlalchemy import create_engine , types

#connection string
server = 'ELIJAH\\SQLEXPRESS01'
database = 'DW_Hospitality_Analysis2'
connection_string = f"mssql+pyodbc://{server}/{database}?driver=SQL+Server"
engine = create_engine(connection_string)

#data Extraction
dim_rooms_path = r'C:\Users\HONESTEAGLE\Desktop\sources\dim_rooms.csv'
dim_rooms_data = pd.read_csv(dim_rooms_path, delimiter=';')

dim_date_path = r'C:\Users\HONESTEAGLE\Desktop\sources\sources2\dim_date.xlsx'
dim_date_data = pd.read_excel(dim_date_path)

dim_hotel_path = r'C:\Users\HONESTEAGLE\Desktop\sources\dim_hotels.csv'
dim_hotel_data = pd.read_csv(dim_hotel_path, delimiter=';')

fact_booking_path = r'C:\Users\HONESTEAGLE\Desktop\sources\sources2\fact_booking.xlsx'
fact_booking_data = pd.read_excel(fact_booking_path)

fact_properties_operations_path = r'C:\Users\HONESTEAGLE\Desktop\sources\sources2\fact_aggerated_booking.xlsx'
fact_properties_operations_data = pd.read_excel(fact_properties_operations_path)

#data Transformations
dim_date_data.rename(columns={
    'week no': 'week_num',
    'day type': 'day_type',
    'yy-mm-dd': 'yy_mm_dd'
}, inplace=True)

dim_date_data['yy_mm_dd'] = pd.to_datetime(dim_date_data['yy_mm_dd'])
dim_date_data['week_num'] = dim_date_data['week_num'].astype(int)
dim_date_data['day_type'] = dim_date_data['day_type'].astype(str)
dim_date_data['date_id'] = dim_date_data['yy_mm_dd'].dt.strftime('%Y%m%d').astype(int)

fact_booking_data['check_in_date_id']=fact_booking_data['check_in_date'].dt.strftime('%Y%m%d').astype(int)
fact_booking_data['checkout_date_id']=fact_booking_data['checkout_date'].dt.strftime('%Y%m%d').astype(int)
fact_booking_data['booking_date_id']=fact_booking_data['booking_date'].dt.strftime('%Y%m%d').astype(int)
fact_booking_data['check_in_date']=pd.to_datetime(fact_booking_data['check_in_date'])
fact_booking_data['checkout_date']=pd.to_datetime(fact_booking_data['checkout_date'])
fact_booking_data['booking_date']=pd.to_datetime(fact_booking_data['booking_date'])
fact_booking_data['booking_id']=fact_booking_data['booking_id'].astype(str)
fact_booking_data['property_id']=fact_booking_data['property_id'].astype(int)
fact_booking_data['no_guests']=fact_booking_data['no_guests'].astype(int)
fact_booking_data['room_category']=fact_booking_data['room_category'].astype(str)
fact_booking_data['booking_platform']=fact_booking_data['booking_platform'].astype(str)
fact_booking_data['ratings_given']=fact_booking_data['ratings_given']
fact_booking_data['booking_status']=fact_booking_data['booking_status'].astype(str)
fact_booking_data['revenue_generated']=fact_booking_data['revenue_generated'].astype(int)
fact_booking_data['revenue_realized']=fact_booking_data['revenue_realized'].astype(int)

fact_properties_operations_data.rename(columns={
    'successful_bookings':'successful_booking'}, inplace=True)
fact_properties_operations_data['check_in_date_id']=fact_properties_operations_data['check_in_date'].dt.strftime('%Y%m%d').astype(int)
fact_properties_operations_data['check_in_date']=pd.to_datetime(fact_properties_operations_data['check_in_date'])
fact_properties_operations_data['property_id']=fact_properties_operations_data['property_id'].astype(int)
fact_properties_operations_data['room_category']=fact_properties_operations_data['room_category'].astype(str)
fact_properties_operations_data['successful_booking']=fact_properties_operations_data['successful_booking'].astype(int)
fact_properties_operations_data['capacity']=fact_properties_operations_data['capacity'].astype(int)

#data Loading
dim_rooms_data.to_sql('dim_rooms', engine, if_exists='append', index=False)

dim_date_data.to_sql('dim_date', engine, if_exists='append', index=False, dtype={
    'yy_mm_dd': types.DateTime(),     
    'week_num': types.Integer(),           
    'day_type': types.VARCHAR(20),   
    'date_id': types.Integer()
})

dim_hotel_data.to_sql('dim_hotel', engine, if_exists='append', index=False, dtype={
    'property_id': types.Integer(),     
    'category': types.VARCHAR(25),           
    'property_name': types.VARCHAR(25),   
    'city': types.VARCHAR(25)
})

fact_booking_data.to_sql('fact_booking', engine, if_exists='append', index=False)

fact_properties_operations_data.to_sql('fact_properties_operations', engine, if_exists='append', index=False)

engine.dispose()