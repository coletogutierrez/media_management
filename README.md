## MEDIA MANAGEMENT



### First:
1. docker-compose up
- OR:
1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r ./mediamanagementproject/requirements.txt

### Install reusable app:
If not docker:
cd django-monitoring && python3 run.py && cd ..

### Database:
1. cd mediamanagementproject
2. python3 manage.py makemigrations
3. python3 manage.py migrate
4. python3 manage.py createsuperuser

### Some tasks:
1. systemctl enable celery.service
2. systemctl start celery.service
3. systemctl status celery.service

4. apt install rabbitmq-server
5. systemctl enable rabbitmq-server.service
6. systemctl start rabbitmq-server.service
7. systemctl status rabbitmq-server.service

8. rabbitmqctl add_user mediamanagementproject mediamanagementproject
9. rabbitmqctl add_vhost mediamanagementproject_vhost
10. rabbitmqctl set_user_tags mediamanagementproject mediamanagementproject_tag
11. rabbitmqctl set_permissions -p mediamanagementproject_vhost mediamanagementproject ".*" ".*" ".*"

12. nohup celery -A mediamanagementproject worker &
13. To complement django-celery-results: nohup celery -A mediamanagementproject flower --basic_auth=user1:mediamanagementproject,user2:mediamanagementproject &

### Execute:
1. cd mediamanagementproject (if not)
2. python3 manage.py runserver

### Go to:
http://127.0.0.1:8000/admin/
- admin/admin


### More screenshots:
- Insert token:
python3 manage.py drf_create_token username
OR:
![Screenshot](create_token.png)

- Albums with more data:
![Screenshot](album_with_more_data_list.png)

- Documentation:
![Screenshot](swagger_and_redoc.png)

### Some urls:
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin/authtoken/tokenproxy/
- http://127.0.0.1:8000/admin/django_celery_results/taskresult/


### Docs:
- http://127.0.0.1:8000/api/schema/swagger-ui/
- http://127.0.0.1:8000/api/schema/redoc/
- http://127.0.0.1:8000/api/schema/

### Tests:
python3 manage.py test

### API URLS:
- (Use web interface and/or direct calls)
1. Api root:
- http://127.0.0.1:8000/api/v1/
2. All artists list:
- http://127.0.0.1:8000/api/v1/artists/?token=0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f
3. All albums with tracks:
- http://127.0.0.1:8000/api/v1/albums_with_tracks/?token=0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f
4. All albums of a artist:
- http://127.0.0.1:8000/api/v1/albums_with_filtering/?token=0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f&artist=1
5. All tracks of a album:
- http://127.0.0.1:8000/api/v1/tracks_with_filtering/?token=0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f&album=3
6. All albums and more data:
- http://127.0.0.1:8000/api/v1/albums_with_more_data/?token=0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f

-- Can add:
- &format=api
- &format=json
- &format=xml

### curl:
1. Authentication token implemented as param "token" in QueryParamAuthentication view. It can also be used in web interface
2. BrowsableAPIRenderer (api format for browser): default
3. JSONRenderer:
curl 'http://127.0.0.1:8000/api/v1/artists/' -H "Accept: application/json" -H 'Authorization: Token 0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f'
4. XMLRenderer:
curl 'http://127.0.0.1:8000/api/v1/artists/' -H "Accept: application/xml" -H 'Authorization: Token 0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f'


### python:
import requests
url = 'http://127.0.0.1:8000/api/v1/artists/'
headers = {'Authorization': 'Token 0f600cb1b626c5a4b41c3a4e30fc5b0f09e7085f'}
r = requests.get(url, headers=headers)

