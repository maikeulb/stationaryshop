# Stationary Shop

E-commerce application where users may browse the catalog, manage their
shopping cart, and submit orders (dummy or through stripe). Admin users may
manage the catalog. Features include a distributed session store (with Redis),
localization (via Babel), full-text search (with
PostgreSQL), and asynchronous emails (via threads).

Technology
----------
* Flask
* PostgreSQL
* Redis
* Babel (il8n/l10n)
* Bootstrap 4
* Stripe
* DataTables
* Noty

Screenshots
---
### Index 
The index and layout templates are translated to Japanese thanks to Google
translate (Most likely not too accurate).
![index](/screenshots/main.png?raw=true "Index")
***
![japanese](/screenshots/japanese.png?raw=true "Japanese")
### Catalog  
Display catalog-items per category (or all categories) and sort (client-side)
by price or perform a full-text (multi-match) search.
![catalog](/screenshots/catalog.png?raw=true "Catalog")
***
![search](/screenshots/search.png?raw=true "Search")
### Cart
Displays cart items with the ability to checkout (demo checkout or through
stripe). Checking out asynchronously (via threads) sends out order
confirmations.
![cart](/screenshots/cart.png?raw=true "Cart")
***
![mail](/screenshots/mail.png?raw=true "Mail")
### Admin 
Admin users may manage the catalog (admin interface powered by DataTables).
![admin](/screenshots/admin.png?raw=true "Admin")
***
![edit](/screenshots/edit.png?raw=true "Edit")

Run
---
With docker:
```
docker-compose build
docker-compose up
Go to http://localhost:5000
```

Alternatively, create a database named 'stationaryshop' and spin up a Redis
server. Open `config.py` and point the database and Redis URI's to your
servers. You may optionally open up `./app/__init__.py` to uncomment
`return ja` (be sure to comment out the other return statement) to view the
website partially translated in Japanese. 

After configuring the settings, set the `FLASK_APP` env variable to
stationaryshop.py, and install the javascript (e.g `npm install`) and python
dependencies (e.g. `pip install -r requirements.txt`). Be sure to install the
python dependencies using `requirements.txt` located in `./stationaryshop/`, not
`./stationaryshop/requirements/` (I'm working on pruning the dev/prod/test dependencies).

`cd` into `./stationaryshop` (if you are not already); then run:
```
flask db upgrade
flask seed-db
flask run
Go to http://localhost:5000
```

Deploy (Dockerized hosts)
---
This process is more thoroughly explained
[here](https://www.digitalocean.com/community/tutorials/how-to-provision-and-manage-remote-docker-hosts-with-docker-machine-on-ubuntu-16-04),
but I'll summarize the steps required (mostly for my own reference).

Prerequisites: Docker Machine installed on your local machine and DigitalOcean
API token.

1. Create Dockerized hos
```
docker-machine create --driver digitalocean --digitalocean-access-token
$DOTOKEN machine-name
```
2. Activate Dockerized host
```
eval (docker-machine env machine-name)
```
3. Build and run containers
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml build
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```
4. Unset Dockerized host
```
eval (docker-machine env -u)
```

TODO
----
Prune requirements.txt  
Add more unit tests  
Add File uploads for admin feature (seeded products are served from file
system, but not uploaded ones)  
HTML emails.
