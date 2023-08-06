# config-service
Part of SOA, used by other services to store and read their configurations.

## usage
Launch with ```docker-compose up``` you can then go to http://localhost:8001/api/v1/configdataservice/docs and take a look at the documentation.

## test
Make sure you change the line 4 in the db.py file into ```isTest=True```
- Launch ```docker-compose up -d conf_db``` 
- Launch ```python -m uvicorn app.main:app --reload --host localhost --port 8002``` from the service sub-directory
- Launch ```pytest``` in the root dir