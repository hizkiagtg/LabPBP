from django.shortcuts import render
from wishlist.models import BarangWishlist

# Create your views here.
def show_wishlist(request):
    return render(request, "wishlist.html", context)

data_barang_wishlist = BarangWishlist.objects.all()
context = {
    'list_barang': data_barang_wishlist,
    'nama': 'Hizkia Sebastian Ginting'
}
