from psycopg2 import connect, OperationalError, sql, DatabaseError

try:
    cnx = connect(user='postgres', password='coderslab', host='localhost', port=5433, database='postgres')
    cursor = cnx.cursor()
    print('Connected')
except OperationalError as error:
    print("Connection Error")
    raise ValueError(f"Connection Error: {error}")

query_create_table_user = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name}(
        id SERIAL,
        name VARCHAR(50),
        email VARCHAR(120) UNIQUE,
        password VARCHAR(60) DEFAULT 'ala',
        PRIMARY KEY (id)
    )
""").format(table_name=sql.Identifier('user'))

query_insert_user = sql.SQL("""
    INSERT INTO {table_name}(name, email, password, price)
    VALUES (%s, %s, %s, %s)
""").format(table_name=sql.Identifier('user'))

query_update = sql.SQL("""
    UPDATE {table_name}
    SET email = %s 
    WHERE id = %s;
""").format(table_name=sql.Identifier('user'))

query_delete = sql.SQL("""
    DELETE
    FROM {table_name}
    WHERE id = %s
""").format(table_name=sql.Identifier('user'))

query_create_table_address = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name}(
        id SERIAL PRIMARY KEY,
        street VARCHAR(85),
        city VARCHAR(85),
        notes TEXT,
        userID SMALLINT,
        FOREIGN KEY (userID) REFERENCES {foreign_table_name}(id))
        
""").format(table_name=sql.Identifier('address_user'), foreign_table_name=sql.Identifier('user'))
query_alter = sql.SQL("""
    ALTER TABLE {table_name} ADD COLUMN Price DECIMAL(7, 2) DEFAULT 0

""").format(table_name=sql.Identifier('user'))

query_alter2 = sql.SQL("""
    ALTER TABLE {table_name} ADD COLUMN DateOfCreated TIMESTAMP DEFAULT CURRENT_TIMESTAMP

""").format(table_name=sql.Identifier('user'))


with cnx:
    # try:
    #     cursor.execute(query_create_table_address)
    # except DatabaseError as error:
    #     print(error)
    try:
        cursor.execute(query_insert_user, ('Jarek', 'jarek@gmail.com', 'janusz1', 3.50))
    except DatabaseError as error:
        print(error)
    # try:
    #     cursor.execute(query_update, ('janusz@wp.pl', 1))
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_delete, (1,))
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_alter2)
    # except DatabaseError as error:
    #     print(error)

cnx.close()
