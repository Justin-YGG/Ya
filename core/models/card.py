# coding: utf-8
import calendar

from datetime import datetime

from enum import Enum

from sky.extensions import db
from tools.datetimet import get_first_and_last_of_month_by_date


class Card(db.Model):

    __tablename__ = 'card'

    class Category(Enum):
        selected = 'S'
        common = 'C'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.String(80), nullable=False)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.CHAR(1), nullable=False)
    pic_link = db.Column(db.String(80), nullable=False)
    like_amount = db.Column(db.Integer, nullable=False)
    tag_id = db.Column(db.Integer, nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, author_id, title, content, category, pic_link,
                 tag_id, creation_time, update_time, like_amount=0):
        self.author_id = str(author_id)
        self.title = title
        self.content = content
        self._category = category
        self.pic_link = pic_link
        self.tag_id = str(tag_id)
        self.like_amount = like_amount
        self.creation_time = creation_time
        self.update_time = update_time

    @property
    def category(self):
        return self.Category(self._category)

    @category.setter
    def category(self, new_category):
        self.category = new_category
        db.session.commit()

    @classmethod
    def create(cls, author_id, title, content, pic_link, tag_id, 
               like_amount=0, category=cls.Category.common):
        assert isinstance(category, cls.Category)

        instance = cls(
            author_id, title, content, category.value, pic_link,
            tag_id, datetime.now(), datetime.now())
        db.session.add(instance)

        db.session.commit()

    @classmethod
    def get(cls, id_):
        return cls.query.filter_by(id=id_).one_or_none()

    @classmethod
    def get_ids_by_date(cls, date_):
        first_day, last_day = get_first_and_last_of_month_by_date(date_)


    @classmethod
    def get_multi(cls, ids):
        return [cls.get(id_) for id_ in ids]

