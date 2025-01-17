docker.cleanup:
	docker rm $(docker ps -aq)

docker.build:
	docker-compose -f local.yml build

docker.up.django:
	docker-compose -f local.yml up django

docker.django-cli:
	docker-compose -f local.yml run django-cli python manage.py shell


import.positions:
	cp ../finx-reports-ib/data/*_open_positions.csv data
	docker-compose -f local.yml run django-cli python manage.py runscript import_positions

import.trades:
	cp ../finx-reports-ib/data/*_trades.csv data
	docker-compose -f local.yml run django-cli python manage.py runscript import_trades

db.migrate:
	docker-compose -f local.yml run django-cli python manage.py migrate

db.makemigrations:
	docker-compose -f local.yml run django-cli python manage.py makemigrations


# dump data from aws db
db.pg_dump:
	docker-compose -f local-aws.yml run django-cli python manage.py runscript db_dump

# import data into local db
db.pg_restore:
	docker-compose -f local.yml run django-cli python manage.py runscript db_import
