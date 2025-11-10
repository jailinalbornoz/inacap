from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm
from django.urls import reverse
from django.shortcuts import redirect


#rest_framework

from rest_framework import viewsets
from .serializers import ProductoSerializer
from rest_framework.permissions import IsAuthenticated

def home(request):
    return redirect('producto_list')

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, "core/producto_list.html", {"productos":productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, "core/producto_detail.html", {"producto":producto})

def producto_create(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("producto_list")
    else:
        form = ProductoForm()
    return render(request, "core/producto_form.html", {"form":form, "crear": True})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("producto_detail", pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, "core/producto_form.html", {"form":form, "crear": False, "producto": producto})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        producto.delete()
        return redirect("producto_list")
    return render(request, "core/producto_confirm_delete.html", {"producto": producto})


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated]