When creating/modifying database clusters and their supporting AWS infrastructure using Terraform and a GitOps methodology, you'll want to keep several important steps and considerations in mind. Here's a checklist to guide you through the process:

### Development Environment Setup:

Install Terraform in your development environment.
Install Git in your development environment.
Make sure you have the AWS CLI installed and correctly configured.

### AWS Credentials Setup:

Use AWS Identity and Access Management (IAM) to create a user with the appropriate permissions.
Configure your AWS credentials securely, such as via the AWS CLI, environment variables, or within your Terraform scripts using the aws provider.

### Git Repository Setup:

Create a new repository for your Terraform code.
Define and adhere to a branching strategy, such as GitFlow or GitHub Flow.
Define a clear directory structure for your Terraform modules and resources.

### Terraform Code:

Write Terraform code to create/modify your database clusters.
Modularize your code. For instance, write a separate module for your database cluster, VPC, Subnets, etc.
Make use of Terraform's resource targeting to ensure you're only modifying the resources you intend to.

### Terraform State Management:

Decide on a strategy for Terraform state management. In AWS, S3 buckets are commonly used for this purpose.
Enable state locking using DynamoDB to prevent concurrent state modifications.

### Testing:

Plan your changes using terraform plan to ensure the changes are what you expect.
Apply your changes in a test environment before applying them to production.

### Code Review:

Use Pull Requests to review changes to infrastructure code.
Use automated checks (like terraform fmt and terraform validate) to catch common issues.
Continuous Integration/Continuous 

### Deployment (CI/CD):

Configure a CI/CD pipeline for automated testing and deployment. Tools such as AWS CodePipeline, Jenkins, or GitHub Actions can be used for this.
Include a step in your pipeline to run terraform plan and output the results to a file that can be reviewed.

### Monitoring and Logging:

Set up monitoring and logging for your AWS resources using services like CloudWatch.
Monitor the logs of your CI/CD pipeline for any errors during the terraform apply step.

### Documentation:

Document your Terraform code and the overall infrastructure design.
Ensure to document how to use your modules, what inputs they need, and what they output.
Update README file with the instructions to setup, install, and use the application.

Remember, the overall goal of using a GitOps methodology is to use Git as the single source of truth for both your infrastructure and application code. Changes to infrastructure should be made through Git, and your actual environment should mirror what's in your Git repository.




