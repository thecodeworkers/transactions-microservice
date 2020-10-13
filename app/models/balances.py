from mongoengine import Document, StringField, BooleanField, DecimalField, ObjectIdField

class Balances(Document):
    user = ObjectIdField(required=True)
    currency = StringField(required=True)
    amount = DecimalField(required=True, min_value=0, precision=8)
    pending_amount = DecimalField(required=True, min_value=0, precision=8)
