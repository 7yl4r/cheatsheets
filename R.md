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

# project setup
```R
# list dependencies
installed.packages() 
```
## install from github
```R
# install devtools, then use it
install.packages("devtools")
devtools::install_github('marinebon/obisindicators')
```

## Install dependencies from DESCRIPTION file:

```bash
# manual install devtools
Rscript -e 'if (!requireNamespace("devtools")) install.packages("devtools")'
# devtools on DESCRIPTION
Rscript -e 'devtools::install(pkg=".", quick=TRUE, quiet=TRUE, upgrade=TRUE)'
```

# File i/o
## excel
```R
library(readxl)
dat <- read_excel('location/of/excel/file.xlsx')
```

## .csv
```R
library(tidyverse)
statloc <- read_csv('data/statloc.csv')
```

# Install latest R (ubuntu) ([ref](https://askubuntu.com/a/436491/87936))
```bash
sudo add-apt-repository "deb http://cran.rstudio.com/bin/linux/ubuntu $(lsb_release -sc)-cran35/"
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository ppa:marutter/rdev
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install r-base
```
