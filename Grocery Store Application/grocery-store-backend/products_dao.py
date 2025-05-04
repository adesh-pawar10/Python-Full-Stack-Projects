from sql_connection import managed_connection

def get_all_products(limit=10, offset=0, sort_by='name', sort_order='ASC', filters=None):
    query = "SELECT * FROM products"
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
        products = cursor.fetchall()
        return products

def insert_new_product(product_data):
    query = "INSERT INTO products (name, uom_id, price_per_unit) VALUES (%s, %s, %s)"
    params = (product_data['name'], product_data['uom_id'], product_data['price_per_unit'])

    with managed_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.lastrowid

def delete_product(product_id):
    query = "DELETE FROM products WHERE product_id = %s"

    with managed_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, (product_id,))
        connection.commit()
        return product_id



if __name__ == '__main__':
    # conn = managed_connection()

    # Insert a test product
    # new_id = insert_new_product(conn, {
    #     'name': 'potatoes',
    #     'uom_id': 1,
    #     'price_per_unit': 10
    # })
    # print(f"Inserted new product with ID: {new_id}")

    # Optional: fetch all products
    print(get_all_products())
