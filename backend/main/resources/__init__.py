# Los Resources se exponen con alias *Resource; main/__init__.py los registra
# en la API con api.add_resource().
from .user import User as UserResource
from .user import UserList as UserListResource
from .product import Product as ProductResource
from .product import ProductList as ProductListResource
from .order import Order as OrderResource
from .order import OrderList as OrderListResource
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
    
    
    "NotificationResource","NotificationListResource",
    "OrderDetailResource","OrderDetailListResource",
    "RatingResource",
    "RatingListResource"

]


