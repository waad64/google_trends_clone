from django.shortcuts import render
from pytrends.request import TrendReq
from .models import SearchQuery

def index(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')
        location = request.POST.get('location')
        
        # Save the search query to the database
        search_query = SearchQuery.objects.create(keyword=keyword, location=location)
        search_query.save()
        
        pytrend = TrendReq()
        pytrend.build_payload(kw_list=[keyword], geo=location)
        data = pytrend.interest_over_time()
        context = {'data': data.to_html()}
        return render(request, 'trends/results.html', context)
    return render(request, 'trends/index.html')
def results(request):
    # This view doesn't need to handle any logic, as the data has already been fetched in the index view
    return render(request, 'trends/results.html')
