import sqlalchemy as sa
import sqlalchemy.orm as orm

factory = None


def global_int(db_file: str):
    """Initialize the SQLite DB."""
    global factory

    if factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = 'sqlite:///' + db_file.strip()

    # To see whats going on, set echo to True
    engine = sa.create_engine(conn_str, echo=False)

    factory = orm.sessionmaker(bind=engine)
