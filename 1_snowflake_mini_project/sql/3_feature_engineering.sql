USE WAREHOUSE ML_WH;
USE DATABASE AI_ML_PROJECT;
USE SCHEMA LOGISTICS;

CREATE OR REPLACE VIEW SHIPMENT_RISK_VIEW AS
SELECT
    shipment_id,
    customer_id,
    origin_city,
    destination_city,
    carrier,
    shipment_mode,
    distance_km,
    package_weight,
    weather_condition,
    traffic_level,
    shipment_status,
    delay_hours,
    shipment_date,

    CASE
        WHEN delay_hours > 48 THEN 'HIGH'
        WHEN delay_hours > 24 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS delay_risk,

    CASE
        WHEN weather_condition IN ('Storm', 'Fog')
             OR traffic_level = 'High'
             OR delay_hours > 36
        THEN 1
        ELSE 0
    END AS anomaly_flag

FROM SHIPMENT_DATA;