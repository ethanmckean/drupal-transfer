# drupal-transfer
View template for Drupal 7 along with a python script to clean the output
Template configuration may differ per site. 
- Views -> import to import template.

Python3 is required for `script.py`


TODO:
- [ ] ~~Add command line options (and/or args)~~
  - Replaced in favor of configuration file
- [X] Add configuration file
  - [ ] Support specifying folder with input and output xml files
  - [X] Support specifying domain & site name
  - [X] Support more granular cleaning options
- [ ] Refactor the stats logic to be more efficient (not necessary currently due to fast enough execution time)
  - [ ] Pretty up the display