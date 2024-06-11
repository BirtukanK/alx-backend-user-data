#!/usr/bin/env python3
""" user model"""


from sqlalchemy import Column, String, Integer


class User(Base):
    """ user class to define model"""
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String, nullable = False)
    hashed_password = Column(String, nullable = False)
    session_id = Column(String, nullable = True)
    reset_token = Column(String, nullable = False)

    def __repr__(self):
        """ display values"""
        return "<User(id='%s', email='%s', session_id='%s')>" % (
                self.id, self.email, self.session_id)
