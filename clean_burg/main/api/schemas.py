from ninja import Schema


class CreateOrderSchema(Schema):
    client_id: int
    client_name: str
    client_phone: str
    client_comment: str


class UpdateOrderSchema(Schema):
    client_name: str
    client_phone: str
    client_comment: str


class GetOrderSchema(Schema):
    id: int
    client_id: int
    client_name: str
    client_phone: str
    client_comment: str
