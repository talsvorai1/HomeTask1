# HomeTask1
This project creates a CI/CD Jenkins pipeline, that fetches a simple web application from a GitLab repository, builds a docker image and runs a unittest.
When the artifact is approved it pushes it to ECR (Amazon Elastic Container Registry), and deploys the app in an EKS (Amazon Elastic Kubernetes Service) cluster via a remote EC2 instance.
