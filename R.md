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

# logging
```R
library(logger)

# set log threshold
log_threshold(TRACE) 

# log functions:
log_trace("TRACE")
log_debug("DEBUG")
log_info("INFO")
log_success("SUCCESS")
log_warn("WARN")
log_error("ERROR")
log_fatal("FATAL")
```

# project setup
```R
# list dependencies
installed.packages()

# add a dependency to DESCRIPTION
usethis::use_package("dggridR")  # from CRAN
usethis::use_dev_package("robis", remote="iobis/robis")  # from github
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
devtools::install_local()  # <- alternative
```

## editing DESCRIPTION file
"author" types (full list [here](https://www.loc.gov/marc/relators/relaterm.html)):
* cre: the creator or maintainer - the current maintainer, even if they are not the initial creator of the package.
* aut: authors, those who have made significant contributions to the package.
* ctb: contributors, those who have made smaller contributions, like patches.
* fnd: funder, the people or organizations that have provided financial support for the development of the package.

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

# Install latest RStudio (ubuntu)
```
sudo apt install libnss3
tylar@LAPTOP-ESK3B866:~/obisindicators$ wget https://download1.rstudio.org/desktop/bionic/amd64/rstudio-2022.02.1-461-amd64.deb
tylar@LAPTOP-ESK3B866:~/obisindicators$ sudo apt install ./rstudio-2022.02.1-461-amd64.deb
```
