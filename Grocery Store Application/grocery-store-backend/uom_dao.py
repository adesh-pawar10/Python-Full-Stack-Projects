from sql_connection import managed_connection

def get_all_uoms():
    query = "SELECT * FROM uom"

    with managed_connection() as connection:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        uoms = cursor.fetchall()
        return uoms

def insert_uom(uom):
    query = "INSERT INTO uom (uom_name) VALUES (%s)"
    params = (uom['uom_name'],)

    with managed_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        return cursor.lastrowid

def delete_uom(uom_id):
    query = "DELETE FROM uom WHERE uom_id = %s"

    with managed_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query, (uom_id,))
        connection.commit()
        return uom_id


if __name__ == '__main__':
    # conn = managed_connection()
    print(get_all_uoms())
