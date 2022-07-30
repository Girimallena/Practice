import boto3
import json
ACCESS_KEY="AKIAVIGWAIF5ACVRY3CK"
SECRET_KEY="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"
AWS_REGION="us-east-1"


snsclient=boto3.client('sns',
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY,
                            region_name=AWS_REGION)

topic=snsclient.create_topic(Name="VsCode_test")
print(topic)
arn=topic['TopicArn']
proto='email'
End='girimallena1763@gmail.com'

def Subscribe(arn,proto,End):
    subscribe=snsclient.subscribe(
        TopicArn=arn,
        Protocol=proto,
        Endpoint=End,
        ReturnSubscriptionArn=True)['SubscriptionArn']

print(Subscribe(arn,proto,End))


# if __name__=="__main__":
#     app.run(debug=True)  