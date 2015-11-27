# Google Play Review Scrapper

Google doesn´t provide a public API to retrieve reviews for a specific application. 
If you are the app´s owner you could download the reviews, otherwise there is no official way to get that.

The main intent of this scrapper is to analyse the reviews in order to look for app´s weakness, so that you could identify what gaps the app don´t fill and maybe some opportunity arise.

## Warning

Read the license before use it.

## This script is simple and does basically this steps:

1. Do a post request to google play.
2. Do some transformations.
3. Outputs a json or html string

## What do you need before running the script

1. You will need to obtain the application ID (generally something like com.mycompany.myapp)

## Usage

python gpscrap.py --appid=com.mycompany.myapp --pagenum=1

Optional:
--format=<json or html>

