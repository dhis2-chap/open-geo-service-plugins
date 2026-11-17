"""WorldPop Global2 population by age and sex, from the plugin in Open Geo Service core.

Open Geo Service keeps the plugin but no longer lists the dataset, since its ingest is slow: WorldPop publishes
about 40 GeoTIFFs per country-year, one per sex and age band, and each is downloaded and stacked.
The template here offers it to the instances that want it anyway.
"""

from open_geo_service.plugins.rasters.worldpop import WorldPopAgeSexYearlyPlugin

__all__ = ["WorldPopAgeSexYearlyPlugin"]
