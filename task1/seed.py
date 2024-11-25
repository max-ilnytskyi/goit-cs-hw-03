import faker
from random import randint, choice

from connect import create_connection

USERS_AMOUNT = 10
TASKS_AMOUNT = 20
STATUSES = ["new", "in progress", "completed"]


def generate_fake_data(
    users_amount: int, statuses: list[str], tasks_amount: int
) -> tuple:
    fake_users = []
    fake_tasks = []
    fake_statuses = []

    fake_data = faker.Faker()

    for status in statuses:
        fake_statuses.append((status,))

    for _ in range(users_amount):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(tasks_amount):
        fake_tasks.append(
            (
                fake_data.sentence(),
                choice((None, True)) and fake_data.paragraph(),
                randint(1, len(statuses)),
                randint(1, users_amount),
            )
        )

    return fake_users, fake_statuses, fake_tasks


def insert_data_to_db(users, statuses, tasks) -> None:
    with create_connection() as connection:
        if connection is not None:
            try:
                cursor = connection.cursor()

                sql_to_users = """INSERT INTO users(fullname, email)
                                    VALUES (%s, %s)"""
                sql_to_status = """INSERT INTO status(name)
                                    VALUES (%s)"""
                sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id)
                                    VALUES (%s, %s, %s, %s)"""

                cursor.executemany(sql_to_users, users)
                cursor.executemany(sql_to_status, statuses)
                cursor.executemany(sql_to_tasks, tasks)

                connection.commit()
            except Exception as e:
                print(e)
        else:
            print("Error! cannot create the database connection.")


if __name__ == "__main__":

    insert_data_to_db(
        *generate_fake_data(
            USERS_AMOUNT,
            STATUSES,
            TASKS_AMOUNT,
        )
    )
