from django.db import connection
from psycopg2.extensions import AsIs


def dictfetchall(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        OrderedDict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def get_all_nyc_growth_scores(params):
    conn = connection
    cur = conn.cursor()
    cur.execute("""
        select z.rank, z.count, z.percentile, z.per_proficient, 
        z.dbn, z.school_name, z.subject, z.grade, 
        %(calculation)s as growth,
        z.total_tested, z.total_mean,
        z.num_level_1, z.per_level_1,
        z.num_level_2, z.per_level_2,
        z.num_level_3, z.per_level_3,
        z.num_level_4, z.per_level_4

        FROM (
            select (count - rank)/count::numeric * 100 as percentile, *
            FROM (
                select
                rank() OVER (PARTITION BY nys.year, nys.subject ORDER BY nys.per_proficient desc),
                count(*) OVER (PARTITION BY nys.year, nys.subject), nys.*, b.sum

                FROM (
                    select distinct this.id, this.year, this.dbn, this.school_name, 
                    this.subject, this.grade, this.total_tested, this.total_mean, 
                    this.num_level_1, this.per_level_1,
                    this.num_level_2, this.per_level_2,
                    this.num_level_3, this.per_level_3,
                    this.num_level_4, this.per_level_4,
                    this.num_proficient,
                    this.per_proficient - that.per_proficient as per_proficient

                    FROM city_data.nys_test_results_all_nyc_schools as this

                    JOIN (
                        select *
                        from city_data.nys_test_results_all_nyc_schools
                        where year = %(academic_year)s - 1
                    ) as that
                        on that.dbn = this.dbn
                        and that.subject = this.subject
                        and that.grade = this.grade
                    where this.year = %(academic_year)s
                ) as nys

                JOIN (
                    select dbn, sum(grade::numeric)
                    from city_data.nys_test_results_all_nyc_schools
                    where (grade != 'All Grades' and grade is not null)
                    and year = %(academic_year)s
                    group by dbn
                ) as b 
                    on b.dbn = nys.dbn

                where b.sum >= %(three_eight_cohort)s
                and nys.year = %(academic_year)s
                and nys.grade = %(grade_level)s
                and substring(nys.dbn, 1,2) = '84'
            ) as a
            order by a.subject, a.rank
        ) as z

        """, {
                'academic_year': params['academic_year'],
                'grade_level': params['grade_level'],
                'three_eight_cohort': params['three_eight_cohort'], 
                'calculation': AsIs(params['calculation'])
            })

    rows = dictfetchall(cur)
    cur.close()
    return rows
