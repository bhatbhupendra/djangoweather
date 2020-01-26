from django.shortcuts import render

def home(request):
        import json
        import requests
        if request.method == "POST":
            zipcode=request.POST['zipcode']
            api_request=requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode='+ zipcode +'&distance=5&API_KEY=F3731176-AA0C-40FE-9FDA-B85A53950C69')
            try:
                api=json.loads(api_request.content)
            except Exception as e:
                api="Error..."

            if api[0]['Category']['Name'] == "Good":
                Category_Discription="Good (0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            elif api[0]['Category']['Name'] == "Moderate":
                Category_Discription="Moderate (51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                Category_Discription="Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            elif api[0]['Category']['Name'] == "Unhealthy":
                Category_Discription="Unhealthy (151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                Category_Discription="Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects."
            elif api[0]['Category']['Name'] == "Hazardous":
                Category_Discription="Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."


            return render(request, 'home.html', {'api':api,'Category_Discription':Category_Discription})

        else:
            api_request=requests.get('http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F3731176-AA0C-40FE-9FDA-B85A53950C69')
            try:
                api=json.loads(api_request.content)
            except Exception as e:
                api="Error..."

            if api[0]['Category']['Name'] == "Good":
                Category_Discription="Good (0 - 50) Air quality is considered satisfactory, and air pollution poses little or no risk."
            elif api[0]['Category']['Name'] == "Moderate":
                Category_Discription="Moderate (51 - 100) Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution"
            elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
                Category_Discription="Unhealthy for Sensitive Groups (101 - 150) Although general public is not likely to be affected at this AQI range, people with lung disease, older adults and children are at a greater risk from exposure to ozone, whereas persons with heart and lung disease, older adults and children are at greater risk from the presence of particles in the air."
            elif api[0]['Category']['Name'] == "Unhealthy":
                Category_Discription="Unhealthy (151 - 200) Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
            elif api[0]['Category']['Name'] == "Very Unhealthy":
                Category_Discription="Very Unhealthy (201 - 300) Health alert: everyone may experience more serious health effects."
            elif api[0]['Category']['Name'] == "Hazardous":
                Category_Discription="Hazardous (301 - 500) Health warnings of emergency conditions. The entire population is more likely to be affected."


            return render(request, 'home.html', {'api':api,'Category_Discription':Category_Discription})

def about(request):
    return render(request, 'about.html', {})
