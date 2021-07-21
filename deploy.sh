#!bin/bash
gcloud functions deploy dailyelectroset \
    --project=daily-electro \
    --trigger-topic dailyelectroset \
    --memory=256MB \
    --env-vars-file .env.yaml \
    --region=us-central1 \
    --runtime python39 \
    --entry-point=post_tweet