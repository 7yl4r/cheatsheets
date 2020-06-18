```bash
# stop all running containers
docker stop $(docker ps -q)

# find which container is using a volume
docker ps -a --filter volume=VOLUME_NAME_OR_MOUNT_POINT
```
