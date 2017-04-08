### Main Workflow for creating data models

#### Contents:
- [Collecting source data](#collecting-source-data)
- [Collecting RUS data](#collecting-rus-data)
- [Processing collected data](#processing-collected-data)
- [Collecting images for names](#collecting-images-for-names)
- [Upload images to Firebase Storage](#transfer-data-from-donetablexlsx-to-xcode-plists-and-upload-images-to-firebase-storage)
- [Other scripts](#other-scripts)
- [Alternative workflow](#alternative-workflow-not-so-clean-and-correct)

**!!!IMPORTANT!!!**
Store all files in **!WORKFLOW** directory
Run all scripts MyNamesEnvironment directory:

```
iMac-Anton:MyNamesEnvironment antonnovoselov$ pwd
/Users/antonnovoselov/Documents/Development/Nickname generator wrap/MyNamesEnvironment

iMac-Anton:MyNamesEnvironment antonnovoselov$ python 07.\ Collect\ images/getImages.py
```

#### Collecting source data
1. Collect ENG names data using parser. Collect name, description, gender, URL.
- Use:
  - **Datacol parser**
  - Last working examples:
    * ~~lotr4.par~~ (DEPRECATED)
    * **lotr4-eng.par**
- Configure parser:
  - Name, description, gender to collecting fields.
  - Datacol collecting URL automatically.
- Result: Spreadsheet with Eng data. Name it **sourcetableStage1.xlsx**
- Rename sheet with data to 'sheet1'
- Put *sourcetableStage1.xlsx* to *!WORKFLOW* directory

#### Cellecting RUS data
2. For every ENG URL, collect corresponding RUS URL if it can be found.
- Use:
  - **get_links_from_web.py**
- Configure script:
  - **cell_start_number**
  - **cell_end_number**
- Source: **sourcetableStage1.xlsx**
- Result: **resulttableStage1.xlsx** (with added RUS URLs to column 'E')
- Delete *sourcetableStage1.xlsx*

3. For every RUS URL, collect corresponding RUS data (name, description, URL)
- Use:
  - **Datacol parser**
- Last working examples:
  - **lotr eng-rus from URLs.par**
- Source: Copy column E contents from **resulttableStage1.xlsx**
- Result: Spreadsheet with Rus data. It will be saved with name **lotr eng-rus from URLs** in MyDocuments directory

4. Add RUS data to sourcesheet
- In **resulttableStage1.xlsx** create new sheet **sourcesheet**
- Copy contents of **lotr eng-rus from URLs** to **sourcesheet** of the **resulttableStage1.xlsx**
- Use:
  - **proceed_ruslinks.py**
- Configure script:
  - *sheet1* sheet:
    - **cell_start_number**
    - **cell_end_number**
  - *sourcesheet* sheet:
    - **cell_source_start_number**
    - **cell_source_end_number**
- Source: **resulttableStage1.xlsx**
- Result: **resulttableStage2.xlsx** (with added RUS name to column 'G' and Rus bio to column 'H')
- Drag column E to column H (replace).  F - rus name, G - rus bio, H - rus url
- Delete *resulttableStage1.xlsx*

#### Processing collected data
5. Transfer data from *resulttableStage2.xlsx* to *TemplateTable.xlsx*:
- Correct column 'C' - specify correct gender. If there's race - concatenate race + gender. For example
  - **HobbitMasc** - if it's hobbits race
  - **Masc** - no race
- Correct cell 'N3'. Use format: *'category ID'.'gender ID.'*. For example:
  - **02.02.0.** - Fiction.Tolkien.Masc.
- Correct cell 'O3'. Specify *'.race ID'*. If there's no race, delete cell content. For example:
  - **.03**
 - Enumerate column 'A' according to names list count
 - Delete *resulttableStage2.xlsx*

 6. Use script to fill imageName column in names *TemplateTable.xlsx*:
 - Use:
   - **workbookDiacriticRemover.py**
 - Configure:
   - **cell_start_number**
   - **cell_end_number**
- Source: **TemplateTable.xlsx**
- Result: **DoneTable.xlsx** (with imageName filled to column 'F' for every name).

#### Collecting images for names
7. Collect images for names using script
- Use
  - **getImages.py**
- Configure:
  - **cell_start_number**
  - **cell_end_number**
  - **macos** = True/False
  - **dirPath** - path where save parsed from URLs images
- Source: **DoneTable.xlsx**
- Result: names images loaded and saved to *dirPath* using correct image names.

#### Transfer data from DoneTable.xlsx to Xcode Plists, and upload images to Firebase Storage
8. Copy column 'G' and column 'L' contents of **DoneTable.xlsx** to Xcode project as plists.
- In Xcode create 2 plists, named as 'CategoryAliasGender.plist' or 'CategoryAliasGenderRace.plist'
- Localize created plists - enable Eng and Rus localizations.
- Copy column contents to standard MacOS Notes.
- Then copy from Notes to Xcode. This action removes unnecessary quotes symbols.
- 'G' - ENG plist. 'L' - RUS plist
9. Upload names images using simulator working directory.
- Configure ANViewController uploadUsingFileManager() method
  - Specify correct **pathName**. It will be used as directory name in Firebase Storage
  - Edit **fullFileName** prefix checking clause. It's preventing from uploading images from other category and gender
- Copy images from *dirPath* to **!toUpload/** directory of simulator working directory. And press the **Upload** button.

10. Move *DoneTable.xlsx* to SourceTables storage directory. Rename file using template:
- 'CategoryAliasGenderRace.xlsx' - if there's race
- 'CategoryAliasGender.xlsx' - no race

11. Move parsed images from *dirPath* to NamesImages storage directory.

#### Other scripts
-- [OtherScripts](./OtherScripts.md)

#### Alternative workflow (not so clean and correct)
-- [ImagesFromHeap](./ImagesFromHeap.md) (DEPRECATED)
