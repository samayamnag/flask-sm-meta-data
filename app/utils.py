from instance.config import Config
from flask import request
from app import babel


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(Config.LANGUAGES[0].keys())


def page_num():
    return int(request.args.get('page') or 1)


def per_page():
    return int(request.args.get('per_page') or 10)


def pagination_links(pagination, total_records):

    import math

    current_page = pagination.page
    last_page = int(math.ceil(total_records / pagination.per_page))

    return {
        "first": first_page_url(),
        "last": last_page_url(last_page),
        "prev": previous_page_url(current_page),
        "next": next_page_url(current_page, last_page),
    }


def pagination_meta_data(pagination, total_records):

    import math

    current_page = pagination.page
    from_record = pagination_first_item(pagination)
    last_page = int(math.ceil(total_records / pagination.per_page))

    return {
        "current_page": current_page,
        "from": from_record,
        "last_page": last_page,
        "path": request.base_url,
        "per_page": pagination.per_page,
        'to': pagination_last_item(pagination),
        "total": total_records
    }


def pagination_first_item(pagination):
    return (pagination.page - 1) * pagination.per_page + 1


def pagination_last_item(pagination):
    return pagination_first_item(pagination) + len(pagination.items) - 1


def first_page_url():
    return 1


def next_page_url(current_page, last_page):
    if last_page > current_page:
        return current_page + 1


def previous_page_url(current_page):
    if current_page > 1:
        return current_page - 1


def last_page_url(last_page):
    return last_page
