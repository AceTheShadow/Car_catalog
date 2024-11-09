from flask import Blueprint

blueprint = Blueprint(
    'country_blueprint',
    __name__,
    url_prefix='/admin/country'
)
