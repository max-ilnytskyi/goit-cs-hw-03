-- Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT * FROM tasks
WHERE user_id = 5;

-- Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT * FROM tasks
INNER JOIN status ON status.id = tasks.status_id
WHERE status.name = 'new';

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE tasks 
SET status_id = 2
WHERE id = 1;

-- Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
SELECT * FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM tasks
);

-- Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO tasks(title, description, status_id, user_id)
VALUES ('New task', 'Task description', 1, 5);

-- Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT * FROM tasks
LEFT JOIN status ON status.id = tasks.status_id
WHERE status.name <> 'completed';

-- Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE FROM tasks
WHERE id = 21;

-- Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
SELECT * FROM users
WHERE email LIKE '%ic%';

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE users
SET fullname = 'New fullname'
WHERE id = 5;

-- Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT status.id, status.name, COUNT(tasks.id) as tasks_count
FROM status
INNER JOIN tasks ON status.id = tasks.status_id
GROUP BY status.id;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT * FROM tasks
INNER JOIN users ON users.id = tasks.user_id
WHERE users.email LIKE '%example.net';

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT * FROM tasks
WHERE description ISNULL;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT * FROM users
INNER JOIN tasks ON tasks.user_id = users.id
INNER JOIN status ON status.id = tasks.status_id
WHERE status.name = 'in progress';

-- Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT users.fullname, COUNT(tasks.id)
FROM users
LEFT JOIN tasks ON tasks.user_id = users.id
GROUP BY users.id;