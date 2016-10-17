INSERT INTO name_email_list (First_Name, Last_Name, Email, Count)
SELECT T1.meta_value AS First_Name, T2.meta_value AS Last_Name, T3.meta_value AS Email, COUNT(1) AS Count 
FROM (SELECT meta_value, field_id 
FROM wp_kczafk_frm_item_metas 
WHERE field_id = 25 
OR field_id = 15 
OR field_id = 8) AS T1
LEFT JOIN (SELECT meta_value, field_id 
FROM wp_kczafk_frm_item_metas 
WHERE field_id = 26 
OR field_id = 16 
OR field_id = 9) AS T2
ON T1.item_id = T2.item_id 
LEFT JOIN (SELECT meta_value, field_id 
FROM wp_kczafk_frm_item_metas 
WHERE field_id = 27 
OR field_id = 17 
OR field_id = 10) AS T3
ON T1.item_id = T3.item_id
GROUP BY First_Name, Last_Name, Email
ORDER BY Count DESC;
