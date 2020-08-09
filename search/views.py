import traceback

from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from django.core.paginator import Paginator, Page, EmptyPage, PageNotAnInteger
from django.db.models.query import Q
from django.http import HttpResponse

from .documents import UniversityDocument
from .models import University


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class UniversityDetails(APIView):
    def get(self, request):
        try:
            get_data = request.GET
            search_value = get_data.get("search")
            page_number = request.GET.get("page")
            filter_by_code = get_data.get("filter_by_code")
            filter_by_code = filter_by_code \
                and filter_by_code.strip('][').split(',')
            filter_by_domain = get_data.get("filter_by_domain")
            filter_by_domain = filter_by_domain \
                and filter_by_domain.strip('][').split(',')
            query = Q()
            if search_value:
                query &= Q(name__icontains=search_value)
            if filter_by_code:
                query &= Q(alpha_two_code__in=filter_by_code)
            if filter_by_domain:
                domain_query = Q()
                for i in filter_by_domain:
                    domain_query |= Q(domain__endswith=i)
                query &= domain_query
            data = UniversityDocument.search().to_queryset().filter(query)
            paginator = Paginator(data, 10)
            try:
                page = paginator.page(page_number)
            except PageNotAnInteger:
                page = paginator.page(1)
            except EmptyPage:
                page = paginator.page(paginator.num_pages)
            return JSONResponse({
                "message": "Read Successful", 
                "data": page.object_list.values()
            })
        except Exception as e:
            print(e, traceback.format_exc())
            return JSONResponse({
                "message": "Something Went Wrong", 
                "data": {}
            })

    def post(self, request):
        try:
            post_data = request.data
            alpha_two_code = post_data.get("alpha_two_code")
            country = post_data.get("country")
            domain = post_data.get("domain")
            name = post_data.get("name")
            web_page = post_data.get("web_page")
            uni_object = University(
                alpha_two_code=alpha_two_code, 
                country=country, 
                domain=domain, 
                name=name, 
                web_page=web_page
            )
            uni_object.save()
            return JSONResponse({
                "message": "Successfully Created", 
                "data": {"id": uni_object.id}
            })
        except Exception as e:
            print(e, traceback.format_exc())
            return JSONResponse({
                "message": "Something Went Wrong", 
                "data": {}
            })

    def put(self, request):
        try:
            post_data = request.data
            uni_id = post_data.get("id")
            alpha_two_code = post_data.get("alpha_two_code")
            country = post_data.get("country")
            domain = post_data.get("domain")
            name = post_data.get("name")
            web_page = post_data.get("web_page")
            University.objects.filter(id=uni_id).update(
                alpha_two_code=alpha_two_code, 
                country=country, 
                domain=domain, 
                name=name, 
                web_page=web_page
            )
            return JSONResponse({
                "message": "Successfully Updated", 
                "data": {}
            })
        except Exception as e:
            print(e, traceback.format_exc())
            return JSONResponse({
                "message": "Something Went Wrong", 
                "data": {}
            })

    def delete(self, request):
        try:
            post_data = request.data
            uni_id = post_data.get("id")
            University.objects.filter(id=uni_id).delete()
            return JSONResponse({
                "message": "Successfully Deleted", 
                "data": {}
            })
        except Exception as e:
            print(e, traceback.format_exc())
            return JSONResponse({
                "message": "Something Went Wrong", 
                "data": {}
            })
