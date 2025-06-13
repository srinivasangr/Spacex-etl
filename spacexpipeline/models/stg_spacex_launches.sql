{{ config(materialized='view') }}

with source_data as (
    select *
    from dev.public.spacex_launches_local
)

select
    id,
    name,
    date_utc,
    rocket,
    success,
    flight_number,
    details
from source_data