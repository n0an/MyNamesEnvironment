# Getting name images from images heap (DEPRECATED)

1. Prepare files using concatenation in Excel:
- !fem_name_image_conc.txt
- !masc_name_image_conc.txt

2. Using ContentDownloader parser:
- 'Ссылки' tab
- Add links from source names table. (F8)
- Click Run (F5)
- Wait till done.
- Copy all parsed links
- Go to 'Контент' tab
- Paste links in bottom pane (F8)
- Click Run (F5)
- Wait till done.
- Go to 'C:/content'
- Copy 'images' folder to !WORKFLOW directory
- Rename 'images' folder using template: 'CategoryAliasGender'+'SRCImages'

2. Run script:
- sort_images_using_names.py
