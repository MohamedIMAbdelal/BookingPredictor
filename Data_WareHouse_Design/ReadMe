# Hotel Booking Data Warehouse Schema

This repository contains the data warehouse schema design for a hotel booking system. The schema follows a **star schema** model, with fact tables and dimension tables that support efficient queries for booking, property operations, and revenue analysis.

## Schema Overview

### Fact Tables

1. **fact_booking**  
   This table contains detailed records of hotel bookings.
   
   - **Columns**:
     - `booking_id`: Unique identifier for each booking.
     - `property_id`: Links to the hotel (property) where the booking was made.
     - `booking_date_id`: Links to the date the booking was created (in `dim_date`).
     - `check_in_date_id`: Links to the check-in date (in `dim_date`).
     - `checkout_date_id`: Links to the checkout date (in `dim_date`).
     - `booking_date`: The actual booking date.
     - `check_in_date`: The actual check-in date.
     - `checkout_date`: The actual checkout date.
     - `no_guests`: Number of guests in the booking.
     - `room_category`: The type of room booked.
     - `booking_platform`: The platform used for the booking (e.g., website, app).
     - `ratings_given`: Customer ratings for the booking.
     - `booking_status`: The status of the booking (e.g., confirmed, canceled).
     - `revenue_generated`: Total revenue generated from the booking.
     - `revenue_realized`: Revenue actually realized after discounts, cancellations, etc.
   
2. **fact_properties_operations**  
   This table tracks operational details related to the properties (hotels).

   - **Columns**:
     - `property_id`: Links to the hotel (property) where operations are tracked.
     - `check_in_date_id`: Links to the check-in date (in `dim_date`).
     - `room_category`: The room category for operational tracking.
     - `successful_booking`: Indicator of whether the booking was successful.

### Dimension Tables

1. **dim_date**  
   Provides time-related information, allowing for time-series analysis of bookings and operations.

   - **Columns**:
     - `date_id`: Unique identifier for each date.
     - `yy_mm_dd`: The date in year-month-day format.
     - `week_num`: The week number of the year.
     - `day_type`: The type of day (e.g., weekend, weekday).

2. **dim_rooms**  
   Details about the rooms and their classifications.

   - **Columns**:
     - `room_id`: Unique identifier for each room.
     - `room_class`: The classification of the room (e.g., standard, deluxe, suite).

3. **dim_hotel**  
   Contains metadata about the hotels (properties) where bookings and operations are tracked.

   - **Columns**:
     - `property_id`: Unique identifier for each hotel.
     - `property_name`: The name of the hotel.
     - `category`: The category or classification of the hotel (e.g., 3-star, 5-star).
     - `city`: The city where the hotel is located.

## Relationships

- **fact_booking** is linked to:
  - `dim_date` via `booking_date_id`, `check_in_date_id`, and `checkout_date_id`.
  - `dim_hotel` via `property_id`.
  - `dim_rooms` via `room_category`.

- **fact_properties_operations** is linked to:
  - `dim_date` via `check_in_date_id`.
  - `dim_hotel` via `property_id`.
  - `dim_rooms` via `room_category`.

## Purpose

This data warehouse schema is designed to support various types of analysis in the hotel industry, including:

- Tracking booking patterns over time.
- Analyzing hotel property operations and performance.
- Evaluating room occupancy and revenue generation.
- Monitoring booking platforms and customer ratings.

By using a star schema, this model enables efficient querying and reporting for business intelligence purposes.
