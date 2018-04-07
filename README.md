# Stationary Shop

E-commerce application where users may browse the catalog, manage their
shopping cart, and submit orders (dummy or through stripe). Admin users may
manage the catalog. Features include distributed session caching (with Redis),
localization (via Babel), full-text search (with
PostgreSQL), asynchronous emails (via threads).

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
If you have docker installed,
```
TODO
```

Alternatively, create a database named 'stationaryshop' and spin up a Redis
server. Open `config.py` and point the database and Redis URI's to your
servers. You may optionally open up `./app/__init__.py` to change and uncomment out
`return ja` (be sure to comment out the other return statement) to view the
website partially translated in Japanese. 

After configuring the settings, set the `FLASK_APP` env variable to
stationaryshop.py, and install the javascript (e.g `npm install`) and python
dependencies (e.g. `pip install -r requirements.txt`). Be sure to install the
python dependencies using `requirements.txt` located in `./src/`, not
`./src/requirements/` (I'm working on pruning the dev/prod/test dependencies).

`cd` into `./src` (if you are not already) and run the following:
```
flask db upgrade
flask seed-db
flask run
Go to http://localhost:5000
```
TODO
----
Dockerfile  
Modularize javascript and configure webpack  
Prune requirements.txt  
Add more unit tests  
Figure out how to send HTML emails.
