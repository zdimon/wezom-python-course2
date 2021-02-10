# Наборы форм. Formset.

Набор форм — это абстрактный слой для работы с множеством форм на одной странице. Его можно сравнить с таблицей данных.

Вы можете позволить пользователю создавать несколько объектов модели за один раз. 

Допустим у нас есть модель резюме.

    from django.db import models
    from django.contrib.auth.models import User


    class Cv(models.Model): 
        name = models.CharField(max_length=255)
        user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)


    class WorkExperience(models.Model):
        cv = models.ForeignKey(Cv, on_delete=models.CASCADE, blank=True)
        position = models.CharField(max_length=255, blank=True)
        company = models.CharField(max_length=255, blank=True)

    class Certification(models.Model):
        cv = models.ForeignKey(Cv, on_delete=models.CASCADE, blank=True)
        name = models.CharField(max_length=255, blank=True)
        provider = models.CharField(max_length=255, blank=True)

Мы связали одно резюме пользователя с друмя множествами моделей WorkExperience и Certification.

## Админ интерфейс.


    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals

    from django.contrib import admin
    from .models import *

    class WorkExperienceInine(admin.TabularInline):
        model = WorkExperience

    class CertificationAdmin(admin.TabularInline):
        model = Certification


    class CvAdmin(admin.ModelAdmin):
        list_display = ['name']
        inlines = [WorkExperienceInine, CertificationAdmin]

    admin.site.register(Cv, CvAdmin)

![start page]({path-to-subject}/images/1.png)

Как видно в админке мы уже имеем возможность с помощью набора форм создать сразу нескольколько объектов, привязанных к обьекту резюме.

Попробуем реализовать подобное на фронтенде.

### Создадим классы форм в forms.py.

    from django.forms import ModelForm
    from .models import *

    class CvForm(ModelForm):
        class Meta:
            model = Cv
            fields = ['name', 'user']

    class WorkExperienceForm(ModelForm):
        class Meta:
            model = WorkExperience#
            fields = ['cv', 'position', 'company']

    class Certification(ModelForm):
        class Meta:
            model = Certification
            fields = ['cv', 'name', 'provider']

## Передадим одну форму во вьюшке.

    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals

    from django.shortcuts import render
    from .forms import *

    def create_cv(request):
        form = CvForm()
        return render(request,'create_cv.html',{'form': form})

Роутинг.

    from django.conf.urls import url
    from django.contrib import admin
    from main.views import create_cv

    urlpatterns = [
        url(r'', create_cv),
        url(r'^admin/', admin.site.urls),
    ]



Шаблон.


    <html>
    <head></head>
    <body>
        <form action="" method="POST">
            {% csrf_token %}
            {{ form }}
            <input type="submit" value="Submit" />
        </form>
    </body>
    </html>

![start page]({path-to-subject}/images/2.png)

Теперь сохраним форму и переправим пользователя на другую вьюшку.

    
    ...
    def create_cv(request):
        form = CvForm(request.POST or None)
        if request.method == 'POST':
            cv = form.save()
            return HttpResponseRedirect(reverse('create_options', kwargs={'id':cv.pk}))
        return render(request,'create_cv.html',{'form': form})

    def create_options(request,id):
        cv = Cv.objects.get(pk=id)
        form = WorkExperienceForm()
        return render(request,'create_options.html', {'cv': cv, 'form': form})

Роутинг

    from django.conf.urls import url
    from django.contrib import admin
    from main.views import create_cv, create_options
    from django.urls import path

    urlpatterns = [
        path('', create_cv),
        path(r'create/options/<int:id>/', create_options, name='create_options'),
        url(r'^admin/', admin.site.urls),
    ]


Шаблон второй страницы.

        
    <html>
    <head></head>
    <body>
        <h1>Create options for {{ cv.name }}</h1>
        <form action="" method="POST">
            {{ form }}
            <input type="submit" value="Submit" />
        </form>
    </body>
    </html>

![start page]({path-to-subject}/images/2.png)

Теперь попробуем добавить несколько форм как набор.

    from django.forms.formsets import formset_factory

    def create_options(request,id):
        cv = Cv.objects.get(pk=id)
        expirience_formset = formset_factory(WorkExperienceForm, extra=2)
        return render(request,'create_options.html', {'cv': cv, 'expirience_formset': expirience_formset})

Шаблон.

    <html>
    <head></head>
    <body>
        <h1>Create options for {{ cv.name }}</h1>
        <form action="" method="POST">
            {% for form in expirience_formset %}
                {{ form.as_p }}
            {% endfor %}
            <input type="submit" value="Submit" />
        </form>
    </body>
    </html>

Заполним начальными значениям из объекта резюме.

    def create_options(request,id):
        cv = Cv.objects.get(pk=id)
        ExpirienceFormSet = formset_factory(WorkExperienceForm, extra=2)
        expirience_formset = ExpirienceFormSet(initial=[
              {'cv': cv }
         ])

![start page]({path-to-subject}/images/3.png)

Как видим заполнилась только первая форма и теперь их стало 3.

Изменим немного структуру и определим сохранение постом.


    if request.method == 'POST':
        expirience_formset = ExpirienceFormSet(request.POST)
        for form in expirience_formset:
            form.save()
    else:
        expirience_formset = ExpirienceFormSet(initial=[
            {'cv': cv },
            {'cv': cv }
        ])


При сохранении получили ошибку.

![start page]({path-to-subject}/images/4.png)

Необходимо было добавить в шаблон поля менеджера форм.

        ...
        {{ expirience_formset.management_form }}
        {% for form in expirience_formset %}
            {{ form.as_p }}
        {% endfor %}
        ...

При пересохранении добавляются дубликаты и не редактируются уже созданные записи.

Для этого попробуев ввести в форму идентификаторы.

    class WorkExperienceForm(ModelForm):
        id = forms.CharField(label='Id', max_length=100)
        class Meta:
            model = WorkExperience
            fields = ['cv', 'position', 'company', 'id']

Переопределим метод save.

    def save(self, commit=False, *args, **kwargs):
        m = super(WorkExperienceForm, self).save(commit=False, *args, **kwargs)
        if not m.id:
            ex = WorkExperience()
            ex.position = m.position
            ex.cv = m.cv
        else:
            ex = WorkExperience.objects.get(pk=m.id)
            ex.position = m.position

        ex.save()
        return ex.cv

Добавим объекты во вьюхе в формсет.

    def create_options(request,id):
        cv = Cv.objects.get(pk=id)
        objs = []
        for exp in WorkExperience.objects.filter(cv=cv):
            objs.append({'cv': exp.cv, 'position': exp.position, 'company': exp.company, 'id': exp.id})
        ExpirienceFormSet = formset_factory(WorkExperienceForm,extra=0)
        objs.append({'cv': cv})
        
        if request.method == 'POST':
            expirience_formset = ExpirienceFormSet(request.POST)
            for form in expirience_formset:
                if form.is_valid():
                    cv = form.save()
                    return HttpResponseRedirect(reverse('create_options', kwargs={'id':cv.pk}))
        else:
            expirience_formset = ExpirienceFormSet(initial=objs)

        return render(request,'create_options.html', {'cv': cv, 'expirience_formset': expirience_formset})




Выведем скрытые поля на форме.

        {% for form in expirience_formset %}
            {{ form.as_p }}
            {% for hidden in form.hidden_fields %}
                {{ hidden }}
            {% endfor %}
        {% endfor %}




