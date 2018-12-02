import glob
import re


def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1-\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1-\2', s1).lower()


data_to_write = 'import Vue from \'vue\'\n\n'
component_list = []
for component_file in sorted(glob.glob('node_modules/buefy/src/components/*/*.vue')):
    name = component_file.split('/')[-1].replace('.vue', '')
    path = component_file.split('node_modules/')[-1].replace('.vue', '')

    data_to_write += f'import {name} from \'{path}\'\n'
    component_list.append(name)

data_to_write += '\n'
for component in component_list:
    component_name = convert(component)
    data_to_write += f'Vue.component(\'b-{component_name}\', {component})\n'

with open('dist/fakeComponents.js', 'w+') as f:
    f.write(data_to_write)
