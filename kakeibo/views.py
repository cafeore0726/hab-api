from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Record
from .serializers import RecordSerializer

class RecordPagination(PageNumberPagination):
    page_size = 5  # 1ページ5件表示

class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-recorded_at')
    serializer_class = RecordSerializer
    pagination_class = RecordPagination

@api_view(['GET'])
def budget_status(request):
    total = sum(record.amount for record in Record.objects.all())
    status = "黒字" if total >= 0 else "赤字"
    return Response({"total": total, "status": status})
