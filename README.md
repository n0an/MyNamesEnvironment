# MyNamesEnvironment

## Workflow

### Collecting source data
1. Collect ENG names data using parser. Collect name, description, gender, URL.
- Use:
  - Datacol parser.
  - Last working examples:
    * lotr4.par
    * lotr4-eng.par
- Configure:
  - Name, description, gender to collecting fields.
  - Datacol collecting URL automatically .

### Processing collected data
2. For every ENG URL, collect corresponding RUS data (name, description, URL) if it can be found.
- Use:
  - **get_links_from_web.py**
- Configure:
  - **cell_start_number**
  - **cell_end_number**
- Source: **sourcetableStage1.xlsx**
- Result: **resulttableStage1.xlsx** (with added RUS data)

3. Transfer data from *resulttableStage1.xlsx* to *TemplateTable.xlsx*:
- Correct column 'C' - specify correct gender. If there's race - concatenate race + gender. For example
  - **HobbitMasc** - if it's hobbits race
  - **Masc** - no race
- Correct cell 'N3'. Use format: *'category ID'.'gender ID.'*. For example:
  - **02.02.0.** - Fiction.Tolkien.Masc.
- Correct cell 'O3'. Specify *'.race ID'*. If there's no race, delete cell content. For example:
  - **.03**
 - Enumerate column 'A' according to names list count
 - Save table as **sourceTableStage2.xlsx** to scripts directory. Delete resulttableStage1.xlsx

 4. Use script to fill imageName column in names sourceTableStage2 table:
 - Use:
   - **workbookDiacriticRemover.py**
 - Configure:
   - **cell_start_number**
   - **cell_end_number**
- Source: **sourceTableStage2.xlsx**
- Result: **DoneTable.xlsx** (with imageName filled to column 'F' for every name). Delete sourceTableStage2.xlsx

### Collecting images for names
5. Collect images for names using script
- Use
  - **getImages.py**
- Configure:
  - **cell_start_number**
  - **cell_end_number**
  - **macos** = True/False
  - **dirPath** - path where save parsed from URLs images
- Source: **DoneTable.xlsx**
- Result: names images loaded and saved to *dirPath* using correct image names.
6. Move *DoneTable.xlsx* to SourceTables storage directory. Rename file using template:
- 'CategoryAliasGenderRace.xlsx' - if there's race
- 'CategoryAliasGender.xlsx' - no race
7. Move parsed images from *dirPath* to NamesImages storage directory.
8. Copy column 'G' and column 'L' contens to Xcode project as plists.
- In Xcode create 2 plists, named as 'CategoryAliasGender.plist' or 'CategoryAliasGenderRace.plist'
- Localize created plists - enable Eng and Rus localizations.
- Copy column contents to standard MacOs Notes.
- Then copy from Notes to Xcode. This action removes unnecessary quotes symbols.
- 'G' - ENG plist. 'L' - RUS plist
9. Upload names images using simulator, working directory.
- Configure ANViewController uploadUsingFileManager() method
  - Specify correct **pathName**. It will be used as directory name in Firebase Storage
  - Edit **fullFileName** prefix checking clause. It's preventing from uploading images from other category ang gender
- Copy images to **!toUpload/** directory of simulator working directory. And press the **Upload** button.
