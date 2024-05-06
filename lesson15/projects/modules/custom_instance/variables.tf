variable "instance_type" {
  type = string
  default = "t2.micro"
  description = "web server instance type"
}

variable "instance_ami" {
  type = string
  default = "ami-0900fe555666598a2"
  description = "AMI"
}

variable "instance_name" {
  type = string
  description = "web-server name"
}