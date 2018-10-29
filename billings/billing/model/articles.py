# -*- coding:utf-8 -*-
from billing import db

class articles(db.Model):
    __tablename__ = 'tbl_articles'

    def __init__(self, reference, description, billed, articletype, price, payout, units, serviceId, ledgernr_pl, ledgernr_dr):
        self.reference = reference
        self.description = description
        self.billed = billed
        self.articletype = articletype
        self.price = price
        self.payout = payout
        self.units = units
        self.serviceId = serviceId
        self.ledgernr_pl = ledgernr_pl
        self.ledgernr_dr = ledgernr_dr

    def __repr__(self):
        return '<Servicenumber %s>' % self.servicenumber