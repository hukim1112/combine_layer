import os
import pytoshop
from pytoshop.user import nested_layers

bg_path = './background'
bc_path = './bottom_color'
result_path = './result'

if not os.path.isdir(bg_path):
    os.makedirs(bg_path)
if not os.path.isdir(bc_path):
    os.makedirs(bc_path)
if not os.path.isdir(result_path):
    os.makedirs(result_path)

for file in os.listdir(bg_path):
    with open(os.path.join(bg_path, file) ,'rb') as fd:
        bg_psd = pytoshop.read(fd)
        bg_nested = nested_layers.psd_to_nested_layers(bg_psd)
        for l in bg_nested:
            if l._name == 'bg':
                bg_group = l
        with open(os.path.join(bc_path, file) , 'rb') as fd:
            bc_psd = pytoshop.read(fd)
            bc_nested = nested_layers.psd_to_nested_layers(bc_psd)
            bc_nested.insert(len(bc_nested)-1, bg_group)

            with open(os.path.join(result_path, file), 'wb') as fd:
                bc_psd = nested_layers.nested_layers_to_psd(bc_nested, bc_psd._color_mode)
                bc_psd.write(fd)
