# GamesShop
A simple e-commerce app, written in Python, using Django, as an university project. It simulates an Internet shop with PC games. 

## Project structure

The application is located in the **shop** directory. 

### Rooting

All routing is done in **urls.py**.

### Views

All views are located in **views.py**. They are:
* **home** - gets all offers from database and renders a list
* **cart** - gets all items currently in cart from database and renders a list
* **add_to_cart** - adds item to cart, saves the change in database and redirects to home page
* **remove_from_cart** - removes item from cart, saves the change in database and redirects to cart page
* **order** - renders a form for personal data of the person ordering
* **payment** - gets authorization token from PayU and redirects to PayU page for payment
* **thanks** - renders a page thanking for purchase
* **details** - gets an offer from database and renders a page with details about product

### Model

The model is located in **models.py**.

### HTML templates

All HTML templates are located in **templates/shop** directory. They are:
* **base.html** - basic template containing the header, extended by all other templates
* **list.html** - a template for displaying offers as a list
* **shop.html** - contains a button for adding to cart
* **cart.html** - contains a button for removing from cart, a total amount and a button for ordering
* **order** - a form for personal data of the person ordering
* **thanks** - a page with thank you notice 
* **details** - a page for offer details

### CSS

CSS is located in **static/shop** directory.

## Database model

The database model consists of one table - **Offer**. The fields it contains are as follows:
* **name** - the name of the game
* **description** - description of the game
* **price** - the price of the game in PLN
* **release_date** - the date the game was released
* **developer** - the development studio that created the game
* **in_order** - boolean field informing whether or not the game is in cart
* **cover_image** - the url to an image of the cover of the game

## Technology

* **[Python](https://www.python.org/downloads/)**
* **[Django](https://www.djangoproject.com/download/)**
* **[requests](https://pypi.org/project/requests/)**

## Getting started

### First start-up

Before the first compilation you need to download all necessery technology listed above. After that you need to migrate the database. You can do that by opening the command prompt and navigating to the project's main directory. Than you need to type two commands:

```
python manage.py makemigrations

python manage.py migrate
```

### Compilation

To compile the project open the command prompt and navigate to the project's main directory. Than use the command:

```
python manage.py runserver
```
