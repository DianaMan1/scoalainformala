items_per_page = 10


def get_offset(page: int):
    return (page - 1) * 10


def get_items_per_page():
    return items_per_page


def get_pagination(metadata):
    total_pages = int(metadata['totalCount'] / items_per_page)

    is_there_a_last_page = metadata['totalCount'] / items_per_page % 1

    if is_there_a_last_page:
        total_pages = total_pages + 1

    current_page = int(metadata['currentOffset'] / items_per_page) + 1
    next_page = 1 if current_page == total_pages else current_page + 1
    previous_page = total_pages if current_page == 1 else current_page - 1
    is_first_page = current_page == 1
    is_last_page = current_page == total_pages

    return {
        'is_first_page': is_first_page,
        'is_last_page': is_last_page,
        'next_page': next_page,
        'previous_page': previous_page,
        'current_page': current_page,
        'total_pages': total_pages
    }
