import mysql.connector


def connect_to_mysql(host, username, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        if connection.is_connected():
            print("Connected to MySQL Server")
            return connection
    except mysql.connector.Error as e:
        print("Error connecting to MySQL Server:", e)
        return None


def create_table(connection):
    try:
        cursor = connection.cursor()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS ages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            age INT
        )
        """
        cursor.execute(create_table_query)
        print("Table created successfully")
        cursor.close()
    except mysql.connector.Error as e:
        print("Error creating table:", e)


def insert_data(connection, table, name, age):
    try:
        cursor = connection.cursor()
        insert_query = f"""
        INSERT INTO {table} (name, age) VALUES (%s, %s)
        """
        cursor.execute(insert_query, (name, age))
        connection.commit()
        print("Data inserted successfully")
        cursor.close()
    except mysql.connector.Error as e:
        print("Error inserting data:", e)


def query_above_age(connection, table, age):
    try:
        cursor = connection.cursor()
        query = f"""
        SELECT * FROM {table} WHERE age > %s
        """
        cursor.execute(query, (age,))
        result = cursor.fetchall()
        if result:
            print("People above", age, "years old:")
            for row in result:
                print("ID:", row[0], "Name:", row[1], "Age:", row[2])
        else:
            print("No people found above", age, "years old")
        cursor.close()
    except mysql.connector.Error as e:
        print("Error querying data:", e)


def delete_by_name(connection, table, name):
    try:
        cursor = connection.cursor()
        delete_query = f"""
        DELETE FROM {table} WHERE name = %s
        """
        cursor.execute(delete_query, (name,))
        connection.commit()
        print("Records with name", name, "deleted successfully")
        cursor.close()
    except mysql.connector.Error as e:
        print("Error deleting records:", e)


def update_age_by_name(connection, table, name, new_age):
    try:
        cursor = connection.cursor()
        update_query = f"""
        UPDATE {table} SET age = %s WHERE name = %s
        """
        cursor.execute(update_query, (new_age, name))
        connection.commit()
        print("Age of", name, "updated to", new_age)
        cursor.close()
    except mysql.connector.Error as e:
        print("Error updating age:", e)


def close_connection(connection):
    try:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")
    except mysql.connector.Error as e:
        print("Error closing connection:", e)


def main():
    host = "localhost"
    username = "root"
    password = "my-secret-pw"
    database = "lesson13"
    table = "ages"

    connection = connect_to_mysql(host, username, password, database)
    if connection:
        create_table(connection)
        insert_data(connection, table, "Yarin", 20)
        query_above_age(connection, table, 25)
        update_age_by_name(connection, table, "Yarin", 30)
        delete_by_name(connection, table, "Yarin")
        close_connection(connection)


if __name__ == "__main__":
    main()
