def add_table(cur, name: str, fields):
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {name}(           
        );
        """)

    for column, constraint in fields.items():
        cur.execute(f"""
            ALTER TABLE {name}
            ADD {column} {constraint};""")
    return print(f'Таблица {name} c полями {fields} успешно создана ')

def add_client(cur,client):
    cur.execute(
        f'''INSERT INTO client (name,surname) 
        VALUES ({client[0]}, {client[1]});'''
    )
    return print(f'Клиент {client} добавлен в базу данных')

def get_client_id(cur, name, surname):
    cur.execute(f'''
        SELECT id FROM client
        WHERE name = {name} AND surname = {surname}
    ;''')
    list_id = []
    for id in cur.fetchall():
        list_id += id
    print(f'Найдено {len(list_id)} клиентов, их id: {list_id}')
    return list_id

def add_phone(cur, name, surname, client_info):
    list_id = get_client_id(cur, name, surname)
    if len(list_id) > 1:
        client_id = int(input('Введите id клиента'))
    else: client_id = list_id[0]

    cur.execute(f'''
                    INSERT INTO info(phone, client_id)
                    VALUES ({client_info[0]}, {client_id})
                ;''')
    return print(f'Номер ({client_info[0]} успешно добавлен клиенту {name} {surname} c id {client_id}')



def change_info(cur, name, surname, table, field, data):
    list_id = get_client_id(cur, name, surname)
    if len(list_id) > 1:
        client_id = int(input('Введите id клиента'))
    else:
        client_id = list_id[0]
    if table == 'client':
         cur.execute(f'''
                    UPDATE {table}
                    SET {field} = {data}
                    WHERE id = {client_id}
                   ;''')
    if table == 'info':
        cur.execute(f'''
                    UPDATE {table}
                    SET {field} = {data}
                    WHERE client_id = {client_id}
                ;''')
    return print(f'В таблице {table} у клиента с id {client_id} поле  {field} изменено на {data}')

def del_phone(cur, name, surname):
    list_id = get_client_id(cur, name, surname)
    if len(list_id) > 1:
        client_id = int(input('Введите id клиента'))
    else:
        client_id = list_id[0]
    cur.execute(f'''
                    UPDATE info i
                    SET phone = NULL
                    WHERE client_id = {client_id}
                ;''')
    return print(f'У клиента с id {client_id} удален номер телефона')

def del_client(cur, name, surname):
    list_id = get_client_id(cur, name, surname)
    if len(list_id) > 1:
        client_id = int(input('Введите id клиента'))
    else:
        client_id = list_id[0]
    cur.execute(f'''
                    DELETE  FROM info i
                    WHERE client_id = {client_id}                           
                ;''')
    cur.execute(f'''
                    DELETE  FROM client c
                    WHERE id = {client_id}                           
                ;''')
    return print(f'Клиент с id {client_id} успешно удален')

def search_client(cur, field, data):
    cur.execute(f'''
                    SELECT * FROM client c
                    FULL OUTER JOIN info i ON c.id = i.client_id
                    WHERE {field} = {data}                          
                    ;''')
    data = cur.fetchall()
    data_dict = { 'id': data[0][0],  'name': data[0][1], 'surname': data[0][2], 'email': data[0][3], 'phone': data[0][4]}
    print(data_dict)
    return data_dict