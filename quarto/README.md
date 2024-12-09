## preferred .qmd header
```
----
code-fold: true
----
```

## Chunk metadata reference
Common metadata lines for chunks:
```R
#| label: myLabel
#| code-summary: sameAsMyLabel
#| message: false
#| warning: false
#| eval: true
```

# setup
## RStudio new quarto website
```bash
mkdir newRepo
cd newRepo
quarto create-project --type website
git add _quarto.yml about.qmd index.qmd styles.css

quarto render && quarto preview
quarto publish
```

##  add .gitignore
```gitignore
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


