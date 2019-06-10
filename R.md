```R
# function def
my_fn = function(
    param
){
    return(TRUE)
}

# load fn from file
source("my_file_w_fn_in_it.R")

# str manipulations
library(glue)
var1 <- 'foo'
var2 <- 'bar'
glue("{var1}_{var2}.rds")  # foo_bar.rds

# regex str replace
gsub("\ ", "_", "hello world ")  # hello_world_
```

