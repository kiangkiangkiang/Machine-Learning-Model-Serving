The Flask API, while suitable for many use cases, may exhibit performance bottlenecks under high traffic loads. To address this limitation and construct a more robust web server, we propose incorporating Nginx and WSGI. By positioning Nginx as a reverse proxy in front of our existing application server (model endpoint), we can distribute incoming traffic more efficiently and improve overall system performance.

<p align="center">
    <img src = "./web_flow.png" style="width: 100%; "></img>
</p>

Our next step, following the establishment of these fundamental concepts, is to implement a proxy layer as an intermediary for our application server.




### Reference:
1. [WSGI Basic Concept](https://minglunwu.com/notes/2021/flask_plus_wsgi.html/)
2. [Flask with Nginx & WSGI](https://medium.com/%E5%B7%A5%E7%A8%8B%E9%9A%A8%E5%AF%AB%E7%AD%86%E8%A8%98/flask-app-%E5%8A%A0%E4%B8%8A-wsgi-%E5%8F%8A-nginx-%E6%9C%8D%E5%8B%99-b8bdc60d1dc7)
3. [Forward Proxy & Reverse Proxy](https://www.pressplay.cc/project/F720CEB1D6057D7ABB5614722AB18FFF/articles/660A57208C29FF94453548ED21F284EF)
4. [Load Testing Tool](https://loader.io/)