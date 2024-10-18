Power BI Integration for Hotel Data Analytics
As part of our project, we used Power BI to visualize and analyze key performance indicators (KPIs) from our hotel booking data. Below are details of the Power BI interface and data warehouse schema that were implemented.

1. Power BI Dashboard Interface - Hotel Data Analytics

This dashboard offers a comprehensive view of hotel performance across various dimensions, including revenue, occupancy rates, and booking details.

Filter Options:
Users can dynamically filter data by city, room class, booking platform, room category, property name, and booking ID. This allows for granular analysis of specific data subsets.

Key Metrics:

Revenue: Displays total revenue for a selected period along with week-over-week (WoW) change percentages.
ADR (Average Daily Rate) and RevPAR (Revenue per Available Room): Highlight room revenue metrics and fluctuations over time.
Occupancy%: Shows the percentage of occupied rooms, alongside Realization% (the percentage of total capacity realized) and DURN (Duration) representing the average length of stay.
Visual indicators such as upward and downward arrows provide immediate insights into performance trends.
Visuals:

Pie Chart: Visualizes the distribution of room categories (Luxury vs. Business) as a percentage of total bookings.
Line Graph: Tracks RevPAR, ADR, and Occupancy% over time, helping identify patterns and trends over weeks.
Tabular Data:

A detailed table presents booking information by property, with metrics such as Revenue, Occupancy%, Realization%, and RevPAR. This breakdown enables a deep dive into individual property performance.
Additional Insights:

Data on cancellation rates, average ratings, and ADR broken down by Day Type (Weekday vs. Weekend) provide insights into how different factors influence hotel performance.
2. Power BI Data Warehouse Schema

The Power BI data model was built using the following tables and relationships to store and analyze hotel booking data:

Fact Tables:

Fact_BookingOperations: Contains detailed booking operations data, including booking date, check-in/check-out dates, number of guests, and stay duration.
Fact_Bookings: Aggregates bookings data, capturing key metrics such as property ID, room category, and total bookings/capacity.
Dimension Tables:

Dim_Date: Stores time-related attributes like date, Day_Type (Weekday/Weekend), and WeekNum, facilitating time-based analysis.
Dim_Rooms: Provides room-specific data, such as room_class and room_id, allowing segmentation of bookings by room type.
Dim_Hotels: Holds hotel property data, including city, category, and property_id, for filtering and grouping data by property or location.
Calculated Measures: A list of calculated measures (e.g., ADR WoW change %, Occupancy, Revenue, Cancellation%) were created to track KPIs and trends. These measures were essential for analyzing hotel performance metrics in real time and supporting data-driven decision-making.

These Power BI reports and dashboards provide detailed, interactive insights into hotel performance, helping stakeholders optimize operations, monitor revenue, and improve guest experience. Through seamless integration with our data warehouse and using calculated measures, the dashboard ensures accurate, real-time analysis of business KPIs.


