# How to interact with REST APIs from JavaScript

This repository accompanies our blog post "How to interact with REST APIs from JavaScript".

## How to run the Flask app

We've provided you with a sample REST API in the form of a Flask app.

To run it, you'll need Python 3 and Pipenv installed. Then, do:

```
cd backend
pipenv install
pipenv run flask run
```

## What does the app do?

The app stores movies. It has two endpoints, `POST /` and `GET /movies`.

### Adding movies

To add a new movie, send either form or JSON data containing `title` and `year` to the `POST /` endpoint.

See the examples `vanilla-post-form.html`, `vanilla-post-json.html`, and `fetch-post.html`.

### Retrieving movies

To get the movies currently stored, send a request to `GET /movies`.

See the examples `vanilla-get.html` and `fetch-get.html`.

## How to run the examples

Once the Flask app is running, just open the appropriate example file in your browser.

For example, on Windows, navigate to `file:///C:/Users/bob/vanilla-get.html` (or whatever path your file is in).