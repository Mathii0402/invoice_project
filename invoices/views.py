from rest_framework import generics
from .models import Invoice,InvoiceDetail
from .serializer import InvoiceSerializer,InvoiceDetailSerializer,Invoicenameserializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin

class InvoiceListCreateView(GenericAPIView,CreateModelMixin):
    queryset = Invoice.objects.all()
    serializer_class = Invoicenameserializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) 

class InvoiceListView(GenericAPIView,ListModelMixin):
    queryset = Invoice.objects.all()
    serializer_class = Invoicenameserializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
    

class InvoiceListDetCreateView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs) 

class CompleteInvoiceDetailView(GenericAPIView,ListModelMixin):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs) 
