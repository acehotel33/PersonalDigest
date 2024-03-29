import requests
import os

def fetch_nasa_pic(api_key):
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    # print(url)
    response = requests.get(url)
    if response.status_code == 200:
        nasa_pic_data = response.json()
        nasa_pic = {
            "description": nasa_pic_data['explanation'],
            "title": nasa_pic_data['title'],
            "url": nasa_pic_data['hdurl'],
        }
        print(nasa_pic)
        return nasa_pic
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None


if __name__ == '__main__':
    nasa_api_key = os.getenv('NASA_API_KEY')
    nasa_pic = fetch_nasa_pic(nasa_api_key)


# {"copyright":"\nJoe Hua\n",
# "date":"2024-03-27",
# "explanation":"Almost every object in the featured photograph is a galaxy.  The Coma Cluster of Galaxies pictured here is one of the densest clusters known - it contains thousands of galaxies.  Each of these galaxies houses billions of stars - just as our own Milky Way Galaxy does.  Although nearby when compared to most other clusters, light from the Coma Cluster still takes hundreds of millions of years to reach us.  In fact, the Coma Cluster is so big it takes light millions of years just to go from one side to the other.  Most galaxies in Coma and other clusters are ellipticals, while most galaxies outside of clusters are spirals.  The nature of Coma's X-ray emission is still being investigated.",
# "hdurl":"https://apod.nasa.gov/apod/image/2403/ComaCluster_Hua_960.jpg",
# "media_type":"image",
# "service_version":"v1",
# "title":"The Coma Cluster of Galaxies",
# "url":"https://apod.nasa.gov/apod/image/2403/ComaCluster_Hua_960.jpg"}