from django.shortcuts import render
from django.views.generic import DetailView

from hotel_reservation.models import Pokoj, Vybaveni
def index(request):

  num_pokoj = Pokoj.objects.all().count()
  pokoje = Pokoj.objects.order_by('poschodi')
  vybaveni = Vybaveni.objects.all()
  context = {
  'num_pokoj': num_pokoj,
  'pokoje': pokoje,
  'vybaveni': vybaveni
 }
  return render(request, 'index.html', context=context)



class RoomDetailView(DetailView):
    model = Pokoj
    context_object_name = "room_detail"
    template_name = "rooms/detail.html"

