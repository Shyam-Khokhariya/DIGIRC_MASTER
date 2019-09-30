import pandas as pd
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import AddVehicleForm, AddVehicleFileForm
from django.contrib import messages
import os
import _csv
from django.core.paginator import Paginator






from django.shortcuts import render

from collections import OrderedDict
import numpy as np
from .fusioncharts import FusionCharts


# Loading Data from a Ordered Dictionary
# Example to create a column 2D chart with the chart data passed as Dictionary format.
# The `chart` method is defined to load chart data from Dictionary.




















app = settings.APP_NAME

auth = settings.FIREBASE.auth()

database = settings.FIREBASE.database()


def get_user(request):
    return request.session['user']


def get_user_details(request, context):
    if 'logged_status' in request.session:
        user = get_user(request)
        user_info = database.child('manufacturer').child(str(user['userId'])).child('profile').get()
        if user_info.val() is not None:
            for info in user_info.each():
                context.update({info.key(): info.val()})
    return context




def chart1(vehicles,context):
    dataSource = {}
    data=pd.DataFrame()
    for v in vehicles.each():
        # print(v.val())
        data=data.append(pd.DataFrame([v.val()]))
    # print(data.columns)
    # context['data1']=data
    # print(context['data1'])
    chartConfig = {
        "borderColor": "#ffffff",
        "bgColor":"#ffffff",
        "borderAlpha": "80",
        "theme":"fusion",
        "xAxisName":"Vehicle Type",
        "yAxisName":"Sales",
        "palettecolors":"#cbe86d,#a8d3ed,#ffcd8c,#ffabdd",

        "showRealTimeValue": "0",

    }


    # The `chartData` dict contains key-value pairs data
    chartData ={}

    u_body_type = data.body_type.unique()
    list_body_type=list(data.body_type)
    # print(u_body_type)
    for d in u_body_type:
        chartData[d]=list_body_type.count(d)
    # print(chartData)
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data1 = {}
        data1["label"] = key
        data1["value"] = value
        dataSource["data"].append(data1)

    column2D = FusionCharts("column2d", "ex", "100%", "120%", "chart-1", "json", dataSource)
    context['output']=column2D.render()
    # return (column2D.render())
    veh_chartConfig={
        "palettecolors": "#d9fcf8",
        "showLabels":"0",
        "showYAxisValues":"0",
        "showBorder":"0",
        "theme": "fusion",
        "showPlotBorder": "1",
        "drawFullAreaBorder": "0",
        "usePlotGradientColor": "2",
        "plotBorderThickness": "2",
        "plotBorderColor": "#00c0c0",
        "canvasPadding":"-50px",
        "showRealTimeValue": "0",
        "plotGradientColor":"#00ffe2"
      }
    total_vehicle1 = {}
    total_vehicle1["chart"] = veh_chartConfig
    total_vehicle1["categories"]=[{
          "category": [
          ]
        }]

    total_vehicle1["dataset"]=[{"data":[
        ]
    }
    ]
    total_vehicle1["data"] = []
    print(total_vehicle1["categories"][0]["category"])
    year=data.manufacture_year.unique()
    year.sort()
    total_vehicle1["categories"][0]["category"].append({"label":(str)(int(year[0])-1)})
    total_vehicle1["dataset"][0]["data"].append({"value": 0})
    # print(year)
    for y in year:
        total_vehicle1["categories"][0]["category"].append({"label":y})
    # print(total_vehicle["categories"][0]["category"])
    for d in year:
        total_vehicle1["dataset"][0]["data"].append({"value":list(data.manufacture_year).count(d)})

    chartObj1 = FusionCharts('stackedarea2d', 'ex1', '100%', '100%', 'Total_vehicle1', 'json', total_vehicle1)
    context['op_tot1'] = chartObj1.render()

    veh_chartConfig2 = {
        "palettecolors": "#ffd000",
        "showLabels": "1",
        "showYAxisValues": "1",
        "xAxisName":"Year",
        "yAxisName":"Number Of Vehicle Manufactured",
        "yAxisMinValue":"0",
        "xAxisMinValue":"0",
        "showBorder": "0",
        "theme": "fusion",
        "showPlotBorder": "1",
        "drawFullAreaBorder": "0",
        "usePlotGradientColor": "3",
        "plotBorderThickness": "2",
        "plotBorderColor": "#ff0303",
        "canvasPadding":"30",
        "showValues":"1",
        "showRealTimeValue": "0",
        "plotGradientColor": "#f7fa98"
    }
    total_vehicle1["chart"] = veh_chartConfig2
    chartObj2 = FusionCharts('stackedarea2d', 'ex2', '100%', '180%', 'Total_vehicle2', 'json', total_vehicle1)
    context['op_tot2']=chartObj2.render()
    growth=(total_vehicle1["dataset"][0]["data"][-1]["value"]-total_vehicle1["dataset"][0]["data"][-2]["value"])/total_vehicle1["dataset"][0]["data"][-2]["value"]
    context['Growth']=round(growth*100,2)


    print(data.status.unique())

    chartConfig = {
        "numberPrefix": "$",
        "defaultCenterLabel": "Total revenue: $64.08K",
        "centerLabel": "Revenue from $label: $value",
        "pieRadius":"40%",
        "labelDistance":"10px",
        "doughnutRadius":"200%",
        "enableSmartLabels":"1",
        "manageLabelOverflow":"1",
        "labelPosition":"Outside",
        "showPercentInToolTip":"1",
        "useEllipsesWhenOverflow":"1",
        "theme": "fusion"
    }

    # The `chartData` dict contains key-value pairs data
    chartData = {}
    u_body_type = data.body_type.unique()
    list_body_type = list(data.body_type)
    # print(u_body_type)
    for d in u_body_type:
        chartData[d] = list_body_type.count(d)
    # print(chartData)
    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    for key, value in chartData.items():
        data1 = {}
        data1["label"] = key
        data1["value"] = value
        dataSource["data"].append(data1)

    Dough = FusionCharts("doughnut2d", "do", "100%", "300%", "dough", "json", dataSource)
    context['op_dough'] = Dough.render()


class Dashboard(TemplateView):
    template_name = 'manufacturer/home.html'
    def get_context_data(self, **kwargs):
        user = get_user(self.request)
        vehicles = database.child('manufacturer').child(str(user['userId'])).child('vehicles').get()
        context = {'app': app, 'title': 'Dashboard'}
        chart1(vehicles,context)
        context.update(get_user_details(self.request, context))
        return context



def get_file_name(request, file_name):
    return request.FILES[file_name].name


def chassis_added(vehicle, user):
    vehicle_data = database.child('manufacturer').child(str(user['userId'])).child('vehicles').child(
        vehicle.get('chassis_no')).get()
    if vehicle_data.val() is not None:
        return True
    else:
        return False


def add_vehicle(request):
    form1 = AddVehicleForm()
    form2 = AddVehicleFileForm()
    if request.method == 'POST':
        if 'form1' in request.POST:
            form1 = AddVehicleForm(request.POST)
            if form1.is_valid():
                try:
                    vehicle = form1.save(commit=False)
                    vehicle = vehicle.__dict__
                    for key in ['_state', 'id']:
                        vehicle.pop(key)
                    user = get_user(request)
                    if chassis_added(vehicle, user):
                        messages.error(request, f'Chassis No Already Added')
                    else:
                        database.child('manufacturer').child(str(user['userId'])).child('vehicles').child(
                            vehicle.get('chassis_no')).set(vehicle)
                        form1 = AddVehicleForm()
                        messages.success(request, f'Saved Successfully')
                except:
                    messages.error(request, f'Error Occured')
            else:
                messages.error(request, f'Details are Invalid')
        elif 'form2' in request.POST and request.FILES['file']:
            form2 = AddVehicleFileForm(request.POST, request.FILES)
            if form2.is_valid():
                if str(get_file_name(request, 'file')).find('.csv') != -1:
                    try:
                        form2.save()
                        file_name = get_file_name(request, 'file')
                        path = os.path.join(settings.BASE_DIR, 'media') + '/datasheets/' + file_name
                        fields = list()
                        rows = list()
                        with open(path, 'r') as csvfile:
                            csvreader = _csv.reader(csvfile)
                            for row in csvreader:
                                rows.append(row)
                            for field in rows.pop(0):
                                fields.append(field)
                        data_list = list()
                        for row in rows:
                            data = dict()
                            for (key, value) in zip(fields, row):
                                data.update({key.strip(): value.strip()})
                            data_list.append(data)
                        user = get_user(request)
                        for vehicle in data_list:
                            database.child('manufacturer').child(str(user['userId'])).child('vehicles').child(
                                vehicle.get('chassis_no')).set(vehicle)
                        os.remove(path)
                        messages.success(request, f'Saved Successfully')
                    except:
                        messages.error(request, f'Error Occured')
                else:
                    messages.error(request, f'Datasheet is not in proper format')
            else:
                messages.error('Invalid File')
    context = {'app': app, 'title': 'Add Vehicle', 'form1': form1, 'form2': form2}
    context.update(get_user_details(request, context))
    return render(request, 'manufacturer/add.html', context)


class DisplayManufactured(TemplateView):
    template_name = 'manufacturer/manufactured_display.html'

    def get_context_data(self, **kwargs):
        user = get_user(self.request)
        vehicles = database.child('manufacturer').child(str(user['userId'])).child('vehicles').get()
        vehicles_list = list()
        if vehicles.val() is not None:
            for vehicle in vehicles.each():
                vehicles_list.append(vehicle.val())
        context = {'app': app, 'title': 'Display Vehicles'}
        context.update(get_user_details(self.request, context))
        paginator = Paginator(vehicles_list, settings.VEHICLE_COUNT)
        page = self.request.GET.get('page')
        vehicles = paginator.get_page(page)
        print(vehicles)
        context.update({'vehicles': vehicles})
        return context


class DisplayVehicleDetail(TemplateView):
    template_name = 'manufacturer/vehicle_display.html'

    def get_context_data(self, **kwargs):
        user = self.request.session['user']
        vehicles = database.child('manufacturer').child(str(user['userId'])).child('vehicles').get()
        context = {'app': app, 'title': 'Display Vehicles'}
        context.update(get_user_details(self.request, context))
        if vehicles.val() is not None:
            for vehicle in vehicles.each():
                if str(self.request.path).endswith(vehicle.key()):
                    context.update({'vehicle': vehicle.val()})
                    break
        return context
