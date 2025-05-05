from .user import User as UserResource
from .user import UserList as UserListResource
from .product import Product as ProductResource
from .product import ProductList as ProductListResource
from .order import Order as OrderResource
from .order import OrderList as OrderListResource
from .auth import Login as LoginResource, Register as RegisterResource
from .notification import Notification as NotificationResource, Notification_List as NotificationListResource
from .order_details import OrderDetails as OrderDetailResource, OrderDetailsList as OrderDetailListResource
from .rating import Rating as RatingResource, RatingList as RatingListResource
__all__ = [
    "UserResource",
    "UserListResource",
    "ProductResource",
    "ProductListResource",
    "OrderResource",
    "OrderListResource",
    "LoginResource",
    "RegisterResource",

]


