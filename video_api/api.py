import os
# Cron Job
from django_cron import CronJobBase, Schedule



import apiclient

from .models import *
from videos import settings
from datetime import datetime, timedelta




class YoutubeApi(CronJobBase):
    RUN_EVERY_MINS = 1 #for async fetching

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'video_api.call_youtube_api'    # a unique code

    def callapi(self):
        apiKeys = settings.GOOGLE_API_KEYS
      
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=5)
     
        
        #####################################################

       

        for apiKey in apiKeys:
            try:
                youtube = apiclient.discovery.build("youtube", "v3", developerKey=apiKey)
               
                req = youtube.search().list(q="football", part="snippet", order="date", maxResults=50,
                                            publishedAfter=(last_request_time.replace(microsecond=0).isoformat()+'Z'))
                res = req.execute()
               
                print(res)
                valid = True
                print(apiKey)
              
            except apiclient.errors.HttpError as err:
                code = err.resp.status
                print("not working")
                if not(code == 400 or code == 403):
                    
                    break

            
        


        

          

            for item in res['items']:
                video_id = item['id']['videoId']
                publishedDateTime = item['snippet']['publishedAt']
                title = item['snippet']['title']
                description = item['snippet']['description']
                thumbnailsUrls = item['snippet']['thumbnails']['default']['url']
                channel_id = item['snippet']['channelId']
                channel_title = item['snippet']['channelTitle']
        
                Videos.objects.create(
                    video_id=video_id,
                    title=title,
                    description=description,
                    channel_id=channel_id,
                    channel_title=channel_title,
                    publishedDateTime=publishedDateTime,
                    thumbnailsUrls=thumbnailsUrls,
                )