import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Movie as MovieModel, db
from models import Genre as GenreModel
from models import Movie_Genre as MovieGenreModel
from sqlalchemy.orm import Session

class Movie(SQLAlchemyObjectType):
    class Meta:
        model = MovieModel

class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel
'''
class MovieGenre(SQLAlchemyObjectType):
    class Meta:
        model = MovieGenreModel
        '''

class Query(graphene.ObjectType):
    movies = graphene.List(Movie)

    def resolve_movies_by_genre(self, info):
        return db.session.execute(db.select(MovieModel)).scalars()


