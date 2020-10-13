from mongoengine import Document, DecimalField

class Amounts(Document):
    fee = DecimalField(required=True, min_value=0, precision=8)
    min_amount = DecimalField(required=True, min_value=0, precision=8)
    max_amount = DecimalField(required=True, min_value=0, precision=8)
