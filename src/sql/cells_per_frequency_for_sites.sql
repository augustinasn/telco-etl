SELECT
    s.site_id,
    COUNT(CASE WHEN cd.type = 'gsm' AND cd.frequency_band = 900 THEN 1 END) AS frequency_band_G900_by_site,
    COUNT(CASE WHEN cd.type = 'gsm' AND cd.frequency_band = 1800 THEN 1 END) AS frequency_band_G1800_by_site,
    COUNT(CASE WHEN cd.type = 'umts' AND cd.frequency_band = 2100 THEN 1 END) AS frequency_band_U2100_by_site,
    COUNT(CASE WHEN cd.type = 'lte' AND cd.frequency_band = 700 THEN 1 END) AS frequency_band_L700_by_site,
    COUNT(CASE WHEN cd.type = 'lte' AND cd.frequency_band = 800 THEN 1 END) AS frequency_band_L800_by_site,
    COUNT(CASE WHEN cd.type = 'lte' AND cd.frequency_band = 1800 THEN 1 END) AS frequency_band_L1800_by_site,
    COUNT(CASE WHEN cd.type = 'lte' AND cd.frequency_band = 2600 THEN 1 END) AS frequency_band_L2600_by_site
FROM
    cell_data AS cd
JOIN
    sites AS s ON cd.site_id = s.site_id
GROUP BY
    s.site_id;
