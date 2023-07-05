# drupal-transfer
View template for Drupal 7 along with a python script to clean the output
Template configuration may differ per site. 
- Views -> import to import template.

Python3 is required for `script.py`


TODO:
- [ ] Add command line options (and/or args)
- [ ] Add configuration file
  - [ ] Support specifying folder with input and output xml files
  - [ ] Support specifying domain & site name (though site name might be better as a command line arg)
- [ ] Refactor the stats logic to be more efficient (not necessary currently due to fast enough execution time)