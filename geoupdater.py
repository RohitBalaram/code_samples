import psycopg2
from db_config import db_connection, geoclient_keys
from .nyc_geoclient import Geoclient
from customers.models import Client
from ats.models import Rdgs


def geo_client(db, date, client):

    conn = psycopg2.connect(dbname=db,
                            user=db_connection.USERNAME,
                            host=db_connection.HOST,
                            password=db_connection.PASSWORD)

    cur = conn.cursor()

    cur.execute("""
        select s.student_id, street_number, street, city
        from {0}.ats_rdgs as rdgs
        join {0}.sis_public_students s
            on s.local_student_id::integer = rdgs.student_id
        join {0}.ats_rbir as rbir
            on rbir.student_id = rdgs.student_id
            and rbir.tracking_date = rdgs.tracking_date
        where rdgs.tracking_date = '{1}';
    """.format(client, date))

    data = cur.fetchall()

    g = Geoclient(geoclient_keys.key, geoclient_keys.secret)

    errors, update, insert = [], 0, 0

    for row in data:
        results = g.address(row[1], row[2], row[3])
        try:
            if results['message']:
                errors.append(results)
        except:

            cur.execute("""
                select student
                from {0}.nyc_student_data_city_data
                where student = {1}
            """.format(client, row[0]))

            student = cur.fetchall()

            if len(student) > 0:
                student_id = student[0][0]
                cur.execute("""
                    update {0}.nyc_student_data_city_data
                    SET nta = '{1}',
                    district = {2}
                    where student = {3}
                """.format(
                        client, results['nta'],
                        results['communitySchoolDistrict'], student_id
                    )
                )

                cur.execute("COMMIT;")
                update += 1
            else:
                cur.execute("""
                    insert into {0}.nyc_student_data_city_data
                    (student, nta, district)
                    VALUES
                    ({1}, '{2}', {3});
                """.format(
                        client, row[0],
                        results['nta'],
                        results['communitySchoolDistrict'])
                    )
                cur.execute("COMMIT;")
                insert += 1
    print (db, len(errors), update, insert)


def get_most_recent_rdgs_date():
    date = Rdgs.objects.latest('tracking_date')
    return date.tracking_date


def geoclient_updater_with_address():
    etl_clients = Client.objects.exclude(schema_name='public')
    etl_clients = [client.schema_name for client in etl_clients]
    print (etl_clients)
    date = get_most_recent_rdgs_date()
    geo_client('dev', date, 'public')
    for client in etl_clients:
        print (client)
        geo_client('prod', date, client)
    return None
