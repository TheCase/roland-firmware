# Roland ARIA Compact Firmware Summary

https://roland-firmware.repulsor.net/

scrapes the Roland website to create a quick summary HTML page with latest
Roland ARIA Compact firmware versions

Set the MODELS env var (comma separated string) with the models you'd like to track. Example:

```
services:
  roland_firmware:
    ...
    environment:
    - MODELS="jd-08,jx-08"
```


# to build with Kaniko in Kubernetes 

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
