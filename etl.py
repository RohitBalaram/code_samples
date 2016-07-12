from config import db1, db2, dev_pwd
import psycopg2
import traceback
import sys
from io import BytesIO
from customers.models import Client


def db2db(dest_db):
    clients = Client.objects.filter(sis_key__isnull=False)
    clients = [(client.schema_name, client.sis_key) for client in clients]

    if dest_db == 'dev':
        clients = [('public', dev_pwd)]

    # for now list out tables for etl, eventually store dynamically in db
    tables = [
        ("schema.table1", "schema.table1"),
        ("schema.table2", "schema.table2"),
        # The code this is based on processes over 100 tables
    ]

    for client in clients:
        conn1 = psycopg2.connect(dbname=db1.DATABASE_NAME,
            user=db1.USERNAME,
            host=db1.HOST,
            password=client[1],
            port=db1.PORT,
            sslmode=db1.SSL_MODE
        )

        conn2 = psycopg2.connect(dbname=dest_db,
            user=db2.USERNAME,
            host=db2.HOST,
            password=db2.PASSWORD
        )
        for table in tables:
            try:
                input = BytesIO()
                cur = conn1.cursor()

                cur.copy_expert("""
                    COPY (select row_number() OVER (ORDER BY 1) AS id,
                    *, now() as refresh_date
                    from {0}) TO STDOUT
                    """.format(table[0]), input)

                cur.close()
                input.seek(0)
                cur = conn2.cursor()

                cur.copy_expert(
                    'DELETE FROM {0}.{1};'.format(client[0], table[1]),
                    input
                )

                cur.copy_expert(
                    'COPY {0}.{1} FROM STDOUT'.format(client[0], table[1]),
                    input
                )

                cur.execute("COMMIT;")
                cur.execute("""
                    select count(*)
                    from {0}.{1};
                    """.format(client[0], table[1]))

                print ("{0} in {1}.{2}".format(cur.fetchone()[0], client[0], table[1]))
            except:
                print(traceback.format_exc())
                print(sys.exc_info()[0])
                print ('ERROR! Failed to import {0}.{1};'.format(client[0], table[1]))
        
        cur.close()
