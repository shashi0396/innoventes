provider "aws"{
   region= us-easr-2
)

resource "aws_instance""innventes_instance"{
   ami_id = "ami-12345"
   instance_tye = "t2.micro"
   availability_zone = "us-east-2a"
   key_name = "innoventes"
   vpc_security_group_id = [sg-12345]
   tags = {
    name = "innoventes"
   }
}

