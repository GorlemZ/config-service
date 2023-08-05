# config-service
Part of SOA, used by other services to store and read their configurations.



conf_db_username_t
test
conf_db_dev_t


from peewee import *
db= PostgresqlDatabase("conf_db_dev_t", host=conf_db_test, port=5433, user="conf_db_username_t", password="test", autoconnect=False)
