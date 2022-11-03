# Overview

This is a mock SQL database for a library! I wrote this to gain some experience learning about SQL and databases. This project provides all the necissary functions a library would need. 

I got my data set from [here](https://www.theguardian.com/news/datablog/2011/jan/01/top-100-books-of-all-time)

The main software is the interface.py. This acts as the terminal between the library and the database. To load the database with it's information, I wrote the importData.py program, which cleans, connects, and delievers the data to the database. Last, I used the testdata.py in the data folder as some scratch paper incase I needed to test queries or modify the data outside of the main program. 

current implimented commands: commands: search, remove, add, changeBook, numberOf, numberOfTypes, totalBooks

[Software Demo Video](https://youtu.be/2lfN0DlVUTg)

# Relational Database

I used a MySQL database that I locally hosted

For this project, I just started with one table, that being the books. It's data is divided into, index, ISBN, Title, Author, and publishing information, as well as number of copies of that book sold worldwide.

# Development Environment

Python made this project very easy to work with. Pandas also was used primarily to import, clean, and export the data into the SQL database. Other included libraries were SQLalchamy to aid Pandas by creating engines, as well as the MySQL package for it's connector.

# Useful Websites

* [W3Schools](https://www.w3schools.com/sql/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/mysql-common-mysql-queries/)

# Future Work

* Add error checking on input commands
* Add try/catching on the queries themselves
* Add another table with customers and their checked out books
