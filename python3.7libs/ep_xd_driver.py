import hou


def check_keyframes (node_driver) :
    # callback script:
    # import imp; import ep_xd_driver ; imp.reload(ep_xd_driver); node = kwargs["node"] ; ep_xd_driver.check_keyframes(node)

    node_driver = hou.node('/obj/driver')
    xc_keys     = node_driver.node("paths/xc_keys").geometry()
    keyparm     = node_driver.parm("cam_arclen")
    keys        = keyparm.keyframes()

    key_arclenghts = xc_keys.floatListAttribValue("key_arclenghts")
    key_frames     = xc_keys.floatListAttribValue("key_frames")
    key_modes      = xc_keys.floatListAttribValue("key_modes")

    for (keynum, key) in enumerate(keys) :

        if key_modes[keynum] == 1:
            # affect only automatic
            key.setValue(key_arclenghts[keynum])
            key.setFrame(key_frames[keynum])

    keyparm.deleteAllKeyframes()
    keyparm.setKeyframes(keys)



#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def reload_path (node_driver) :
    # callback script:
    # import imp; import ep_xd_driver ; imp.reload(ep_xd_driver); node = kwargs["node"] ; ep_xd_driver.reload_path(node)

    # merge xc nodes
    node_merge = node_driver.node("paths/xc_node_merge")
    path_items = node_driver.parm("path_items").eval()
    type_check = 0

    for i in range(1, path_items+1, 1):
        xc_node_path = node_driver.parm('xc%d' % i).eval()
        xc_node      = node_driver.node(xc_node_path)
        xc_node_abs  = xc_node.path()
        xc_node_points = xc_node_abs + "/points"

        node_merge_parm = node_merge.parm('objpath%d' % i)
        node_merge_parm.set(xc_node_points)

        try:
            if xc_node.type().name().split("::")[1] != "view" :
                type_check += 1
        except:
            type_check += 1

           
    # merge xc nodes
    node_merge = node_driver.node("paths/cam_override_merge")
    over_items = node_driver.parm("override_items").eval()

    for i in range(1, over_items+1, 1):
        cam_over_path = node_driver.parm('cam_over%d' % i).eval()
        cam_over      = node_driver.node(cam_over_path)
        cam_over_abs  = cam_over.path()
        cam_over_points = cam_over_abs + "/points"

        node_merge_parm = node_merge.parm('objpath%d' % i)
        node_merge_parm.set(cam_over_points)

        try:
            if cam_over.type().name().split("::")[1] != "view" :
                type_check += 1
        except:
            type_check += 1

    # warning
    if type_check >0 :
        hou.ui.displayMessage("All referenced cameras type() should be: \n\nxc::view \n\nbecause we need the /points inside", severity=hou.severityType.Error)
        

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------

def create_driven_camera (node_driver) :
    # callback script:
    # import imp; import ep_xd_driver ; imp.reload(ep_xd_driver); node = kwargs["node"] ; ep_xd_driver.create_driven_camera(node)
    
    cam = node_driver.createOutputNode("cam")
    cam.moveToGoodPosition()
    # bind:
    # focal length
    # focus distance
    # (todo later CoC)
