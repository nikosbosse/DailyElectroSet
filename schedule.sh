#!bin/bash
gcloud scheduler jobs create pubsub dailyelectroset \
    --project=daily-electro \
    --schedule="0 6 * * *" \
    --topic=dailyelectroset \
    --description="Post a daily electro set to @DailyElectroSet" \
    --message-body="Post a random set"