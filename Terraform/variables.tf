variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "aws_access_key" {}
variable "aws_secret_key" {}

variable "key_name" {
  description = "Key pair name for SSH"
  default     = "nubela"
}

