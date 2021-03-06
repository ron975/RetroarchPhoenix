import os
import sys
import win32_check
import root_path

if win32_check.check():
    RETRO_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'retroarch_v1.0'))
    OUTPUT_CFG = RETRO_PATH + '\\custom.cfg'
else:
    RETRO_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'shaders'))
    OUTPUT_CFG = os.path.expanduser('~') + '/.config/retroarch/custom.cfg'


def write_shader(data):
    fid = RETRO_PATH + '/retroarch.cgp'
    print('Wrote to: ', fid)
    with open(fid, 'w') as retro_cgp:
        retro_cgp.seek(0)
        retro_cgp.write(data)

def read_shader(selected_shader):
    shader = root_path.change('shaders') + selected_shader
    with open(shader, "r") as shader_file:
        if ".cgp" in selected_shader:
            shader_data = shader_file.readlines()
            first_line = int(shader_data[0].split()[2].replace('"', ''))
            num_of_shaders = first_line
            for i in range(0, num_of_shaders-1):
                for line in shader_data:
                    if 'filter_linear{:}'.format(str(i)) == line.split()[0]:
                        index_for_wrap = shader_data.index(line) + 1
                        shader_data[index_for_wrap] = 'wrap_mode{:} = "clamp_to_border"\n'.format(i)
                        break
            return write_shader(''.join(shader_data))                
        else:
            cg_file = ['shaders = "1"\n', 'shader0 = ""', \
                       'wrap_mode0 = "clamp_to_border"\n', \
                       'float_framebuffer0 = "false"\n']
            
            cg_file[1] = 'shader0 = "{:}"\n'.format(shader)
            write_cg(''.join(cg_file))
            
    config_data = get_config_data(OUTPUT_CFG)
    ammended_data = ammend_config(config_data)
    write_config(OUTPUT_CFG, ammended_data)
    return ('Shader wrote to ', )

def write_cg(ammended_data):
    cgp = root_path.change('shaders') + '/retroarch.cgp'
    with open(cgp, 'w') as ofile:
        ofile.seek(0)
        ofile.write(ammended_data)
        ofile.write('wrap_mode0 = "clamp_to_border"\n')
        ofile.write('float_framebuffer0 = "false"\n')

def get_config_data(cfg_file):
    with open(cfg_file, 'r') as  infile:
        cfg_data = infile.readlines()
        return cfg_data
    
def ammend_config(data):
    with open(OUTPUT_CFG, 'r') as infile:
        for index, line in enumerate(infile):
            if 'video_shader' == line.split()[0]:
                data[index] = 'video_shader = "{:}/retroarch.cgp"\n'.format(root_path.change('shaders'))
                return data
        print('never found')

def write_config(fid, new_data):
    with open(fid, "w") as outfile:
        outfile.seek(0)
        outfile.write("".join(new_data))
    
