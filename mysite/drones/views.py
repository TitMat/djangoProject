from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Drone, Zone, Simulation
from .services import startSimulation


def index(request):
    all_drones_list = Drone.objects.order_by('-name')[:5]
    all_zones_list = Zone.objects.order_by('-name')[:5]
    all_simulations_list = Simulation.objects.order_by('-name')[:5]
    context = {'all_drones_list': all_drones_list, 'all_zones_list': all_zones_list,
               'all_simulations_list': all_simulations_list}
    return render(request, 'drones/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'drones/detail.html', {'question': question})

def detail(request, drone_id):
    drone = get_object_or_404(Drone, pk=drone_id)
    return render(request, 'drones/detail.html', {'drone': drone})


def simulate(request, simulation_id):
    simulation = get_object_or_404(Simulation, pk=simulation_id)
    setattr(simulation, 'bilan', startSimulation(simulation.Drone, simulation.Zone))
    simulation.save()
    return HttpResponseRedirect(reverse('drones:results', args=(simulation_id,)))


def results(request, simulation_id):
    simulation = get_object_or_404(Simulation, pk=simulation_id)
    return render(request, 'drones/results.html', {'simulation': simulation})


def preparesimu(request, simulation_id):
    simulation = get_object_or_404(Simulation, pk=simulation_id)
    return render(request, 'drones/preparesimu.html', {'simulation': simulation})
