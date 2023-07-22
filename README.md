<a id="readme-top"></a> 



<!-- PROJECT SUMMARY -->
<br />
<div align="center">
  <img src="https://yt3.googleusercontent.com/U6A3EBalyYYdPxevtxqQpdJWBCoAvw0gpI8WkkH-UWnsZUZt4kLYZ1hytYeB_h08Lki_LPpK=s176-c-k-c0x00ffffff-no-rj" alt="Logo">
  <br />
  <p align="center">
    A simple Reddit-based YouTube shorts video generator
    <br />
    <a href="https://www.youtube.com/@theredditgod"><strong>See Reddit GOD in action »</strong></a>
    <br />
    <br />
    <a href="#about-the-project">Getting Started</a>
    ·
    <a href="#basic-usage">Usage</a>
    ·
    <a href="https://github.com/Kieran-Lock/reddit-god/blob/main/LICENSE">License</a>
  </p>
</div>



<!-- ABOUT THE PROJECT -->
## About the Project

Reddit GOD is a simple YouTube shorts video generator, which uses the Reddit API to generate batches of videos, ready for immediate upload to YouTube.  
By using Natural Language Processing, Reddit GOD is capable of creating a video with a suitable title and description. It is also highly customizable, allowing for different video lengths, background footage, and video topics.  

_NOTE: Reddit GOD is now depracated due to the recent changes to Reddit's API._



<!-- GETTING STARTED -->
## Getting Started

To get started using Reddit GOD, clone this repository with:
```
git clone https://github.com/Kieran-Lock/reddit-god.git
```


Next, go to the [Reddit API](https://www.reddit.com/dev/api/), and follow [this guide](https://www.reddit.com/wiki/api/) to create an account. Take note of your generate Client ID and Client Secret!  
Also, ensure you have Python installed. This bot is tested with Python 3.11.  

Then, configure the following environment variables in your IDE:  
```
CLIENT_ID=<YOUR REDDIT API CLIENT ID>
CLIENT_SECRET=<YOUR REDDIT API CLIENT SECRET>
USER_AGENT=<A SUITABLE USER AGENT FOR WEB SCRAPING>
```
For our example, we used `Google:RedditGOD:v1.0.0 by Kieran-Lock` for the `USER_AGENT` environment variable. See more about user agents [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent).  

Lastly, add a background video (.mp4 file) to the root of the project, named `background.mp4`. We recommend this to be at least 20 minutes long - the longer the video, the better. This will be used as the background to each shorts video in random snippets.



<!-- BASIC USAGE EXAMPLES -->
## Basic Usage

To configure Reddit GOD, navigate to `main.py`, and adjust the global constants towards the top of the file. You can edit:
```py
SUBREDDIT_NAME = "AskReddit"  # The name of the subreddit thread to take posts from
NUMBER_OF_SUBMISSIONS = 5  # The number of videos to generate in one run
NUMBER_OF_COMMENTS = 4  # The number of comments to narrate in each generated video
NARRATOR_VOICE = Voices.ENGLISH_US_FEMALE  # The Text-To-Speech voice to use
```

You can now run the video generator with the following command (if python is installed correctly):
```py
python3 main.py
```

For the `NARRATOR_VOICE`, you can choose from the below options:
```py
class Voices(Enum):
    ENGLISH_US_FEMALE = "en_us_001"  # TikTok TTS Female
    ENGLISH_US_MALE = "en_us_006"  # TikTok TTS Male
    ENGLISH_US_MALE_NARRATOR = "en_male_narration"  # Narrator / Trailer Voice
    ENGLISH_UK_MALE_1 = "en_uk_001"  # UK Male Voice
```



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0 License. See [LICENSE](https://github.com/Kieran-Lock/reddit-god/blob/main/LICENSE) for further details.

<p align="right">(<a href="#readme-top">Back to Top</a>)</p>
