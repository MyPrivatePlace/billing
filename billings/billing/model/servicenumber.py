# -*- coding:utf-8 -*-
from billing import db

class servicenumber(db.Model):
    __tablename__ = 'tbl_servicenumber'

    def __init__(self, customerId, servicenumber, serviceId, source, contractId):
        self.customerId = customerId
        self.servicenumber = servicenumber
        self.serviceId = serviceId
        self.source = source
        self.contractId = contractId

    def __repr__(self):
        return '<Servicenumber %s>' % self.servicenumber