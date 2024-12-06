import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Genre as GenreModel, db
from sqlalchemy.orm import Session

class Genre(SQLAlchemyObjectType):
    class Meta:
        model = GenreModel

class Query(graphene.ObjectType):
    genres = graphene.List(Genre)
    
    def resolve_genres(self, info):
        return db.session.execute(db.select(GenreModel)).scalars()
    
class AddGenre(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
    
    genre = graphene.Field(Genre)

    def mutate(self, info, name):
        with Session(db.engine) as session:
            with session.begin():
                genre = GenreModel(name=name)
                session.add(genre)
            
            session.refresh(genre)
            return AddGenre(genre=genre)
        
class UpdateGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, id, name):
        with Session(db.engine) as session:
            with session.begin():
                genre = session.execute(db.select(GenreModel).where(GenreModel.id == id)).scalars().first()
                if genre:
                    genre.name = name
                else:
                    return None
            session.refresh(genre)
            return UpdateGenre(genre=genre)
        
class DeleteGenre(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    genre = graphene.Field(Genre)

    def mutate(self, info, id):
        with Session(db.engine) as session:
            with session.begin():
                genre = session.execute(db.select(GenreModel).where(GenreModel.id == id)).scalars().first()
                if genre:
                    session.delete(genre)
                else:
                    return None
            session.refresh(genre)
            return DeleteGenre(genre=genre)
        
class Mutation(graphene.ObjectType):
    create_genre = AddGenre.Field()
    update_genre = UpdateGenre.Field()
    delete_genre = DeleteGenre.Field()