# Google Play Review Scrapper

Google doesn´t provide a public API to retrieve reviews for a specific application. 
If you are the app´s owner you could download the reviews, otherwise there is no official way to get that.

The main intent of this scrapper is to analyse the reviews in order to look for app´s weakness, so that you could identify what gaps the app don´t fill and maybe some opportunity arise.

## Warning

Read the license before use it.

## Spec

Engine
- Should be able to scrap application's reviews from google play store

Parsing
- Should be able to parse a response string from a google play post request

Transforming
- Should be able to transform a json transformed content into html content
- Should be able to transform parsed content to a json formatted string

## What do you need before running the script

1. You will need to obtain the application ID (generally something like com.mycompany.myapp)

## Tests

Requirements:
- pip install nose
- pip install pinocchio

Run the specs:
$ nosetests --with-spec ./specs/

## Usage

python gpscrap.py --appid=com.mycompany.myapp --pagenum=1

Optional:
--format=json or --format=html

