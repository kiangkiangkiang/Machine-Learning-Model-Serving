For Services with **Load Balance** (`./load_balance_nginx.conf`)
```
upstream my_app {
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
    server 127.0.0.1:5003;
}
server{
    listen 80;
    location /{
        include uwsgi_params;
        uwsgi_pass  unix:/app/socket/uwsgi.sock;
    }
}
```