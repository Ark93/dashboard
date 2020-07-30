import logging
import pytz

log_config={
    'log_file_name' : 'dashboard.log',
    'logging_level' : logging.INFO,
    'logging_format' : '%(asctime)s %(message)s' ,
}

influxdb_config={
    
    'influxdb_dockernet_host' : '172.18.0.2', #check the ipv4 from docker network
    'influxdb_host' : '127.0.0.1', #check the ipv4 from docker network
    'influxdb_port' : 8086,
    'influxdb_db' : 'testdb'
}

script_config={    
    'timezone' : pytz.timezone('America/Mexico_City'),
}

stocks = ['mxx']