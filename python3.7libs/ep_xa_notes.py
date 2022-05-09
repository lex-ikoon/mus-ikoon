import hou


def pin_desktop (node_notes) :
    # callback script:
    # import imp; import ep_xa_notes ; imp.reload(ep_xa_notes); node = kwargs["node"] ; ep_xa_notes.pin_desktop(node)

    node_obj = node_notes.node('notes')

    # net 1
    hou.ui.curDesktop().findPaneTab("pt_network_1").setLinkGroup(hou.paneLinkType.Pinned)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_1").setLinkGroup(hou.paneLinkType.Pinned)

    # net 2
    hou.ui.curDesktop().findPaneTab("pt_network_2").setPwd(node_obj)
    hou.ui.curDesktop().findPaneTab("pt_network_2").setLinkGroup(hou.paneLinkType.Pinned)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_2").setPwd(node_obj)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_2").setLinkGroup(hou.paneLinkType.Pinned)

    # net 2 repin
    hou.ui.curDesktop().findPaneTab("pt_network_2").setLinkGroup(hou.paneLinkType.Group2)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_2").setLinkGroup(hou.paneLinkType.Group2)
    
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



def unpin_desktop (node_notes) :
    # callback script:
    # import imp; import ep_xa_notes ; imp.reload(ep_xa_notes); node = kwargs["node"] ; ep_xa_notes.unpin_desktop(node)


    hou.ui.curDesktop().findPaneTab("pt_network_1").setLinkGroup(hou.paneLinkType.Group1)
    hou.ui.curDesktop().findPaneTab("pt_network_2").setLinkGroup(hou.paneLinkType.Group2)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_1").setLinkGroup(hou.paneLinkType.Group1)
    hou.ui.curDesktop().findPaneTab("pt_parmeditor_2").setLinkGroup(hou.paneLinkType.Group2)
    hou.ui.curDesktop().findPaneTab("pt_sceneview_1").setLinkGroup(hou.paneLinkType.FollowSelection)
    hou.ui.curDesktop().findPaneTab("pt_sceneview_2").setLinkGroup(hou.paneLinkType.FollowSelection)


    # camera_set_perspective :
    script = "viewtype -t ortho_front wf_desktop.pt_sceneview_2.world"
    hou.hscript(script)
