from flask import Flask
from flask_graphql import GraphQLView
import graphene
from movie_schema import Query, Mutation
from models import Movie_Genre
#from genre_schema import Query, Mutation
from models import db
from sqlalchemy.orm import Session

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:thegoblet2@localhost/movie_db'
db.init_app(app)

schema = graphene.Schema(query=Query, mutation=Mutation)

app.add_url_rule(
    '/graphql',
    view_func= GraphQLView.as_view('graphql', schema=schema, graphiql = True)
)

def init_movie_genre_data():
    with Session(db.engine) as session:
        with session.begin():
            movie_genres = [
                Movie_Genre(movie_id = 1 , genre_id= 2),
                Movie_Genre(movie_id = 2 , genre_id= 3)
            ]
            session.add_all(movie_genres)

with app.app_context():
    db.create_all()
    #init_movie_genre_data()

if __name__ == '__main__':
    app.run(debug=True)