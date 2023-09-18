from django.shortcuts import render
from .graph import get_graph

def graph_view(request):
    # Get the graph
    graph = get_graph()

    # Render the graph to the template
    return render(request, 'graphs.html', {'graph': graph})