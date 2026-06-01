# Serverless Text-to-Audio Processing Pipeline
This real-time event-driven microservice built on AWS  automatically converts flat text files (`.txt`) into high-quality MP3 audio files using Python and the AWS Boto3 SDK.

## Planned Architecture
This project is designed to be 100% serverless and cost effective while maintaining high avalibility. 

* **Storage:** Amazon S3 (Ingestion & Delivery)
* **Compute:** AWS Lambda (Python)
* **AI synthesis:** Amazon Polly (Text-to-speech Engine)
* **Security:** AWS IAM (Principle of Least Privvelage exe Role)
---

## Implementation Progress Tracker

### Phase 1: Manual Ingestion Architecture
* [X] Step 1: Initialize Project Directory & Git Tracking (Local)
* [X] Step 2: Provision S3 Storage Bucket (AWS Console) (You will need create your own s3 bucket )
* [X] Step 3: Configure Security Boundaries & IAM Execution Role (AWS Console)
* [ ] Step 4: Deploy Serverless Compute Core & Python Code (AWS Lambda)
* [ ] Step 5: Wire S3 Object-Creation Trigger (AWS Automation)
* [ ] Step 6: Execute Live End-to-End Pipeline Verification Test
* [ ] Step 7: Finalize Phase 1 Build Log & Sync to GitHub

### Phase 2: Infrastructure as Code (IaC) Migration 🚀
* [ ] Step 8: Destroy Phase 1 Console Resources to Prevent AWS Drift
* [ ] Step 9: Configure Terraform AWS Provider & State File Parameters
* [ ] Step 10: Translate IAM Roles & Managed Policies into `iam.tf`
* [ ] Step 11: Translate S3 Configuration into `s3.tf`
* [ ] Step 12: Package Python Source Code & Define `lambda.tf` Resource Mapping
* [ ] Step 13: Execute `terraform apply` to Provision the Entire Pipeline in One Command
---

## 🛠️ Step-by-Step Build Log

### Step 1: Initialize Workspace (Local Windows PC)
* **Status:** COMPLETE
* **Notes:** ### Step 2: Provision Cloud Storage (Amazon S3)
* **Status:** COMPLETE
* **Bucket Name:** `[Your Bucket Name Here]`
* **Notes:** ### Step 3: Configure IAM Security Boundary
* **Status:** COMPLETE
* **Role Name:** `[Your Role Name Here]`
* **Attached Policies:** `AmazonPollyFullAccess`, `AWSLambdaBasicExecutionRole`
* **Notes:** ### Step 4: Deploy Serverless Function Logic (AWS Lambda)
* **Status:** PENDING
* **Function Name:** `ConvertTextToAudio`
* **Runtime:** Python 3.12
* **Notes:** ### Step 5: Wire the Ingestion Trigger
* **Status:** PENDING
* **Trigger Source:** S3 Bucket Event (`s3:ObjectCreated:*`)
* **Notes:** ---

## 🎯 Verification & Testing Results

* **Status:** PENDING
* **Test File Name:** `speech_test.txt`
* **Resulting Asset:** `speech_test.mp3`
* **Log Diagnostics:** (Paste any interesting CloudWatch log findings or print statements here)