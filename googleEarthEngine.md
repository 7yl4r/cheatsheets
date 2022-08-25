``` javascript
// import function from a file:
var module_file_name = require('users/tylarmurray/repo_name:module_file_name');
module_file_name.function_name();

// export a function from a file:
exports.my_function_name = function(){
  print("running my_function_name...")
}
```

# imageCollection upload
0. create bucket in google cloud. suggested settings:
    * standard or nearline
    * single-zone 
2. [upload images to gcloud bucket using `gsutil`](https://cloud.google.com/storage/docs/gsutil/commands/cp#description)
3. [upload images to gee using `earthengine`](https://developers.google.com/earth-engine/guides/command_line#upload)
4. [collect together images into a collection in gee code editor](https://gis.stackexchange.com/a/427860/107752)
