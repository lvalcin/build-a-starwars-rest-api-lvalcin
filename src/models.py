from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = "character"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    age: Mapped[str] = mapped_column(String(10), nullable=True)
    species: Mapped[str] = mapped_column(String(30),unique=False, nullable=False)
    title: Mapped[str] = mapped_column(String(30),unique=False, nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.name,
            "species": self.species,
            "title": self.title
            # do not serialize the password, its a security breach
        }
    
class Planet(db.Model):
    __tablename__ = "planet"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    population: Mapped[int] = mapped_column(nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    landscape: Mapped[str] = mapped_column(String(80), unique=False, nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "age": self.age,
            "landscape": self.landscape
            # do not serialize the password, its a security breach
        }
    
class FavoriteCharacter(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    character_id: Mapped[int] = mapped_column(ForeignKey("character.id"))
    user: Mapped["User"]=relationship("User")
    character: Mapped["Character"]=relationship("Character")


    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.email,
            "character": self.character.name
            # do not serialize the password, its a security breach
        }

class FavoritePlanet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    planet_id: Mapped[int] = mapped_column(ForeignKey("planet.id"))
    user: Mapped["User"]=relationship("User")
    planet: Mapped["Planet"]=relationship("Planet")

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user.email,
            "planet": self.planet.name
            # do not serialize the password, its a security breach
        }