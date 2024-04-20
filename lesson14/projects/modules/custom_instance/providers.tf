terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 5.0"
        }
    }
}

provider "aws" {
    region = "us-east-2"
    access_key = "AKIAVBOY4QDZWV45MCLQ"
    secret_key = "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"
}