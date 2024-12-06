TThis flask app uses graphql functionality to view, add, delete, and update both movies and genres, and also
allows movies and genres to be associated in a many-to-many relationship. Queries can then be performed to find movies
by genre, or to find genres associated with a particular movie. The models file contains models that outline the movie object,
genre object, and association table that links them. The movies_schema file contains the queries and mutations for performing these
functions on movies and genres with graphql, as well as their attendant resolvers. 
