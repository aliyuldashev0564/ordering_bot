import datetime
import config
import psycopg2


async def adding_db(agent, to_product, money, client_name, client_number, client_addres):
    try:
        time = datetime.datetime.now()
        connection = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database='Alis'
        )

        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(f'SELECT id FROM all_agent WHERE telegram_id = {agent}')
            a = cursor.fetchone()
            cursor.execute(
                f"""INSERT INTO all_orders (time,to_product_id,agent_id, money, client_name, client_number, client_addres) VALUES
                ('{time}',{to_product}, '{a[0]}', '{money}', '{client_name}', '{client_number}','{client_addres}');"""
            )
        connection.close()
    except Exception as ex:
        print(ex)
async def selecting(telegram_id):
    try:
        connection = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database='Alis'
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            try:
                sql = f"SELECT * FROM all_agent WHERE telegram_id={telegram_id}"
                cursor.execute(sql)
                all = cursor.fetchone()
                if all ==None:
                    connection.close()
                    return False
                else:
                    connection.close()
                    return True
            except:
                connection.close()

                return False
    except Exception as ex:
        print(ex)
async def select_product(name):
    try:
        connection = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database='Alis'
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            sql = f"SELECT narx, image, charecter FROM all_product WHERE name='{name}'"
            cursor.execute(sql)
            all = cursor.fetchone()
            return all
    except Exception as ex:
        print(ex)
async def select_agent(telegram_id):
    try:
        connection = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database='Alis'
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            sql = f"SELECT name, tel_num FROM all_agent WHERE telegram_id='{telegram_id}'"
            cursor.execute(sql)
            all = cursor.fetchone()
            return all
    except Exception as ex:
        print(ex)
async def select_product_all():
    try:
        connection = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database='Alis'
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            sql = f"SELECT name FROM all_product "
            cursor.execute(sql)
            all = cursor.fetchone()
            return all
    except Exception as ex:
        print(ex)
async def add_user(telegram_id, tell,name):
    try:
        connection = psycopg2.connect(
            host=config.DB_HOST,
            user=config.DB_USER,
            password=config.DB_PASS,
            database='Alis'
        )
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO all_agent (telegram_id,name,tel_num) VALUES
                ({telegram_id},'{name}','{tell}');"""
            )
        connection.close()
    except Exception as ex:
        print(f'[info] {ex}')