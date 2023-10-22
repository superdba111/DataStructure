### Summary

#### During the course of this project, I took the initiative to execute all function testing on my AWS account and, after numerous tests, everything ran smoothly.

#### Part 1-3: A Dive into AWS SageMaker
The initial three parts of the assignment were straightforward. In the practical scenario, we leverage AWS SageMaker services. One of the advantages is its compatibility with the s3a protocol, which simplifies data republishing to S3. Furthermore, AWS allows for easy scheduling of Jupyter notebook (.ipynb) files, streamlining the process for those seeking daily report generation.

#### Part 4: Exploring Terraform
For the fourth segment, my approach was primarily centered around Terraform. However, I did deviate slightly by utilizing deploy.sh specifically for the lambda 2 function deployment. To put this into a real-world context, usually after an initial setup on GitHub actions, there's no need to resort to deploy.sh. Everything becomes automated, further eliminating manual steps.

#### Areas for Enhancement:
I'll admit, there's room for improvement. One oversight on my part was hardcoding the S3 bucket name within the Python files. Ideally, this can be managed seamlessly with lambda environment variables designated for the S3 bucket name. There's potential for further refinement, either within the existing Terraform code, or by opting for tools like AWS CDK or CloudFormation. Interestingly, I've previously embarked on a similar mini-project using AWS CDK. For those interested, you can explore it here in my github. Yet, for this particular endeavor, focusing on Infrastructure as Code (IaC) automation, Terraform proved to be a convenient choice.

In conclusion, this assignment was not only an interview opportunity but also a chance to refine my AWS skills, particularly in the domain of automation and integration.




