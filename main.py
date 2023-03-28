import psycopg2
import functions


if __name__ == '__main__':
    with psycopg2.connect(database="PyDB", user="postgres", password="300589iI") as conn:
        with conn.cursor() as cur:
            client_fields = {'id': 'SERIAL PRIMARY KEY', 'name': 'text NOT NULL', 'surname': 'text NOT NULL'}
            info_fields = {'email': 'VARCHAR[40]', 'phone': 'integer', 'client_id': 'integer NOT NULL REFERENCES client(id)'}
            client_1 = (r"'IVAN'", r"'IVANOV'")
            client_2 = (r"'IVAN'", r"'IVANOV'")
            client_3 = (r"'IGOR'", r"'IGOREV'")
            client_1_info = (7897979, 'hkjh@mail.ru')
            client_3_info = (156561, 'sdfsfd@mail.ru')

            cur.execute(
                f'''DROP TABLE info;
                    DROP TABLE client;'''
            )
            functions.add_table(cur, 'client', client_fields)
            functions.add_table(cur, 'info', info_fields)
            functions.add_client(cur, client_1)
            functions.add_client(cur, client_2)
            functions.add_client(cur, client_3)
            functions.add_phone(cur, r"'IVAN'", r"'IVANOV'", client_1_info)
            functions.add_phone(cur, r"'IGOR'", r"'IGOREV'", client_3_info)
            functions.change_info(cur, r"'IVAN'", r"'IVANOV'", 'client', 'surname', r"'PETROV'")
            functions.change_info(cur, r"'IVAN'", r"'IVANOV'", 'info', 'phone', 87987954)
            functions.del_phone(cur, r"'IVAN'", r"'IVANOV'" )
            functions.del_client(cur,r"'IVAN'", r"'IVANOV'" )
            functions.search_client(cur, 'phone', 156561)
            conn.commit()
