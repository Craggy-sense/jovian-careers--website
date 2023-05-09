from sqlalchemy import create_engine, text
import os


db_connection_string = os.environ['MY_PASSWORD']

engine = create_engine(
    db_connection_string,
    connect_args={
         "ssl": {
              "ssl_ca": "/etc/ssl/cert.pem"
        }
    })
def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
           jobs.append(dict(zip(result.keys(), row)))

        return jobs
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :val"),
            {"val":id}
        )
        rows = result.fetchone()
        if len(rows) == 0:
            return None
        else:
            return dict(zip(result.keys(), rows))


