# MyNamesEnvironment

## Workflow

### Collecting source data

1. Collect ENG names data using parser. Collect name, description, URL.
2. For every ENG URL, collect corresponding RUS data (name, description, URL) if it can be found.
- Use:
  - **get_links_from_web.py**
- Configure:
  - **cell_start_number**
  - **cell_end_number**
- Source: **sourcetableStage1.xlsx**
- Result: **resulttableStage1.xlsx** (with added RUS data)
3. Transfer data from *sourcetableStage1.xlsx* to *TemplateTable.xlsx*:
- Correct column 'C' - specify correct gender. If there's race - concatenate race + gender. For example
  - **HobbitMasc** - if it's hobbits race
  - **Masc** - no race
- Correct cell 'N3'. Use format: *'category ID'.'gender ID.'*. For example:
  - **02.02.0.** - Fiction.Tolkien.Masc.
- Correct cell 'O3'. Specify *'.race ID'*. If there's no race, delete cell content. For example:
  - **.03**
 - Enumerate column 'A' according to names list count
 - Save table as **sourceTableStage2.xlsx** to scripts directory
 4. Use script to fill imageName column in names sourceTableStage2 table:
 - Use:
   - **workbookDiacriticRemover.py**
 - Configure:
   - **cell_start_number**
   - **cell_end_number**
- Source: **sourceTableStage2.xlsx**
- Result: **DoneTable.xlsx** (with imageName filled to column 'F' for every name).
5. Collect images for names using script
- Use
  -- **getImages.py**
- Configure:
  - **cell_start_number**
  - **cell_end_number**
  - **macos** = True/False
  - **dirPath** - path where save parsed from URLs images
- Source: **DoneTable.xlsx**
- Result: images loaded and saved to *dirPath* using correct image names.
6. Move *DoneTable.xlsx* to SourceTables storage directory. Rename file using template:
- 'CategoryAliasGenderRace.xlsx' - if there's race
- 'CategoryAliasGender.xlsx' - no race
7. Move parsed images from *dirPath* to NamesImages storage directory.
8. Copy column 'G' and paste to project as Eng plist and column 'L' as Rus plist.
9. Upload names images using simulator, working directory. Copy images to !toUpload/ directory and press Upload button.
  

