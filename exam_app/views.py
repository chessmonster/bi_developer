from django.urls import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import test_tableForm
from .models import test_table
from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from django.views.generic import TemplateView
from .models import Package
from django.db import connection

class test_tableList(ListView):
    model = test_table
    paginate_by = 20


class test_tableCreate(CreateView):
    model = test_table
    form_class = test_tableForm
    success_url = reverse_lazy('exam_app:list')


class test_tableDetail(DetailView):
    model = test_table


class test_tableUpdate(UpdateView):
    model = test_table
    form_class = test_tableForm
    success_url = reverse_lazy('exam_app:list')


class test_tableDelete(DeleteView):
    model = test_table
    success_url = reverse_lazy('exam_app:list')

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Packages delivered per leadtime (days)"] 
            # , "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        results = []
        with connection.cursor() as cursor:
            cursor.execute('''

                select 'within 1 day' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 0.001 and 1
                union all
                select 'within 2 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 1.001 and 2
                union all
                select 'within 3 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 2.001 and 3
                union all
                select 'within 4 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 3.001 and 4
                union all
                select 'within 5 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 4.001 and 5
                union all
                select 'within 6 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 5.001 and 6
                union all
                select 'within 7 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 6.001 and 7

                ''')

            results = cursor.fetchall()

        print(results)

        count = Package.objects.count()

        return [[   round((results[0][1] / count) * 100,2)
                ,   round((results[1][1] / count) * 100,2)
                ,   round((results[2][1] / count) * 100,2)
                ,   round((results[3][1] / count) * 100,2)
                ,   round((results[4][1] / count) * 100,2)
                ,   round((results[5][1] / count) * 100,2)
                ,   round((results[6][1] / count) * 100,2)
                ]]
                # ,
                # [41, 92, 18, 3, 73, 87, 92],
                # [87, 21, 94, 3, 90, 13, 65]]

line_chart = TemplateView.as_view(template_name='exam_app/question_one.html')
line_chart_json = LineChartJSONView.as_view()

class LineChartJSONViewGMA(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Packages delivered per leadtime (days)"] 
            # , "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        results = []
        with connection.cursor() as cursor:
            cursor.execute('''

                select 'within 1 day' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 0.001 and 1 and major_region = 'GMA'
                union all
                select 'within 2 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 1.001 and 2 and major_region = 'GMA'
                union all
                select 'within 3 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 2.001 and 3 and major_region = 'GMA'
                union all
                select 'within 4 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 3.001 and 4 and major_region = 'GMA'
                union all
                select 'within 5 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 4.001 and 5 and major_region = 'GMA'
                union all
                select 'within 6 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 5.001 and 6 and major_region = 'GMA'
                union all
                select 'within 7 days' as leadtime ,count(id) as 'day' from exam_app_package where leadtime between 6.001 and 7 and major_region = 'GMA'

                ''')

            results = cursor.fetchall()

        print(results)

        count = Package.objects.filter(major_region='GMA').count()
        print(count)

        return [[   round((results[0][1] / count) * 100,2)
                ,   round((results[1][1] / count) * 100,2)
                ,   round((results[2][1] / count) * 100,2)
                ,   round((results[3][1] / count) * 100,2)
                ,   round((results[4][1] / count) * 100,2)
                ,   round((results[5][1] / count) * 100,2)
                ,   round((results[6][1] / count) * 100,2)
                ]]

line_chart_gma = TemplateView.as_view(template_name='exam_app/question_one_gma.html')
line_chart_json_gma = LineChartJSONViewGMA.as_view()

class PackagePerMajorRegion(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["GMA","Luzon","Mindanao","Visayas"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Total packages per major region"] 
            # , "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        results = []
        with connection.cursor() as cursor:
            cursor.execute('''
                select major_region, count(id)
                from exam_app_package
                group by major_region
                ''')

            results = cursor.fetchall()

        print(results)

        return [[   results[0][1]
                ,   results[1][1]
                ,   results[2][1]
                ,  results[3][1]
                ]]

line_chart_package_major_region = TemplateView.as_view(template_name='exam_app/question_one_package_major_region.html')
line_chart_json_package_major_region = PackagePerMajorRegion.as_view()

class PackagePerMajorRegion(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["GMA","Luzon","Mindanao","Visayas"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Total packages per major region"] 
            # , "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        results = []
        with connection.cursor() as cursor:
            cursor.execute('''
                select major_region, count(id), avg(leadtime)
                from exam_app_package
                group by major_region
                ''')

            results = cursor.fetchall()

        print(results)

        
        return [[  results[0][1]
                ,  results[1][1]
                ,  results[2][1]
                ,  results[3][1]
                ]]

line_chart_package_major_region = TemplateView.as_view(template_name='exam_app/question_one_package_major_region.html')
line_chart_json_package_major_region = PackagePerMajorRegion.as_view()

class PackagePerMajorRegionAvg(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["GMA","Luzon","Mindanao","Visayas"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Total packages per major region"] 
            # , "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        results = []
        with connection.cursor() as cursor:
            cursor.execute('''
                select major_region, count(id), avg(leadtime)
                from exam_app_package
                group by major_region
                ''')

            results = cursor.fetchall()

        print(results)

        
        return [
                [results[0][1],  results[1][1],  results[2][1],  results[3][1]],
            ]

line_chart_package_major_region_avg = TemplateView.as_view(template_name='exam_app/question_one_package_major_region_avg.html')
line_chart_json_package_major_region_avg = PackagePerMajorRegionAvg.as_view()

class PackagePerMajorRegionAvgTime(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["GMA","Luzon","Mindanao","Visayas"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Average Leadtime"] 
            # , "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        results = []
        with connection.cursor() as cursor:
            cursor.execute('''
                select major_region, count(id), avg(leadtime)
                from exam_app_package
                group by major_region
                ''')

            results = cursor.fetchall()

        print(results)

        
        return [
                [results[0][2],  results[1][2],  results[2][2],  results[3][2]],
            ]

line_chart_json_package_major_region_avg_time = PackagePerMajorRegionAvgTime.as_view()