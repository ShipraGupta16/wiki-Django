import random
from . import util
from django.db import models
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader, Context
from django.core.files.base import ContentFile



class CreateWikiForm(forms.Form):
    title = forms.CharField(help_text="Title", max_length=100)
    description = forms.CharField(
        max_length=300,
        widget=forms.Textarea,
        help_text='Write here your message!'
    )

class EditWikiForm(forms.Form):
    title = forms.CharField(help_text="Title", max_length=100)
    description = forms.CharField(
        max_length=300,
        widget=forms.Textarea,
        help_text='Write here your message!'
    )
    fields = {
       'title',
       'description' 
    }

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def wikientry(request, name):
    if(util.get_entry(name) != None):
        return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(name),
        "name": util.get_entry_title(name)
        })
    else:
        return render(request, "encyclopedia/notfound.html")


def search(request):
    query = request.GET['q']
    context = Context({'query': query, }).flatten()
    if(util.get_entry_title(query) != None):
        return wikientry(request, query)
    else:
        return render(request, "encyclopedia/results.html", {
            "entries": util.search_filter(query),
            "query": query
        })    
    
def create(request):
    if request.method == "POST":
        form = CreateWikiForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            if util.get_entry_title(title) == None:
                util.save_entry(title, description)
                return wikientry(request, title)
            else:
                return render(request, 'encyclopedia/error.html')
        else:
            return render(request, 'encyclopedia/create.html', {'form': form}) 
    else:
        return render(request, 'encyclopedia/create.html', {
            "form": CreateWikiForm()
            })

def edit(request, name):
    formData = util.get_entry(name)
    initial = {
        "title": util.get_entry_title(name),
        "description": util.get_entry(name)
    }
    if request.method == "POST":
        form = EditWikiForm(request.POST, initial=initial)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            util.save_entry(title, description)
            return wikientry(request, title)
        else:
            return render(request, 'encyclopedia/error.html')
    else:
        form = EditWikiForm(initial=initial)
        args = {'form': form}
        return render(request, 'encyclopedia/edit.html', args)

def randomEntries(request):
    entries = util.list_entries()
    randomIndex = random.randint(0, len(entries)-1)
    return wikientry(request, entries[randomIndex])














