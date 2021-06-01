## axiom/docker-erddap

### everyday stuff
```bash
# (hereon assuming docker container name = erddap)

# see stderr logs from entrypoint
docker logs erddap

# see logs.txt
docker exec -it erddap cat /erddapData/logs/log.txt.previous
```

### datset setup
```bash
# generate xml chunk for datasets.xml
docker exec -it erddap bash -c "cd /usr/local/tomcat/webapps/erddap/WEB-INF && bash GenerateDatasetsXml.sh -verbose"

# test loading of a dataset from datsets.xml (eg w/ dasaset ID = OC_2a67_61be_9fd6)
docker exec -it erddap bash -c "cd /usr/local/tomcat/webapps/erddap/WEB-INF/ && bash DasDds.sh OC_2a67_61be_9fd6"
```

### config 
```
# see amount of memory allowed by ERDDAP (for debug OutOfMemoryError)
docker exec -it erddap cat /usr/local/tomcat/bin/setenv.sh
```
