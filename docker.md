# CLI 
```bash
# stop all running containers
docker stop $(docker ps -q)

# find which container is using a volume
docker ps -a --filter volume=VOLUME_NAME_OR_MOUNT_POINT
```

# docker-compose
## volumes
```yaml
volumes:  # named volumes at top-level
   # named docker-managed volume
   volume_1_name:/dir/in/container/volume
   
   # named bind-mount
   my-named-mount:
     driver_opts:
           type: none
           device: /home/full/path  # needs full path
           o: bind  
           
    # named tmp-dir (for sharing btw containers)
    tmpfs_name:
        driver_opts:
            type: tmpfs
            device: tmpfs
            
container_title:
    volumes: 
      - /container/volume/path  # docker-managed volume
      
      - /my/bind/mount/path:/container/path  # bind mount to absolute host dir
      - ./my/relative/path:/container/path2  # bind mount to relative host dir
      
      - volume_1_name:/container/path  # named volume usage
      - my-named-mount:/container/path2  # named bind mount usage
      - tmpfs_name:/container/path3  # named tmpfs usage
```
