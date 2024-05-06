module "custom-web-server" {
  source = "../modules/custom_instance"
  instance_name = "tf-module-int"
  instance_type = "t2.nano"
}