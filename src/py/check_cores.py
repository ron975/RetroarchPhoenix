import os
import win32_check
import root_path
import xml_creator


def get_matches(path='/usr/lib/libretro'):
    if os.path.exists(path):
        matches = xml_creator.scan(path, ('*.so'), tag='core_exists')
        return matches
    else:
        return '''The directory entered doesn't exist.'''


def get_jslist(a_list, tag='core_exists', index=0):
    jscript_list = []
    for entry in a_list:
        if '\n' in entry:
            entry = entry.replace('\n', '')
        jscript_dict = {}
        print(entry)
        if index != 0:
            jscript_dict[tag] = entry[index].rstrip(' ').rstrip('\n')
        else:
            jscript_dict[tag] = entry
        jscript_list.append(jscript_dict)
    return jscript_list

def get_shader_path(shader_list):
    path_list = []
    for line in shader_list:
        shader_path = line.split(':')
        path_list.append(shader_path)

        paths = get_jslist(shader_path, tag='shader_path')
    return get_jslist(path_list, tag='shader_path', index=1)

def get_title(get_path=0):
    with open(root_path.change('..') + '/shaders.txt', 'r') as fid:
        lines = fid.readlines()
        if get_path:
            return get_shader_path(lines)
        
        shader_title = get_jslist(lines, tag='shader')
        #shader_path = get_jslist(lines[1], tag='shader_path')
        #pyotherside.send('shader_path',shader_path)
    return shader_title
    
def cores_list(path='/usr/lib/libretro'):
    if win32_check.check():
        pass
    else:
        with open(root_path.path() + '/linux_cores.txt', 'r') as fid:
            cores = fid.readlines()
            clean_cores = get_jslist(cores, tag='available')
        return clean_cores
