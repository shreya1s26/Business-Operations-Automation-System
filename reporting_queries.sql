-- Weekly Revenue Report
SELECT 
    DATE(created_at) AS report_date,
    SUM(revenue) AS total_revenue,
    COUNT(order_id) AS total_orders
FROM operations_data
GROUP BY DATE(created_at)
ORDER BY report_date DESC;

-- Top Customers
SELECT 
    customer_id,
    SUM(revenue) AS customer_revenue
FROM operations_data
GROUP BY customer_id
ORDER BY customer_revenue DESC
LIMIT 10;
