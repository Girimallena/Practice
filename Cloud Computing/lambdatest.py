import boto3
import json
ACCESS_KEY="AKIAVIGWAIF5ACVRY3CK"
SECRET_KEY="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"
AWS_REGION="us-east-1"

lambdaclient=boto3.client('lambda',
                            aws_access_key_id=ACCESS_KEY,
                            aws_secret_access_key=SECRET_KEY,
                            region_name=AWS_REGION)

payload={'email':['projectpro9@gmail.com','girimallena1763@gmail.com'],"arn":"arn:aws:sns:us-east-1:361226060154:VsCode_test"}
lambdaclient.invoke(
    FunctionName='Sample',
    InvocationType='Event',
    Payload=json.dumps(payload)
)