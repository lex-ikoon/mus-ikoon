import hou
import os
from pathlib import Path
# -----------------------------------------------------------------

def change_to_JPG (node) :
    rop  = node.parm("roppath").evalAsNode()
    path = "$JOB/__data.render/$OS/${OS}_$F4.jpg"
    rop.parm("picture").set(path)


# -----------------------------------------------------------------

def video_path_to_clipboard (node) :
    
    job_location = hou.getenv("JOB")
    path         = Path(job_location)

    if node.parm("render_ig").eval() == 0:
        video_location = str(path.parent.absolute()) + "\_out\out_web.mp4"
        hou.ui.copyTextToClipboard(video_location)
        os.startfile(video_location)
    
    if node.parm("render_ig").eval() == 1:
        video_location = str(path.parent.absolute()) + "\_out\out_ig.mp4"
        hou.ui.copyTextToClipboard(video_location)

# -----------------------------------------------------------------

def video_play (node) :
    job_location = hou.getenv("JOB")
    path         = Path(job_location)

    if node.parm("render_ig").eval() == 0:
        video_location = str(path.parent.absolute()) + "\_out\out_web.mp4"
    
    if node.parm("render_ig").eval() == 1:
        video_location = str(path.parent.absolute()) + "\_out\out_ig.mp4"

    os.startfile(video_location)

# -----------------------------------------------------------------

def clone_rop_for_ig (node) :
    # define
    offsetx  = 3
    offsety  = 0
    color_ig = hou.Color(1.0, 0.725, 0.0)
    rop      = node.parm("roppath").evalAsNode()
    rop_ig   = rop.parent().copyItems([rop], channel_reference_originals = True, relative_references = True, connect_outputs_to_multi_inputs = True)
    posx     = rop.position()[0] + offsetx
    posy     = rop.position()[1] + offsety

    rop_ig[0].setPosition( [posx,posy] )
    rop_ig[0].setName( rop.name() + "_IG" )
    rop_ig[0].parm("tres").deleteAllKeyframes()
    rop_ig[0].parm("tres").set(1)
    rop_ig[0].setColor(color_ig)


# -----------------------------------------------------------------

def set_rop_bg (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.change_to_JPG(node)

    rop = node.parm("roppath").evalAsNode()
    cam = rop.parm("camera").evalAsNode()
    bg  = cam.parm("vm_background").evalAsString()
    rop.parm("bgimage").set(bg)
    # print(bg)

# -----------------------------------------------------------------

# -----------------------------------------------------------------

def set_resolution (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_resolution(node)
    camera = node.parm("cam").evalAsNode()
    res    = node.parm("res_web").evalAsInt()
    camera.parm("resx").set(res)
    camera.parm("resy").set(res)
    camera.parm("res_preview_mult").set(3.0)

# -----------------------------------------------------------------

def set_bg (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_bg(node)
    
    camera      = node.parm("cam").evalAsNode()
    bg_img_path = node.parm("bg_img_path")

    path        = camera.relativePathTo(node)
    expression = '''Q:/_gd/houdini_packages/mus_ikoon/tex/mus_source_cam_bg/bg_`padzero(3,chs("''' + path + '''"/bg_img))`.png'''
    # print(expression)
    camera.parm("vm_background").set(expression)

# -----------------------------------------------------------------

def remove_bg (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.remove_bg(node)
    camera     = node.parm("cam").evalAsNode()
    image_path = ""
    camera.parm("vm_background").set(image_path)


# -----------------------------------------------------------------

def set_fps (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_fps(node)
    hou.setFps(30)


# -----------------------------------------------------------------

def set_job (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_job(node)
    hip = hou.getenv("HIP")
    hou.putenv("JOB", hip)

# -----------------------------------------------------------------

def asCode_save (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.asCode_save(node)

    asCode      = hou.node("/obj").asCode(brief=False, recurse=True, save_creation_commands=True, save_spare_parms=True)
    path_asCode = str(hou.getenv("HIP")) + "/asCode.py"
    file_asCode = open( path_asCode, 'w' )
    file_asCode.write(asCode)
    file_asCode.close()

# -----------------------------------------------------------------

def asCode_load (node) :
    path_asCode = str(hou.getenv("HIP")) + "/asCode.py"
    exec(open(path_asCode).read())

    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.asCode_load(node)


