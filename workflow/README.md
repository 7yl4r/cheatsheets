This is an attempt at flowchart-ifying all of my work functions in their most generic form.

```mermaid
graph TD

%% === node definitions =====================================================
init["create git repo"]
projectType{"specify end \n product goal"}
createPresentation["quarto+revealJS \n setup"]
createSpreadsheet[".csv spreadsheet \n report setup"]

%% === connections ==========================================================
init -->
projectType -- "live presentation" --> createPresentation
projectType -- "research report \n (ie: lit review, product search)" --> createSpreadsheet


%% === external links =======================================================
click createPresentation "https://github.com/7yl4r/cheatsheets/blob/master/workflow/live_presentation.qmd"
click createSpreadsheet "https://github.com/7yl4r/cheatsheets/blob/master/workflow/search_report.qmd"

%% === legend ===============================================================
subgraph Legend
    example{"human \n choice"} -- "selected choice option" --> B["checklist"]
end
```


reference materials
* quarto inspirations:
  * https://github.com/marinebon/MarineSDMs/tree/main
  * https://github.com/tbep-tech/shiny-workshop/tree/main
