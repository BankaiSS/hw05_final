from django.core.paginator import Paginator

from yatube.settings import NUMBER_OF_POSTS


def paginate(request, data_list):
    paginator = Paginator(data_list, NUMBER_OF_POSTS)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
