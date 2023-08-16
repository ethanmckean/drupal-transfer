import re
import yaml
import copy

# Read the input file
with open('export.xml', 'r') as file:
    input = file.read()

# Read config options
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)['site']

# Setup regex dictionary
patterns = {
    "convert_http": (r'href="http:',r'href="https:'),
    "note_accordions": (r'<Body>[\s\S]*?div class="accordion"[\s\S]*?</Body>[\s\S]*?<Path>(/[^<]+)</Path>', ''),
    "clean_href": (r'href="https:\/\/' + config['name'] + r'\.umich\.edu(.*?)"', r'href="\1"'),
    "clean_image_tags":(r'<Image>.*src="(.*?)".*</Image>', r'<Image>\1</Image>'),
    "clean_image_path": (r'src="https:\/\/' + config['name'] + r'\.umich\.edu(.*?)"', r'src="\1"'),
    "clean_button":(r'<a class(.*)btn-danger', r'<a class\1btn-error'),
    "clean_subdirectory_path":(r'<Path>/' + config['subdirectory_path_name'] + r'(.*)</Path>', r'<Path>\1</Path>')
}

modified_input = copy.deepcopy(input)

for pattern_key, pattern_value in patterns.items():
    if config[pattern_key]:
        match pattern_key:
            case "clean_subdirectory_path":
                if config["subdirectory_path"]:
                    modified_input = re.sub(pattern_value[0], pattern_value[1], modified_input)
            case "note_accordions":
                print('Pages with accordions:', re.findall(pattern_value[0], modified_input))
            case _:
                modified_input = re.sub(pattern_value[0], pattern_value[1], modified_input)

print('# btn danger removed = ', len(re.findall(patterns['clean_button'][0], input)))
regex_btn = r'btn-danger'
print("# btn danger = ", len(re.findall(regex_btn, input)))

#Write the modified output
with open('out.xml', 'w') as file:
    file.write(modified_input)
      
print("Cleaned ", len(re.findall(patterns["clean_href"][0], input)), " hrefs")

print("Fixed ", len(re.findall(patterns["clean_image_tags"][0], input)), " images")

print("Cleaned ", len(re.findall(patterns["clean_image_path"][0], input)), " images paths")
