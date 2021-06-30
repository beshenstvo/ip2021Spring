from ninja import NinjaAPI

from clean_burg.main.api.views import router as order_router

api = NinjaAPI(version="1.0.0", urls_namespace="internal_api", auth=None)

# Api
# ------------------------------------------------------------------------
api.add_router("/orders/", order_router)
# -----------------------------------------------------------------------
