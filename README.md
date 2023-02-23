# Python-and-django-full-stack-web-developer-bootcamp

### 1. Introduction

Materials (see on the website)

### 2. How web work ? 
####  Full stack
#####  Front-End 
- HTML, CSS, Javascript. 
- JQuery allows you to easily manipulate the contents of an HTML document by manipulating elements, classes, and IDs, while HTML allows you to only display the content of a webpage.
- Bootstrap : contains CSS- and JavaScript-based design templates for typography, forms, buttons, navigation and other interface components
- The differencen between CSS and HTML: The main difference between CSS and HTML is that CSS is used to style and layout web pages while HTML is used for the structure and content of a web page. In other words, HTML contains the information about the web page (text, images, media, etc.) while CSS determines how that information is displayed to users.
- Javascript allows you to add interactivity to the website, including programming logic.
##### Back-end
- The language : Python
- The framework : Django
- The database : SQLite

 
#### 3. HTML basics
###### Structure
###### Basic taggings  
Head, body, title, text style ..  (https://www.w3schools.com/TAGS/default.asp)
###### Lists
- odrder list
- unordered list
###### Nested list
###### div and span tags
The div and span elements are structural elements used to create divisions and sections within an HTML document. The <div> element is a generic container which can be used for any purpose - it is generally used for larger divisions of content, such as sections of a page. The <span> element is used for smaller sections of content, such as a single word or phrase, and it does not set apart the content from other sections of the same document.

Both elements can have attributes, such as a id attribute which can be used for styling with CSS. They can also contain text, images, and other elements 
###### Attributes
- Add more information to HTML tags. Ex : link or referencing an image ...

### 4. HTML advanced
###### Table
###### Forms basics : form, field, buttom...
###### Forms and labels
###### Forms and selections
- Radio button(linked)
- Drop down menus
- Text Area Inputs

### 5. CSS level one basics
- CSS describe how HTML elements are displayed on the page
- we can either define styling inside an HTML file or create .css file and then link to the html file. 

reference:

https://www.w3schools.com/css/

###### CSS level one part one
- you can specify property of element in html in css file
- use color picker to specify color

###### CSS level one part two
Set up parameters of body, div, p, span ...
- Set background of container
- Set up border parameters
- Set up text parameters

###### CSS level one part three
- CSS selectors : select subset of single of elements in html : user "ids" to target single element and use "classes" to target group of elements and combine them. 

Other types of selectors :

https://www.w3schools.com/cssref/css_selectors.php


###### CSS level one part four

If you want to see page in html code, right click and choose "inspect". The elements of html is on the left and Css styles is on the right.

###### CSS level one part five

CSS specificity : It defines the hierarchy of CSS styling and what types of tags overrule. To be more specific:

CSS specificity refers to how browsers determine which CSS rules get applied to an element. When two overlapping rules apply to the same element, the browser needs to know which one to pick. This is known as specificity. Generally speaking, the more specific a rule is, the greater priority it has over another less specific rule.

In order to prevent confusion and ensure that all of your intended rules are correctly applied, it's important to keep track of each element's specificity. This could include looking at how many classes and IDs are applied and which are more closely related to the element in question

For example: If we want to set color for the top priority items instead of all items.

More tricks :
https://designshack.net/articles/css/what-the-heck-is-css-specificity/


### 6. CSS level two advanced

###### Introduction
- Font properties such as size, weight, text alignment ...
- How to download and change fonts


###### Fonts

You can set a properties like font size of one paragraph is double larger than the size of another paragraph(by setting default font size for the text body and let other paragraphs double or tripple this size).

You can see the list of font in here(in case your os does not have proper fonts, you can have the ref in html and specify in css):
- fonts.google.com 
- fontlibrary.org

###### Box model

CSS box model dictate how HTML elements should look like(padding, border, margin ...)

Visualization and color palette css for the color : coolors.co

### 8. Bootstrap Overview

Bootstrapis a common framework used for Front-End Development

Take a look at https://getbootstrap.com/docs/5.3/examples/ (*)to see:
- Template reference for CSS
- Components (form, progress bar, button ...)

You can download css template or CDN(online host for you to connect to) to link to your html
###### Buttons
Click on CSS sections in the website (*) and just copy the code 
- Container
- Jumbotron
- Buttom
###### Forms
- Form for multipple option
- Form to fill in id and pass
- Text area
- Form checked
- Check box

###### Navbars
Require Javascripts plug-in
- Create link or list of link to another host(the location of navbar can be specified)
- The navbar location can be fixed even when we scroll up or down
- Hamburger menu
- Drop-down icons

###### Grids
The grid system provides the core mechanism by which using Bootstrap allows websites to look good across multiple devices of multiple screen sizes.

Example :
- If there is a table, then the columns in the table will not be merged even you scetch the website
- Split one column into 2 small columns in flexible way
See more examples in :
https://getbootstrap.com/docs/5.3/examples/grid/


###### Bootstrap project
- Thumbnails : easily display girds of images, videos, text and more ...
- Form for email and password
- Buttom
- Checkbox 
- Navbar to link to another website

### 9. Javascript Basics
- Build directly into the website
- Make the website more interactive
- Written in .js file then connect to our html

###### Javascripts basics
Basics syntaxs : alert, log, prompt ...

###### Connecting Javascripts 
Exercices + solutions

###### Operators
###### Control Flow
###### While Loops
###### For Loops

### 10. Javascript Level Two

###### Functions
###### Arrays
String is immutable but Arrays is mutable
###### Objects
- Similar to dictionary in python, the value of a key can be a function
- How to use this keyword : to call variable inside the object

### 11. Document Object Model(DOM)
The DOM will allow us to interface our Javascript code to interact with HTML and CSS

###### DOM interaction
A document object(DOM) include all parameters of a webpage and html elements are one of them. Some important attributes:
- document.URL
- document.body
- document.head
- document.links

Method for grabbing elements:
- document.getElementById()
- document.getElementByClassName()
- document.getElementsByTagName()
- document.querySelector()
- document.querySelectorAll()

###### Content interactions
How to change text, HTML code and attributes

###### Events
Set up interaction to occur on a particular event, such as a click or a hover. Ex : Listening for an event looks like this myvariable.addEventListener(event, func)
Other events:
- Clicks(Ex : click on text and it changes the colors)
- Hovers(mouseover, mouseout like. Ex : if you move mouse from text, it change the colors)
- Double clicks
- Drags
...
https://developer.mozilla.org/en-US/docs/Web/Events


### 12. jQuery
- jQuery is a Javascript library. Other library could be notify as Angular, React, NodeJS
- It is just a large single .js file that has many pre-built methods and objects that simplify your workflow
- Specifically interacting with the DOM and making HTTP requests (AJAX)

How do we get JQuery:
- Link a CDS hosted file(like we did for a bootstrap). See example in video 84. jQuery Project Solution Part One
- Download the .js file from jQuery's official web
- Jquery can replace Vanila code JS by more simple line of code

Reference for Jquery:
https://code.jquery.com

###### jQuery Events

###### jQuery Project

Build interactive game between 2 persons

### 13. Backend introduction

There are 3 files : urls.py, views.py, models.py
Take a look at Django overview slide. How it work:
Basically a user will request a URL on your website, something like www.helloworld.com. Then it goes to a urls.py which is then going to call the views.py file in Django. The the URLS are connect to views through a simple call and then that will call your model.py, which contains all the information of your database and the that will query your database for the information, feed it back to views.py, which create the view of your website(what is in the web), then we fill out that view with html, css and JavaScript and we send that back to the user.

### 16. Django basics

It's a web framework, which allows to solve 2 main problems:
- Map a requested URL from a userto the code that's actually meant to handle it
- Create the requested htmp dynamically
=> To sum up, it helps to connect back-end and front-end
It was used by Instagram, Mozilla ...

###### Django Project
- A Django Project is a collection of applications and configurations that when combined together will make up the full web application(your complete website running with Django).
- Create Django project : django-admin startproject first_project

Components :
- __init__.py : This a blank Python script that due to its special name let's Python know that this directory can be treated as a package
- settings.py : This is where you will store all your project settings
- urls.py : This is a python script that store all the URL patterns for your project. Basically the different pages of your web application and how they should connect to the end user.
- wsgi.py : This is a Python Script that acts as the Web Server Gateway Interface. It will later on help us deploy our web to production 
- manage.py : This is a Python Script that we will use a lot. It will be associates with many commands as we build our web app.

###### Django application
- A Django Application is created to perform a particular functionality for your entire web application. For example you could have a registration app, a polling app, comments app, etc.
- These Django Apps can then be plugged into other Django Projects, so you can reuse them! (Or use other people’s apps).
- Create Django appt : python manage.py startapp first_app

Components :
- __init__.py : This a blank Python script that due to its special name let's Python know that this directory can be treated as a package
- admint.py : You can register your models here which Django will then use them with Django’s admin interface.
- apps.py : Here you can place application specific configurations.
- models.py : Here you store the application’s data models.
- test.py : Here you can store test functions to test your code.
- views.py : This is where you have functions that handle requests and return responses.
- Migrations folder : This directory stores database specific information as it relates to the models

###### Django challenge

You need to :
- Create a function in view.py to specify the repsonse
- add URL patterns in urls.py to set up where the request should be sent to views.py, get info in the function in views.py and send back to the frontend

###### Django URL Mappings

In previous section we map urls.py to views.py. Now we use include() function from django.conf.urls to link urls.py to views.py by another file(undirectly)



























































