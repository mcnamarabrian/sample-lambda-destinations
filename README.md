# sample-lambda-destinations

The purpose of this project is to highlight how to use [Lambda Destinations]() using the Serverless Application Model.

# Deployment

## Install dependencies

The project has the following requirements:

* [AWS CLI version 2](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)

* [AWS SAM CLI (0.41.0 or higher)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Clone the repository

### Clone with SSH

```bash
git clone git@github.com:mcnamarabrian/sample-lambda-destinations.git
```

### Clone with HTTPS

```bash
git clone https://github.com/mcnamarabrian/sample-lambda-destinations.git
```

# Deploy the project

## Build the project

```bash
sam build --use-container
```

## Deploy the project

For the initial deploy, please use the `--guided` flag.  You will be prompted for an email address to receive success and failure notifications from the Lambda function.  Save the responses to the default `samconfig.toml` file.  Use the stack name `sample-lambda-destinations`.

```bash
sam deploy --guided
```

Subsequent deploys do not need the `--guided` flag.  They will utilize the responses provided in `samconfig.toml`. 

```bash
sam deploy
```

# Testing the project

## Gather relevant information from the CloudFormation stack

```bash
export FUNCTION_NAME=$(aws cloudformation describe-stack-resource --stack-name sample-lambda-destinations --logical-resource-id SimpleFunction --query "StackResourceDetail.PhysicalResourceId" --output text)
```

## Success

Test out a *success* event and confirm an email is via the SNS Topic **SuccessTopic**. 

```bash
aws lambda invoke --function-name ${FUNCTION_NAME} \
--invocation-type Event \
--payload '{"result": "success"}' \
response.json
```

## Failure

Test out a *failure* event and confirm an email is via the SNS Topic **FailureTopic**. 

```bash
aws lambda invoke --function-name ${FUNCTION_NAME} \
--invocation-type Event \
--payload '{"result": "failure"}' \
response.json
```

# Project cleanup

## Remove the CloudFormation stack

```bash
aws cloudformation delete-stack \
--stack-name sample-lambda-destinations
```

## Remove the associated CloudWatch Logs

```bash
for log_group in $(aws logs describe-log-groups --log-group-name-prefix '/aws/lambda/sample-lambda-destinations-' --query "logGroups[*].logGroupName" --output text); do
  echo "Removing log group ${log_group}..."
  aws logs delete-log-group --log-group-name ${log_group}
  echo
done
```
