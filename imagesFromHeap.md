# Getting name images from images heap (DEPRECATED)

### This workflow works good in case if there're multiple names have the same imageName.
### For example if in source table 'Ahill', and 'Ahilles' have the same imageName 'MythGreekMascAhill'

1. Prepare files using concatenation in Excel with template *'name'+':'+'imageName'*:
- **!fem_name_image_conc.txt**
- **!masc_name_image_conc.txt**

2. Parse images from the internet using ContentDownloader parser with following actions:
- 'Ссылки' tab
- Add links from source names table (F8)
- Click Run (F5)
- Wait till done.
- Copy all parsed links
- Go to 'Контент' tab
- Paste links in bottom pane (F8)
- Click Run (F5)
- Wait till done.
- Go to 'C:/content'
- Copy 'images' folder to !WORKFLOW directory
- Rename 'images' folder using template: *'CategoryAliasGender'+'SRCImages'*

2. Sort parsed images heap to separate folders named according to parsed names
- Use:
  - **sort_images_using_names.py**
- Configure script:
| Parameter     | Decription     |
| :------------- | :------------- |
| **input_file_name** | source file with 'name'+'imagename' concatenated |
| **dir_path** | where to create folders tree with sorted images |
| **images_source_dir** | source folder with images |
- Source: folder-heap with images
- Result: images sorted to directories named according to names
- Delete images heap folder

3. Select best images from sorted images folders tree
- Use:
  - **get_best_images.py**
- Configure script:
| Parameter     | Decription     |
| :------------- | :------------- |
| **dir_path** | location of source folders tree with sorted images |
| **target_path** | where to save selected best images |
| **check_dir_prefix** | check every folder in folder tree if it has this prefix |
- Source: images sorted to directories named according to names
- Result: best images selected and saved to **target_path**
- Delete folder tree with sorted images

4. Selected images are ready to upload to Firebase.
- Use steps **9**, **11** described in [README](./README.md)
