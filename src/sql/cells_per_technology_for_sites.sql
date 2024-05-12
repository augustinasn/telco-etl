SELECT
    s.site_id,
    COALESCE(gsm_count, 0) AS site_gsm_cnt,
    COALESCE(umts_count, 0) AS site_umts_cnt,
    COALESCE(lte_count, 0) AS site_lte_cnt
FROM
    sites s
LEFT JOIN
    (SELECT
         site_id,
         COUNT(CASE WHEN type = 'gsm' THEN 1 END) AS gsm_count,
         COUNT(CASE WHEN type = 'umts' THEN 1 END) AS umts_count,
         COUNT(CASE WHEN type = 'lte' THEN 1 END) AS lte_count
     FROM
         cell_data
     GROUP BY
         site_id) c ON s.site_id = c.site_id;
