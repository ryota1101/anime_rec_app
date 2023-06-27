# anime_rec_app

アニメデータベースから検索できるwebアプリケーション
<br>
Django,NGINX,uWSGI,PostgreSQL

- docker-compose up -d --build(Dockerfile更新)
- docker-compose up -d
- http://0.0.0.0:8888/app/
- docker container stop $(docker ps -q)