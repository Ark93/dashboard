from dashboard import database_connection


def get_main_table():
    conn, cursor = database_connection.get_DB_connection(db_ ='localhost');

    df = database_connection.execute_query(cursor, query='''select unique
    SUB_ID, SUB_LINE_WID, PARENT_PART_NUM, OPERATION_TYPE,
    TOTAL_PERIODS, SUB_LN_START_DT, SUB_LN_END_DT,LABEL
    from UCM_ONB_USAGE_DAILY''')

    return df

