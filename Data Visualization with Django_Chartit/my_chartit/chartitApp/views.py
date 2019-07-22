from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import SalesReport, MonthlyWeatherByCity, SalesHistory
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from django.db.models import Avg, Sum, Count, Min, Max

def home(request):
    first_graph = "My First django_chartit graph"
    return HttpResponse(first_graph)

def sales(request):
    sales =  DataPool(
           series=
            [{'options': {
            #    'source': SalesReport.objects.all()},
            'source': SalesReport},
            #'source': SalesReport.objects.filter(sales__lte=10.00)},
                'terms': [{'month': 'month',
                'sales': 'sales'}]
                },

       
             ]) 

    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        return names[month_num]         
    #Step 2: Create the Chart object
    cht = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': False},
                'terms':{
                  'month': [
                    'sales']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Sales Amounts Over Months'},
               'xAxis': {
                   'title':{'text': 'Sales Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
  
                   x_sortf_mapf_mts=(None, monthname, False))  
    #Step 3: Create a second chart object
    cht2 = Chart(
            datasource = sales,
            series_options =
              [{'options':{
                  'type': 'pie',
                  'plotBorderWidth': 1,
                  'zoomType': 'xy',
                 
                  'legend':{
                      'enabled': True,
                  }},
                  
                'terms':{
                  'month': [
                    'sales']
                  }}],
    
            chart_options =
              {'title': {
                   'text': 'Sales Amounts Over Months - Pie Chart'},
               'xAxis': {
                   'title':{'text': 'Sales Total'}},
               'yAxis': {
                   'title': {'text': 'Month Number'}},
                   
                'legend': {
                    'enabled': True},
                'credits': {
                    'enabled': True}},
                   
                   x_sortf_mapf_mts=(None, monthname, False))                      
    #Step 4: Send the chart object to the template.
    return render(request,'sales.html', 
        {'chart_list': [cht, cht2]})
    
                    




def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('weatherchart.html', {'weatherchart': cht})    


def citySales(request):
    ds = DataPool(
        series=[{
            'options': {
                'source': SalesHistory.objects.only(
                            'bookstore__city', 'sale_qty'
                          )[:10],
            },
            'terms': [
                'bookstore__city__region',
                'sale_qty'
            ]
        }]
)
    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'bar',
                'stacking': True,
                'stack': 0,
            },
            'terms': {
                'bookstore__city__region': [
                    'sale_qty'
                ]
            }},
        ],
        chart_options={
            'title': {
                'text': 'Sales reports'
            },
            'xAxis': {
                'title': {
                    'text': 'City'
                },
                'legend':{
                    "reversed": True,
                }

            }
        }
)
    return render_to_response('citySales.html', {'citySales': cht})


def weatherByCity(request):
    ds = DataPool(
        series=[{
            'options': {
                'source': MonthlyWeatherByCity.objects.all()
            },
            'terms': [
                'month',
                'boston_temp',
                'houston_temp'
            ]
        }]
)
    def monthname(month_num):
        names = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
             7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov',
             12: "Dec"}
        return names[month_num]

    cht = Chart(
        datasource=ds,
        series_options=[{
            'options': {
                'type': 'line'
            },
            'terms': {
                'month': ['boston_temp']
            }}, {
            'options': {
                'type': 'pie',
                'center': [150, 100],
                'size': '50%'
            },
            'terms': {
                'month': ['houston_temp']
            }}
        ],
        chart_options={
            'title': {
                'text': 'Weather Data of Boston (line) and Houston (pie)'
            }
        },
        x_sortf_mapf_mts=[(None, monthname, False),
                          (None, monthname, False)])   

    return render_to_response('weatherByCity.html', {'weatherByCity': cht})                      


def pivot(request): 

    ds = PivotDataPool(
      series=[
       {'options': {
          'source': SalesHistory.objects.all(),
          'categories': 'bookstore__city__city',
          },
        'terms': {
          'Max Books/Sale': Max('sale_qty'), 'Total Books Sold': Sum('sale_qty'),
          'Min Books/Sale': Min('sale_qty'), 'Total Sales $': Sum('price'),
          },          
       }])
    pivcht = PivotChart(
          datasource=ds,
          series_options=[
            {'options': {
               'type': 'bar'
               }, 
             'terms': ['Min Books/Sale','Max Books/Sale' ,'Total Books Sold', 'Total Sales $'],         
            }],
            chart_options={
            'title': {
                'text': 'Sales Data'
            },
             'subtitle': {
                'text': 'All Points',    
            },
            'legend': {
                'layout': 'vertical',
                'align': 'right',
                'verticalAlign': 'center',
                'x': -10,
                'y': 80,
                'floating': True,
                'borderWidth': 1,
                "backgroundColor": '#EEEEEE',
                'shadow': True,
                'reversed': True                
            },
            'plotOptions': {
                'bar': {
                    'dataLabels':{
                        'enabled': True
                    },
                    'pointPadding': 1,
                    'borderWidth': 10,
                    'borderRadius': 11               
                }   }, })                
                   
    return render_to_response('pivot.html', {'pivot': pivcht})                      
  