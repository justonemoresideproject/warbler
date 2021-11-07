import os
from unittest import TestCase
from sqlalchemy import exc

from models import db, User, Message, Follows, Likes

os.environ['DATABASE_URL'] = "postgresql:///warbler-test"

from app import app

db.create_all()

class UserModelMessageTesting(TestCase):
    """Test messages and the views"""

    def setUp(self):
        db.drop_all()
        db.create_all()

        self.uid = 11111
        user = User.signup(
            'testUser',
            'test@test.com',
            'password',
            None
        )

        self.user = User.query.get(self.uid)

        self.client = app.test_client()

    def test_message():

        message = Message(
            text='Hello',
            user_id=self.uid
        )

        db.session.add(m)
        db.session.commit()

        self.assertEqual(len(self.u.messages), 1)
        self.assertEqual(self.u.messages[0].text, 'Hello')

    def test_message_likes(self):
        m1 = Message(
            text="a warble",
            user_id=self.uid
        )

        m2 = Message(
            text="a very interesting warble",
            user_id=self.uid 
        )

        u = User.signup("yetanothertest", "t@email.com", "password", None)
        uid = 888
        u.id = uid
        db.session.add_all([m1, m2, u])
        db.session.commit()

        u.likes.append(m1)

        db.session.commit()

        l = Likes.query.filter(Likes.user_id == uid).all()
        self.assertEqual(len(l), 1)
        self.assertEqual(l[0].message_id, m1.id)