# A twitter bot that posts a random electro set every day

## Basic Setup (Twitter account, code)
The basic setup is very similar to the setup explained in detail [here](https://followtheargument.org/how-to-create-a-twitter-bot-that-posts-a-random-daily-article). Check out this tutorial in order to learn how to set up a Twitter developer account and what the different parts of the code do. 

A quick primer on how to parse a googlesheet, can be seen [here](https://stackoverflow.com/questions/61152242/how-to-obtain-data-from-a-public-google-sheets-using-python). 

<!-- 
The current version doesn't use SQL anymore
## Setting up the database
The data is stored in a Google Cloud MySQL database, but you can actually use any text file on your local machine as well. To learn more about how to set up a Google Cloud MySQL database, check [this](https://towardsdatascience.com/sql-on-the-cloud-with-python-c08a30807661) tutorial out.  -->

## Setting up the serverless bot
The tutorial I used to set up the serverless bot is [this one](https://www.cookieshq.co.uk/posts/how-to-build-a-serverless-twitter-bot-with-python-and-google-cloud)

For the deployment to work, you need to install the gcloud SDK command line interface on your local machine

First, you need to authenticate: 

```gloud auth login```

Then, development is done by sourcing the file deploy.sh. 
In order for this to work, you need to create a new file called .env.yaml that has the same content as the .env file, but in a .yaml format. For an overview of how that looks like, see [here](https://cloud.google.com/functions/docs/env-var). 

Before the deploy.sh script will work, you have to run schedule.sh and go throught the command line steps in order to configure the automatic schedule. Read more [here](https://cloud.google.com/scheduler/docs/tut-pub-sub).

The project in both schedule.sh and deploy.sh is the name of the project created in the Google Cloud Console. 
The entry point in schedule.sh is the function in main.py that will be executed (here it is post_tweet())

You can read error logs by running gcloud functions logs read --project=daily-electro (replace daily-electro with your project name)

For more infos on how to deploy, see [here](https://cloud.google.com/sdk/gcloud/reference/functions/deploy)

After deployment, you can test your function by triggering it [here](https://console.cloud.google.com/cloudscheduler?project=daily-electro&folder=&organizationId=).


## Acknowledgements
Inspiration for this project comes from [Sam Abbott's R Daily Cheat Sheet Bot](https://github.com/seabbs/TweetRstudioCheatsheets)

