from sql_connection import managed_connection

def get_all_orders(limit=10, offset=0, sort_by='datetime', sort_order='ASC', filters=None):
    query = "SELECT * FROM orders"
    params = []
    if filters:
        clauses = [f"{key} = %s" for key, value in filters.items()]
        query += " WHERE " + " AND ".join(clauses)
        params = list(filters.values())

    query += f" ORDER BY {sort_by} {sort_order} LIMIT %s OFFSET %s"
    params += [limit, offset]

    with managed_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, tuple(params))
        orders = cursor.fetchall()
        return orders

def insert_new_order(order_data):
    query = "INSERT INTO orders (customer_name, total, datetime) VALUES (%s, %s, %s)"
    params = (order_data['customer_name'], order_data['total'], order_data['datetime'])

    with managed_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.lastrowid

def delete_order(order_id):
    try:
        with managed_connection() as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM order_details WHERE order_id = %s", (order_id,))
            cursor.execute("DELETE FROM orders WHERE order_id = %s", (order_id,))
            connection.commit()
            return order_id
    except Exception as e:
        connection.rollback()
        raise e



if __name__ == '__main__':
    # conn = managed_connection()
    print(get_all_orders())
#     print(insert_new_order(conn, {
#   "customer_name": "Johny",
#   "total": 150.0,
#   "datetime": "2025-05-03 10:30:00"
# }))
    
