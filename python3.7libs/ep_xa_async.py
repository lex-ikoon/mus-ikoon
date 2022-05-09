import hou


def pin_desktop (node_notes) :
    # callback script:
    # import imp; import ep_xa_async ; imp.reload(ep_xa_async); node = kwargs["node"] ; ep_xa_async.pin_desktop(node)

    node_obj = node_notes.node('notes')

    # net 1
    hou.ui.curDesktop().findPaneTab("pt_network_1").setLinkGroup(hou.paneLinkType.Pinned)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_1").setLinkGroup(hou.paneLinkType.Pinned)

    # net 2
    hou.ui.curDesktop().findPaneTab("pt_network_2").setPwd(node_obj)
    hou.ui.curDesktop().findPaneTab("pt_network_2").setLinkGroup(hou.paneLinkType.Pinned)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_2").setPwd(node_obj)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_2").setLinkGroup(hou.paneLinkType.Pinned)

    # sceneviews
    hou.ui.curDesktop().findPaneTab("pt_sceneview_1").setPwd(node_notes)
    hou.ui.curDesktop().findPaneTab("pt_sceneview_1").setLinkGroup(hou.paneLinkType.Pinned)
    hou.ui.curDesktop().findPaneTab("pt_sceneview_2").setPwd(node_obj)
    hou.ui.curDesktop().findPaneTab("pt_sceneview_2").setLinkGroup(hou.paneLinkType.Pinned)

    # camera_set_ortho :
    script = "viewtype -t ortho_front wf_desktop.pt_sceneview_2.world"
    hou.hscript(script)


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def reload_source_music(node) :
    # callback script:
    # import imp; import ep_xa_async ; imp.reload(ep_xa_async); node = kwargs["node"] ; ep_xa_async.reload_source_music(node)
    file_node = node.node("chopnet/file")
    file_node.parm("reload").pressButton()


def print_music_properties(node) :
    # callback script:
    # import imp; import ep_xa_async ; imp.reload(ep_xa_async); node = kwargs["node"] ; ep_xa_async.print_music_properties(node)

    file_node = node.node("chopnet/OUT")
    print (file_node)
    # .wav first sample is 0
    # .wav last  sample is [1]-[0]
    # last length is [1]-[0] + 1
    sampleRange    = file_node.sampleRange()[1] - file_node.sampleRange()[0]  +  1
    samplesToFrame = file_node.samplesToFrame(sampleRange)
    samplesToTime  = file_node.samplesToTime(sampleRange)
    sampleRate     = file_node.sampleRate()

    print("\n\n-------------- audio --------------")
    print("set the track_length_seconds to:")
    print("samplesToTime()      " , str(samplesToTime) , " seconds")
    print("---------------------------------------")
    print("sampleRange()        " , str(file_node.sampleRange()))
    print("samplesToFrame()     " , str(samplesToFrame))
    print("sampleRate()         " , str(sampleRate))


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def reload_source_image(node) :
    # callback script:
    # import imp; import ep_xa_async ; imp.reload(ep_xa_async); node = kwargs["node"] ; ep_xa_async.reload_source_image(node)

    # reload sequence:
    node.node("spectrum/cop2net/spec_gram").parm("reload").pressButton()
    node.node("spectrum/cop2net/spec_melo").parm("reload").pressButton()


def print_image_size(node) :
    # callback script:
    # import imp; import ep_xa_async ; imp.reload(ep_xa_async); node = kwargs["node"] ; ep_xa_async.print_image_size(node)


    cropped_size_gram = node.node("spectrum/cop2net/crop_gram").parm("hcrop2").evalAsString()
    cropped_size_melo = node.node("spectrum/cop2net/crop_melo").parm("hcrop2").evalAsString()
    print ("--------------------------------")
    print ("GRAM Cropped Size (px) is this: " + cropped_size_gram)
    print ("MELO Cropped Size (px) is this: " + cropped_size_melo)


def export_all(node) :
    # callback script:
    # import imp; import ep_xa_async ; imp.reload(ep_xa_async); node = kwargs["node"] ; ep_xa_async.export_all(node)

    # reload sequence:
    node.node("spectrum/cop2net/spec_gram").parm("reload").pressButton()
    node.node("spectrum/cop2net/spec_melo").parm("reload").pressButton()

    # check crop:
    node.node("spectrum/cop2net/spec_crop_gram").parm("execute").pressButton()
    node.node("spectrum/cop2net/spec_crop_melo").parm("execute").pressButton()

    # render:
    node.node("spectrum/cop2net/spec_gram_F4").parm("execute").pressButton()
    node.node("spectrum/cop2net/spec_melo_F4").parm("execute").pressButton()


# $JOB/tex/_async/gram/spec_gram_`padzero(4,$F-1)`.png
# $JOB/tex/_async/crop/spec_crop_gram.png
# $JOB/tex/_async/melo/spec_melo_`padzero(4,$F-1)`.png
# $JOB/tex/_async/crop/spec_crop_melo.png