## Other useful scripts

**!!!IMPORTANT!!!**
Store all files in **!WORKFLOW** directory

1. **imagesRenamer.py** - Files renamer
Methods:
- **plain_rename** - renames files in specified directory
- **remove_diacritic_spaces_and_dashes** - remove diacritic symbols, dashes and spaces for filenames in specified directory

| Parameter     | Decription     |
| :------------- | :------------- |
| **src_dir** | source directory |
| **target_dir** | target directory |
| **crop_from_index** | index for prefix to cut from filename |
| **new_prefix** | new prefix instead of cropped |

1. **renameBackgrounds.py** - cycle through images, and specify image size in filename
- Use for:
  - Rename parsed background images, to observe image size in filename

| Parameter     | Decription     |
| :------------- | :------------- |
| **file_name_template** | Prefix for new filenames |
| **scrDir** | source directory |
| **targetDir** | targetDir |
