import re
import yaml

# Read the input file
with open('export.xml', 'r') as file:
    input = file.read()

# Read config options
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

# Convert all http to https
if config['site']['convert_http']:
    reg = r'href="http'
    sub = r'href="https'
    modified_input = re.sub(reg,sub,input)

# Output pages with accordions
if config['site']['note_accordions']:
    regex_accordions = r'<Body>[\s\S]*?div class="accordion"[\s\S]*?</Body>[\s\S]*?<Path>(/[^<]+)</Path>'
    print('Pages with accordions:', re.findall(regex_accordions, input))

# Clean the HREFs
if config['site']['clean_href']:
    regex = r'href="https:\/\/' + config['site']['name'] + r'\.umich\.edu(.*?)"'
    substitution = r'href="\1"'
    modified_input = re.sub(regex, substitution, input)

# Clean the Image tags
if config['site']['clean_image_tags']:
    regex_image = r'<Image>.*src="(.*?)".*</Image>'
    substitution = r'<Image>\1</Image>'
    modified_input = re.sub(regex_image, substitution, modified_input)

# Clean the Image paths
if config['site']['clean_image_path']:
    regex_image_path = r'src="https:\/\/' + config['site']['name'] + r'\.umich\.edu(.*?)"'
    substitution = r'src="\1"'
    modified_input = re.sub(regex_image_path, substitution, modified_input)

# Change button class (btn-danger deprecated in our instance of d9)
if config['site']['clean_button']:
    regex_btn = r'<a class(.*)btn-danger'
    substitution = r'<a class\1btn-error'
    modified_input = re.sub(regex_btn, substitution, modified_input)

# Clean the Path (parents, any site with subdomain as part of the URL path)
if config['site']['subdirectory_path'] and config['site']['clean_subdirectory_path']:
    regex_path = r'<Path>/' + config['site']['subdirectory_path_name'] + r'(.*)</Path>'
    substitution = r'<Path>\1</Path>'
    modified_input = re.sub(regex_path, substitution, modified_input)

print('# btn danger removed = ', len(re.findall(regex_btn, input)))
regex_btn = r'btn-danger'
print("# btn danger = ", len(re.findall(regex_btn, input)))

#Write the modified output
with open('out.xml', 'w') as file:
    file.write(modified_input)

print("Cleaned ", len(re.findall(regex, input)), " hrefs")

print("Fixed ", len(re.findall(regex_image, input)), " images")

print("Cleaned ", len(re.findall(regex_image_path, input)), " images paths")
