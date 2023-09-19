#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from models import storage_type
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql.schema import Table
from sqlalchemy.orm import relationship


if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60),
                            ForeignKey('places.id'),
                            primary_key=True,
                            nullable=False),
                    Column('amenity_id', String(60),
                            ForeignKey('amenities.id'),
                            primary_key=True,
                            nullable=False)
                    )


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    if storage_type == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship('Review', backref='place',
                                cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                            viewonly=False, backref='place_amenities')

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            ''' returns list of reviewed instatnces
                with place_id equals to the current place.id.
                FileStorage relationship between Place and Review
            '''
            from models import storage
            all_reviews = storage.all(Review)
            First = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    First.append(review)
            return First

        @property
        def amenities(self):
            ''' returns the list of Amenity instances from
                all Amenity.ids linked to the place based on
                the attribute amenity_ids it contains
            '''
            from models import storage
            all_amenities = storage.all(Amenity)
            First = []
            for amenity in all_amenities.values():
                if amenity.id in self.amenity_ids:
                    First.append(amenity)
            return First

        @amenities.setter
        def amenities(self, obj):
            ''' This adds an Amenity.id to the attribute amenity_ids.
                It only accepts Amenity objects
            '''
            if obj is not None:
                if instance(obj, Amenity):
                    if obj.id not in self.amenity_ids:
                        self.amenity_ids.append(obj.id)
