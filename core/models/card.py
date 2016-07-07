# coding: utf-8
import calendar

from datetime import datetime

from enum import Enum

from sky.extensions import db
from tools.datetimet import get_first_and_last_of_month_by_date


class Card(db.Model):

    __tablename__ = 'card'

    class Status(Enum):
        validate = 'V'
        invalidate = 'I'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.Text, nullable=False)
    status = db.Column(db.CHAR(1), nullable=False)
    pic_link = db.Column(db.String(80), nullable=False)
    like_amount = db.Column(db.Integer, nullable=False)
    creation_time = db.Column(db.DateTime, nullable=False)
    update_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, title, content, status, pic_link,
                 creation_time, update_time, like_amount=0):
        self.title = title
        self.content = content
        self._status = status
        self.pic_link = pic_link
        self.creation_time = creation_time
        self.update_time = update_time

    @property
    def status(self):
        return self.Status(self._status)

    @classmethod
    def create(cls, title, content, status,
               pic_link, like_amount=0):
        assert isinstance(status, cls.Status)

        instance = cls(
            title, content, status.value, pic_link,
            datetime.now(), datetime.now())
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

