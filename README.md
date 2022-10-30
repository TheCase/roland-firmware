# Roland Hardware Firmware Summary

Docker image that scrapes the Roland website to create a quick summary HTML page with latest Roland hardware firmware versions.

I use the great open-source `changedecection.io` to poll the content for changes: https://github.com/dgtlmoon/changedetection.io


## Usage

Set the MODELS env var (comma separated string) with the models you'd like to track. Example:

```
services:
  roland_firmware:
    image: thecase/roland-firmware:latest
    ...
    environment:
    - MODELS="jd-08,jx-08"
```


## build image with Kaniko in Kubernetes 

1. must add a secret:

```
kubectl -n kaniko create secret \ 
docker-registry dockerhub-registry \
--docker-server=https://index.docker.io/v1/ \
--docker-username=<username> \
--docker-password=<token> \
--docker-email=<email>
```

2. Create pod from manifest

```
kubectl apply -f kaniko-builder.yaml
kubectl logs -n kaniko -f kaniko-builder 
```
