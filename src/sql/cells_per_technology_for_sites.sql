SELECT
    s.site_id,
    COUNT(CASE WHEN c.type = 'gsm' THEN 1 END) AS site_gsm_cnt,
    COUNT(CASE WHEN c.type = 'umts' THEN 1 END) AS site_umts_cnt,
    COUNT(CASE WHEN c.type = 'lte' THEN 1 END) AS site_lte_cnt
FROM
    sites s
JOIN
    cell_data c ON s.site_id = c.site_id
GROUP BY
    s.site_id;
