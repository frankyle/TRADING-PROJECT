# views.py
from rest_framework import generics, permissions
from .models import MgiCandles
from .serializers import MgiCandlesSerializer

class MgiCandlesListView(generics.ListCreateAPIView):
    queryset = MgiCandles.objects.all()
    serializer_class = MgiCandlesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MgiCandlesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MgiCandles.objects.all()
    serializer_class = MgiCandlesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MgiCandles.objects.filter(user=self.request.user)
