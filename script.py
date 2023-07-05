import re
# Read the input file
with open('export.xml', 'r') as file:
    input = file.read()

site = "caps"

# Clean the HREFs
regex = r'href="https:\/\/' + site + r'\.umich\.edu(.*?)"'
substitution = r'href="\1"'
modified_input = re.sub(regex, substitution, input)

# Clean the Image tags
regex_image = r'<Image>.*src="(.*?)".*</Image>'
substitution = r'<Image>\1</Image>'
modified_input = re.sub(regex_image, substitution, modified_input)

# Clean the Image paths 
regex_image_path = r'src="https:\/\/' + site + r'\.umich\.edu(.*?)"'
substitution = r'src="\1"'
modified_input = re.sub(regex_image_path, substitution, modified_input)

# Clean the Path (parents, any site with subdomain as part of the URL path)
# regex_path = r'<Path>/parents(.*)</Path>'
# substitution = r'<Path>\1</Path>'
# modified_input = re.sub(regex_path, substitution, modified_input)

# Change button class (btn-danger deprecated in our instance of d9)
regex_btn = r'<a class(.*)btn-danger'
substitution = r'<a class\1btn-error'
modified_input = re.sub(regex_btn, substitution, modified_input)

print('# btn danger removed = ', len(re.findall(regex_btn, input)))
regex_btn = r'btn-danger'
print("# btn danger = ", len(re.findall(regex_btn, input)))

#Write the modified output
with open('out.xml', 'w') as file:
    file.write(modified_input)

print("Cleaned ", len(re.findall(regex, input)), " hrefs")

print("Fixed ", len(re.findall(regex_image, input)), " images")

print("Cleaned ", len(re.findall(regex_image_path, input)), " images paths")