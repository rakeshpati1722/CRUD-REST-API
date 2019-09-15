class a(APIViews):
    def get(self,request):
        a = quotemodel.objects.all()
        b = quoteSerializer(a, many= True)
        return Response(b.data)

class post(APIViews):
    def post(self,request):
        serializer_data = quoteSerializer(request.data)
        if serializer_data is_valid():
            serializer_data.save()
            return response(serializer_data.data,status=status.HTTP_200_OK)
        else:
            return response(serializer_data.data,staus=status_HTTP_400_OK)

# import urllib2
import urllib.request

class GenerateQuote(APIViews):
    def get(self,request):
        url = 'https://www.goodreads.com/'
        quote_from_good_read = urllib.request.urlopen(url)
        



