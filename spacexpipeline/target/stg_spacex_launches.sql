

  create view "dev"."public"."stg_spacex_launches__dbt_tmp" as (
    

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
  ) ;
