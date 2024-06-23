SELECT 
    CASE 
        WHEN "city" <> 'not available in demo dataset' THEN "city"
        ELSE "country"
    END AS location,
    SUM("productPrice" * COALESCE("productQuantity", 1)) AS transaction_revenue
FROM all_sessions
GROUP BY 
    CASE 
        WHEN "city" <> 'not available in demo dataset' THEN "city"
        ELSE "country"
    END
ORDER BY transaction_revenue DESC;