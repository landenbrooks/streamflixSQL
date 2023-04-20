
# Streamflix Portfolio Project

Description: My project is a dupe of the common streaming platform: Netflix. I used tables that included the account, the user, movies, genres, and a my stuff category. My stuff is where you can save the movies that you like or want to watch, but it only has a capacity of 5. Each movie has a title, genre, and a rating (scale of 1-100). There is a B-Tree index on the rating coloumn for the movies table, which makes it easier to find movies within a specific range of ratings.

##### ACCOUNT

| Method      | Path        | Parameters |
| ----------- | ----------- |------------|
| GET         | /accounts   |            |
| POST        | /accounts   |            |
| DELETE      | /accounts   | ID         |

##### GENRE

| Method      | Path        | Parameters |
| ----------- | ----------- |------------|
| GET         | /genres     | ID         |
| POST        | /genres     |            |
| DELETE      | /genres     | ID         |

##### MOVIE

| Method      | Path        | Parameters |
| ----------- | ----------- |------------|
| GET         | /movies     |            |
| PUT/PATCH   | /movies     | ID         |
| DELETE      | /movies     | ID         |
| POST        | /movies     |            |

##### MY STUFF

| Method      | Path        | Parameters |
| ----------- | ----------- |------------|
| PUT/PATCH   | /my_stuff   | ID         |
| DELETE      | /my_stuff   | ID         |

##### USER

| Method      | Path        | Parameters |
| ----------- | ----------- |------------|
| GET         | /users      |            |
| POST        | /users      | ID         |
| DELETE      | /users      | ID         |


##### How did the project's design evolve over time?

The project started off simple with some primary keys being titles and names, but in the end I added a primary key ID to each of the tables because I found that it was easier to connect them and make more sense. There were some issues towards the end using the ORM, but I think everything ended up working out. Now my database is more complex and inclusive of all of the columns. 

##### Did you choose to use an ORM or raw SQL? Why?

I chose to use ORM because I thought that it was easier to follow and understand. 

##### What future improvements are in store, if any?

Some future improvements would be to work on the My Stuff table and allow adding and deleting movies based on the capaity size. And to add more data to the database.