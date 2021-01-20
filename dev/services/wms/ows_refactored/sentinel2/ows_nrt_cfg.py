
bands_sentinel2_ard_nbar = {
    "nbar_coastal_aerosol": [
        "nbar_coastal_aerosol",
        "coastal_aerosol",
        "nbart_coastal_aerosol",
        "nbart_narrow_blue",
        "nbar_narrow_blue" "narrow_blue",
    ],
    "nbar_blue": ["nbar_blue", "blue", "nbart_blue"],
    "nbar_green": ["nbar_green", "green", "nbart_green"],
    "nbar_red": ["nbar_red", "red", "nbart_red"],
    "nbar_red_edge_1": ["nbar_red_edge_1", "red_edge_1", "nbart_red_edge_1"],
    "nbar_red_edge_2": ["nbar_red_edge_2", "red_edge_2", "nbart_red_edge_2"],
    "nbar_red_edge_3": ["nbar_red_edge_3", "red_edge_3", "nbart_red_edge_3"],
    "nbar_nir_1": ["nbar_nir_1", "nir", "nir_1", "nbart_nir_1"],
    "nbar_nir_2": ["nbar_nir_2", "nir2", "nbart_nir_2"],
    "nbar_swir_2": ["nbar_swir_2", "swir_2", "nbart_swir_2"],
    "nbar_swir_3": ["nbar_swir_3", "swir_3", "nbart_swir_3"],
}

bands_sentinel2 = {
    "nbar_coastal_aerosol": ["nbar_coastal_aerosol", "nbar_narrow_blue"],
    "nbar_blue": ["nbar_blue"],
    "nbar_green": ["nbar_green"],
    "nbar_red": ["nbar_red"],
    "nbar_red_edge_1": ["nbar_red_edge_1"],
    "nbar_red_edge_2": ["nbar_red_edge_2"],
    "nbar_red_edge_3": ["nbar_red_edge_3"],
    "nbar_nir_1": ["nbar_nir_1", "nbar_near_infrared_1"],
    "nbar_nir_2": ["nbar_nir_2", "nbar_near_infrared_2"],
    "nbar_swir_2": ["nbar_swir_2", "nbar_shortwave_infrared_2"],
    "nbar_swir_3": ["nbar_swir_3", "nbar_shortwave_infrared_3"],
    "nbart_coastal_aerosol": [
        "nbart_coastal_aerosol",
        "coastal_aerosol",
        "nbart_narrow_blue",
        "narrow_blue",
    ],
    "nbart_blue": ["nbart_blue", "blue"],
    "nbart_green": ["nbart_green", "green"],
    "nbart_red": ["nbart_red", "red"],
    "nbart_red_edge_1": ["nbart_red_edge_1", "red_edge_1"],
    "nbart_red_edge_2": ["nbart_red_edge_2", "red_edge_2"],
    "nbart_red_edge_3": ["nbart_red_edge_3", "red_edge_3"],
    "nbart_nir_1": ["nbart_nir_1", "nir", "nir_1", "nbart_near_infrared_1"],
    "nbart_nir_2": ["nbart_nir_2", "nir_2", "nbart_near_infrared_2"],
    "nbart_swir_2": ["nbart_swir_2", "swir_2", "nbart_shortwave_infrared_2"],
    "nbart_swir_3": ["nbart_swir_3", "swir_3", "nbart_shortwave_infrared_3"],
}
layers =                {
                            "name": "s2_nrt_granule_nbar_t",
                            "title": "Near Real-Time Surface Reflectance (Sentinel 2 (A and B combined))",
                            "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au
""",
                            "multi_product": True,
                            "product_names": ["s2a_nrt_granule", "s2b_nrt_granule"],
                            "bands": bands_sentinel2,
                            "resource_limits": reslim_s2,
                            "dynamic": True,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "native_resolution": [10.0, 10.0],
                                "default_bands": [
                                    "nbart_red",
                                    "nbart_green",
                                    "nbart_blue",
                                ],
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_s2_simple_rgb,
                                    style_s2_irg,
                                    style_s2_ndvi,
                                    style_s2_ndwi,
                                    style_s2_mndwi,
                                    style_s2_ndci,
                                    style_s2_pure_aerosol,
                                    style_s2_pure_blue,
                                    style_s2_pure_green,
                                    style_s2_pure_red,
                                    style_s2_pure_redge_1,
                                    style_s2_pure_redge_2,
                                    style_s2_pure_redge_3,
                                    style_s2_pure_nir,
                                    style_s2_pure_narrow_nir,
                                    style_s2_pure_swir1,
                                    style_s2_pure_swir2,
                                    style_s2_nbr,
                                ],
                            },
                        },
                        {
                            "name": "s2b_nrt_granule_nbar_t",
                            "title": "Near Real-Time Surface Reflectance (Sentinel 2B)",
                            "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au
""",
                            "product_name": "s2b_nrt_granule",
                            "bands": bands_sentinel2,
                            "resource_limits": reslim_s2,
                            "dynamic": True,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "native_resolution": [10.0, 10.0],
                                "default_bands": [
                                    "nbart_red",
                                    "nbart_green",
                                    "nbart_blue",
                                ],
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_s2_simple_rgb,
                                    style_s2_irg,
                                    style_s2_ndvi,
                                    style_s2_ndwi,
                                    style_s2_mndwi,
                                    style_s2_ndci,
                                    style_s2_pure_aerosol,
                                    style_s2_pure_blue,
                                    style_s2_pure_green,
                                    style_s2_pure_red,
                                    style_s2_pure_redge_1,
                                    style_s2_pure_redge_2,
                                    style_s2_pure_redge_3,
                                    style_s2_pure_nir,
                                    style_s2_pure_narrow_nir,
                                    style_s2_pure_swir1,
                                    style_s2_pure_swir2,
                                ],
                            },
                        },
                        {
                            "name": "s2a_nrt_granule_nbar_t",
                            "title": "Near Real-Time Surface Reflectance (Sentinel 2A)",
                            "abstract": """
This is a 90-day rolling archive of daily Sentinel-2 Near Real Time data. The Near Real-Time capability provides analysis-ready data that is processed on receipt using the best-available ancillary information at the time to provide atmospheric corrections.

For more information see http://pid.geoscience.gov.au/dataset/ga/122229

The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For service status information, see https://status.dea.ga.gov.au
""",
                            "product_name": "s2a_nrt_granule",
                            "bands": bands_sentinel2,
                            "resource_limits": reslim_s2,
                            "dynamic": True,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:3577",
                                "native_resolution": [10.0, 10.0],
                                "default_bands": [
                                    "nbart_red",
                                    "nbart_green",
                                    "nbart_blue",
                                ],
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_s2_simple_rgb,
                                    style_s2_irg,
                                    style_s2_ndvi,
                                    style_s2_ndwi,
                                    style_s2_mndwi,
                                    style_s2_ndci,
                                    style_s2_pure_aerosol,
                                    style_s2_pure_blue,
                                    style_s2_pure_green,
                                    style_s2_pure_red,
                                    style_s2_pure_redge_1,
                                    style_s2_pure_redge_2,
                                    style_s2_pure_redge_3,
                                    style_s2_pure_nir,
                                    style_s2_pure_narrow_nir,
                                    style_s2_pure_swir1,
                                    style_s2_pure_swir2,
                                    style_s2_nbr,
                                ],
                            },
                        }