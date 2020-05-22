#!/bin/bash
export IMAGE_FAMILY="ubuntu-1604-lts"
export ZONE="asia-east1-a"
export INSTANCE_TYPE="n1-highcpu-16"
gcloud compute instances create $INSTANCE_NAMES \
        --zone=$ZONE \
        --image-family=$IMAGE_FAMILY \
        --image-project=ubuntu-os-cloud \
        --machine-type=$INSTANCE_TYPE \
        --boot-disk-size=200GB
