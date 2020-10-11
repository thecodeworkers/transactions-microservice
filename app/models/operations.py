from mongoengine import *
import datetime

class Account(EmbeddedDocument):
    since = StringField()
    to = StringField()

class PartialOperation(Document):
    currency = StringField(max_length=10, required=True)
    amount = DecimalField(required=True, min_value=0, precision=8)
    price = DecimalField(required=True, min_value=0, precision=8)
    fee = DecimalField(required=True, min_value=0, precision=8)
    account = EmbeddedDocumentField(Account)
    description = StringField()
    transactionID = StringField(required=True, unique=True)

    meta = {
        'allow_inheritance': True,
        'collection': 'operations'
    }

class Changeable(EmbeddedDocument):
    operation = ReferenceField(PartialOperation)
    orderID = StringField(unique=True)

class Operations(PartialOperation):
    changeable = EmbeddedDocumentField(Changeable)
    created_at = DateTimeField(default=datetime.datetime.now)
