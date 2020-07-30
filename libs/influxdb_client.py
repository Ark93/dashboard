from influxdb import InfluxDBClient, DataFrameClient
from influxdb import exceptions
import pandas as pd
from . import config

def connect_database(db_name='testdb', from_=None):
    try:
        if(from_):
            client = InfluxDBClient( host =config.influxdb_config.get('influxdb_dockernet_host'),
                                    port = config.influxdb_config.get('influxdb_port'),
                                    database=config.influxdb_config.get('influxdb_db')
                                   )
        else:
            client = InfluxDBClient( host =config.influxdb_config.get('influxdb_host'),
                                    port = config.influxdb_config.get('influxdb_port'),
                                    database=config.influxdb_config.get('influxdb_db')
                                   )
        client.ping()
    except Exception as e:
        print('error connecting to database: {}'.format(e))
        raise
    return client

def query_to_dataframe(client ,query = 'Select time,value from mxx'):
    try:
        results = client.query(query)
        df = pd.DataFrame([x for x in results][0])
        df['time']= pd.to_datetime(df.time)
        df['serie'] = results.keys()[0][0]
    except Exception as e:
        print('error querying to database: {}'.format(e))
        raise
    return df
