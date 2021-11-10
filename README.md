# Youtube_API
To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Basic Requirements:
- Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes.
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- A basic search API to search the stored videos using their title and description.

# Instructions:
- You are free to choose any search query, for example official, cricket, football etc. (choose something that has a high frequency of video uploads)
- Try and keep your commit messages clean, and leave comments explaining what you are doing wherever it makes sense.
- Also try and use meaningful variable/function names, and maintain indentation and code style.
- Submission should have a `README` file containing instructions to run the server and test the API.
- Preferred language & Framework
    Python (DRF, Django, Flask)
# Reference:
- YouTube data v3 API: [https://developers.google.com/youtube/v3/getting-started](https://developers.google.com/youtube/v3/getting-started)
- Search API reference: [https://developers.google.com/youtube/v3/docs/search/list](https://developers.google.com/youtube/v3/docs/search/list)


# Setup:
- Clone the project
- Go the project through the terminal and install all dependencies by using typing `pip install -r requirements.txt`
- In the `setting.py` file, add api keys in the GOOGLE_API_KEYS list.

- Setup crontab to run Job
- Run cron using `python manage.py runcrons`
- Run the server using `python manage.py runserver`


