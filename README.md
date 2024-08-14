# s3-notifications-using-sns
Creating lambda function to get notifications on mail using sns based on s3 events.

Following are the steps:
1. Create a SNS Topic as follow -
   ![image](https://github.com/user-attachments/assets/758adba5-3468-4907-a5eb-a96baf4422b0)
2. Create a subscription in SNS Topic with Email protocol -
   ![image](https://github.com/user-attachments/assets/08dd3531-5f07-4bc7-86c4-bf9e89739d6b)
3. Create a S3 Bucket
   ![image](https://github.com/user-attachments/assets/97fcc2c9-db7c-4434-b722-31506bf79ce2)
4. Create a Lambda Function, Select Runtime - Python 3.9
    * Add Code in the function -
   ![image](https://github.com/user-attachments/assets/38d29ed7-67a5-49b7-a194-7962fcc04efa)

    * Create an Environment Variable(Lambda function -> Configurations -> Environment Variables -> Edit -> Add environment variable)
   ![image](https://github.com/user-attachments/assets/fd7b7295-f875-433c-8ce8-e6c53065ad89)

   * Add Trigger in Lambda function - S3 - Select bucket
   ![image](https://github.com/user-attachments/assets/0566fc60-5c64-4edf-92e4-b68683e3969a)

   * Add Following policy to the IAM Role of Lambda Function(Lambda function -> Configurations -> Permissions -> Execution role)
    ```
    {
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "arn:aws:sns:us-east-2:992382400837:SNSTopicForS3Notifications"
    }
    ```
   * Test the Lambda Function and Deploy.

5. Add Object in S3 Bucket
   ![image](https://github.com/user-attachments/assets/66b7567c-d8f1-4bc1-9134-7ced5456a5b6)
     <br>
     * Will get the mail like this -
       ![image](https://github.com/user-attachments/assets/4a83f50c-63a3-445d-baed-c67b82205abc)
6. Delete Object in S3 Bucket
   ![image](https://github.com/user-attachments/assets/e6e94e05-5d5e-412d-ac6e-a12a61a03a07)
     <br>
     * Will get the mail like this -
       ![image](https://github.com/user-attachments/assets/33c32e6d-b2be-4a55-a60f-c627c3c466ee)


  
  


   
