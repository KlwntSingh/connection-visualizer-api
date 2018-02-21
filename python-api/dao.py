from mysql.connector import pooling
from config import CONFIG

pool = pooling.MySQLConnectionPool(pool_name = "mypool",
                              pool_size = 10,
                              **CONFIG)

SELECT_QUERY = """
    SELECT * FROM ip_info where start_ip_number <= {ip} and end_ip_number >= {ip};
"""
def get_ip_address_info(ip):
    query = SELECT_QUERY.format(ip=ip)
    connection = pool.get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    rs = cursor.fetchone()
    json = {}
    json["country"] = rs[2]
    json["state"] = rs[3]
    json["region"] = rs[4]
    cursor.close()
    connection.close()
    return json