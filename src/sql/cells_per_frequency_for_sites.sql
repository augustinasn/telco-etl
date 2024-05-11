SELECT
    s.site_id,
    CONCAT('frequency_band_G', c.frequency_band, '_by_site') AS frequency_band_label,
    COUNT(*) AS cell_count
FROM
    sites s
JOIN
    cell_data c ON s.site_id = c.site_id
GROUP BY
    s.site_id,
    c.frequency_band;