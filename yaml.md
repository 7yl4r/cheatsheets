```yaml
# === yaml DRY anchors in docker
# [ref]( https://medium.com/@kinghuang/docker-compose-anchors-aliases-extensions-a1e4105d70bd )
- &flag Apple
- Beachball
- Cartoon
- Duckface
- *flag    # this is also Apple

services:
  # Node.js gives OS info about the node (Host)
  nodeinfo: &function
    image: functions/nodeinfo:latest
    labels:
      function: "true"
  # Uses `cat` to echo back response, fastest function to execute.
  echoit:
    <<: *function
```
