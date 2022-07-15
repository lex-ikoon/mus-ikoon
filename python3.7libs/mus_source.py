import hou
import os



def set_resolution (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_resolution(node)
    camera = node.parm("cam").evalAsNode()
    res    = node.parm("web_res").evalAsInt()
    camera.parm("resx").set(res)
    camera.parm("resy").set(res)

def set_bg (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_bg(node)
    camera     = node.parm("cam").evalAsNode()
    source     = node.parm("source").evalAsInt()
    image_path = str(hou.getenv("mus_path")) + "/tex/mus_source_cam_bg/" + str(source) + ".png"
    camera.parm("vm_background").set(image_path)

def remove_bg (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.remove_bg(node)
    camera     = node.parm("cam").evalAsNode()
    image_path = ""
    camera.parm("vm_background").set(image_path)


def set_fps (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_fps(node)
    hou.setFps(30)


def set_job (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.set_job(node)
    hip = hou.getenv("HIP")
    hou.putenv("JOB", hip)

def asCode_save (node) :
    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.asCode_save(node)

    asCode      = hou.node("/obj").asCode(brief=False, recurse=True, save_creation_commands=True, save_spare_parms=True)
    path_asCode = str(hou.getenv("HIP")) + "/asCode.py"
    file_asCode = open( path_asCode, 'w' )
    file_asCode.write(asCode)
    file_asCode.close()

def asCode_load (node) :
    path_asCode = str(hou.getenv("HIP")) + "/asCode.py"
    exec(open(path_asCode).read())

    # callback script:
    # import mus_source; import imp; imp.reload(mus_source); node = kwargs["node"] ; mus_source.asCode_load(node)


