USE WAREHOUSE ML_WH;
USE DATABASE AI_ML_PROJECT;
USE SCHEMA LOGISTICS;

CREATE OR REPLACE TABLE SHIPMENT_DATA (
    shipment_id INTEGER,
    customer_id STRING,
    origin_city STRING,
    destination_city STRING,
    carrier STRING,
    shipment_mode STRING,
    distance_km FLOAT,
    package_weight FLOAT,
    weather_condition STRING,
    traffic_level STRING,
    shipment_status STRING,
    delay_hours FLOAT,
    shipment_date TIMESTAMP_NTZ
);