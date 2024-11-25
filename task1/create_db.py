from connect import create_connection

sql = """
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS status;
CREATE TABLE status (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

DROP TABLE IF EXISTS tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    status_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (status_id) REFERENCES status (id)
    ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users (id)
    ON DELETE CASCADE
);
"""

if __name__ == "__main__":
    with create_connection() as connection:
        if connection is not None:
            try:
                cursor = connection.cursor()
                cursor.execute(sql)
                connection.commit()
            except Exception as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")
