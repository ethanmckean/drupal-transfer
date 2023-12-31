# drupal-transfer
View template for Drupal 7 along with a python script to clean the output
Template configuration may differ per site. 

## How to use

### Exporting
- Navigate to the views import page to import the template: `yoursite.xyz/admin/structure/views/import`.
- Give your view a name (e.g. `export`) and paste the view template in.
- Adjust the Filter criteria and other settings as needed (see the preview below to confirm the view is working).
- Save and click "view Data export" (or navigate to the export path).

### Cleaning
Python3 is required for `script.py` (3.7 and greater to ensure proper usage due to dictionary order)
- Ensure `export.xml` is in the same folder
- Run the script: `python3 script.py`
- Configure a feed import and upload `out.xml` to your new Drupal site!

### Misc
`remove_google_redirect.ahk`
- Removes google redirect from links using [AHK](https://github.com/AutoHotkey/AutoHotkey)
`remove_site_url.ahk`
- Removes domain from source (useful for when copying + pasting). Technically it could implement a YAML [parser](https://github.com/HotKeyIt/Yaml) but the overhead would be unnecessary so for now just modify `[DOMAIN HERE]` to the intended domain to remove.

## TODO
- [ ] ~~Add command line options (and/or args)~~
  - Replaced in favor of configuration file
- [X] Add configuration file
  - [ ] Support specifying folder with input and output xml files
  - [X] Support specifying domain & site name
  - [X] Support more granular cleaning options
- [X] Refactor the entire program logic (reduce code repetition while maintaining extensibility)
- [ ] Refactor the stats logic to be more efficient (not necessary currently due to fast enough execution time)
  - [ ] Pretty up the display