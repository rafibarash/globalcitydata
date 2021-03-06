from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponse
from .models import DataSet
from .forms import QueryForm, SearchForm, DatasetSubmitForm
from .filters import DataFilter


def detailView(request, slug):
    dataset = get_object_or_404(DataSet, slug=slug)
    return render(request=request, template_name='data/dataset/detail.html', context={'dataset': dataset})


def homeView(request):
    if request.method == 'POST':
        # Form was submitted
        if 'search' in request.POST:
            queryForm = QueryForm()
            searchForm = SearchForm(request.POST)
            if searchForm.is_valid():
                data_filter = DataFilter(cd=searchForm.cleaned_data)
                datasets = data_filter.search()
                submitted = True
        elif 'query' in request.POST:
            queryForm = QueryForm(request.POST)
            searchForm = SearchForm()
            if queryForm.is_valid():
                dataset_filter = DataFilter(cd=queryForm.cleaned_data)
                datasets = dataset_filter.getData()
                submitted = True
    else:
        queryForm = QueryForm()
        searchForm = SearchForm()
        datasets = set(DataSet.published.all())
        submitted = False
    return render(request=request, template_name='data/dataset/home.html', context={'datasets': datasets,
                                                                                    'queryForm': queryForm,
                                                                                    'searchForm': searchForm,
                                                                                    'submitted': submitted})


def submitDatasetView(request):
    if request.method == 'POST':
        datasetSubmitForm = DatasetSubmitForm(request.POST)
        if datasetSubmitForm.is_valid():
            datasetSubmitForm.save()
            return redirect('data:success')
    else:
        datasetSubmitForm = DatasetSubmitForm()
    return render(request, 'data/dataset/datasetSubmit.html', {'datasetSubmitForm': datasetSubmitForm})


def successView(request):
    return render(request, 'data/dataset/success.html')
