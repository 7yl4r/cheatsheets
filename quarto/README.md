# setup
## RStudio new quarto website
```
mkdir newRepo
cd newRepo
quarto create-project --type website
git add _quarto.yml about.qmd index.qmd styles.css

quarto render && quarto preview
quarto publish
```

##  add .gitignore
```
*csv

.Rproj.user
*.Rproj
.Rhistory
.RData
.Ruserdata

/.quarto/
*_cache/
*.cache/
*_files/
_site/*
```
##
