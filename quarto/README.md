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

## modify _quarto.yml
Ensure the following is at the bottom of the file to apply my favorite settings:
```
format:
  html:
    theme: cosmo
    css: styles.css
    toc: true
    code-fold: true
    message: false
    warning: false
```

Add source code link to website.navbar.left:
```
      - href: https://github.com/marinebon/data_reports
        text: Source Code on GitHub
```
