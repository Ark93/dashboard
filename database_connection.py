import cx_Oracle as co
import pandas as pd
import time

urls = {
    'localhost':
    'santos/santos@//localhost:1521/ORCLCDB'
}

def get_stored_databases():
    return list(urls.keys())


def connect(database_name):
    url_ = urls[database_name]
    try:
        connection = co.connect(url_)
        return connection
    except co.DatabaseError as e:
        # Log error as 
        err, = e.args
        print('error: {}'.format(err))
        raise

def getCursor(connection, arrSize=100000):
    cursor_ = connection.cursor()
    cursor_.arraysize = arrSize
    return cursor_


def get_DB_connection(db_, arrSize=100000):
    '''    Function to connect to stored oracle database host.
    To see which database are stored use function 'get_stored_databases'
    
    Parameters
    ----------
    db_: string
        Name of the Database
    arrSize: int
        size of array
    
    Returns
    -------
    Connection, Cursor
    '''
    conn = connect(db_)
    cursor = getCursor(conn)
    return conn, cursor


def execute_query(cursor_, query):
    """
    """
    try:
        start = time.time()
        result = cursor_.execute(query).fetchall()
        elapsed = (time.time() - start)
    except co.DatabaseError as e:
        err, = e.args
        print('error: %'.format(err))
        raise

    # Getting columns names
    # --------------------
    column_names = [col[0] for col in cursor_.description]
    # --------------------

    # Saving the result to a DataFrame
    # --------------------
    df = pd.DataFrame(result, columns=column_names)
    
    print("Number of columns Queried: {}".format(len(column_names)))
    print("Total Rows Retrieved: {:,}".format(len(df)))
    print("Execution Time: {:.2f} seconds".format(elapsed))
    
    return df


def insert_records(conn, cursor_, stmt_, df_):
    """ Function to insert new data contained in dataframe into database table
    """
    try:
        print("Inserting records using statement:")
        print(stmt_)
        cursor_.executemany(
            stmt_, list(df_.fillna(0).values)
        )
        conn.commit()
        print("Inserted Records: {}".format(cursor_.rowcount))
        pass
    except co.DatabaseError as e:
        err, = e.args
        print(err.message)
        raise

def update_records(conn, cursor_, stmt_, df_):
    """ Function to update records contained in dataframe into database table
    """
    try:
        print("Updating records using statement:")
        print(stmt_)
        cursor_.executemany(
            stmt_, list(df_.fillna(0).values)
        )
        conn.commit()
        print("Updated Records: {}".format(cursor_.rowcount))
        pass
    except co.DatabaseError as e:
        err, = e.args
        print(err.message)
        raise

def get_schema_tables( cursor_):
    """ Function to retrieve all table names in schema database
    """
    try:
        print("retrieving table names:")
        stmt_ = 'SELECT table_name FROM user_tables'
        print(stmt_)
        return execute_query(cursor_, stmt_)
    except co.DatabaseError as e:
        err, = e.args
        print(err.message)
        raise