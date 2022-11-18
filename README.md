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


## build amd/arm image
```
docker buildx build --platform linux/amd64,linux/arm64 -t thecase/roland-firmware:1.0.1 -t thecase/roland-firmware:latest . --push
```
