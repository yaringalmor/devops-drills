resource "aws_instance" "web-server" {
    ami = var.instance_ami
    instance_type = var.instance_type

    tags = {
        Name = var.instance_name
    }
}