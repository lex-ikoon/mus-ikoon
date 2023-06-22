def change(**kwargs):
    if kwargs["event_type"] == hou.nodeEventType.ParmTupleChanged:
        try:
            node_driver = kwargs["node"].parm("driver").evalAsNode()
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

        except:
            # print ("error")
            pass

node  = kwargs["node"]
node.addEventCallback( (hou.nodeEventType.ParmTupleChanged, ), change)