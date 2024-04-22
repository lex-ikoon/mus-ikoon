import hou


def panes_music() :
    desktop    = hou.ui.curDesktop()
    pane_net   = desktop.findPaneTab("pt_network_2")
    pane_parm  = desktop.findPaneTab("pt_parmeditor_2")
    pane_scene = desktop.findPaneTab("pt_sceneview_2")
    return pane_net, pane_parm, pane_scene


def pane_scene_selectpositions(number) :
    pane_net, pane_parm, pane_scene = panes_music()
    positions = pane_scene.selectPositions(prompt='Click to specify a position',
        number_of_positions=number,
        connect_positions=True,
        show_coordinates=True,
        bbox=hou.BoundingBox(),
        position_type=hou.positionType.WorldSpace,
        icon=None,
        label=None)
    return positions


def camera_get_LRY() :
    pane_net, pane_parm, pane_scene = panes_music()

    camera = pane_scene.curViewport().defaultCamera()
    translation  = camera.translation()
    width  = camera.orthoWidth()
    left   = translation[0] - width/2
    right  = translation[0] + width/2
    y      = translation[1]
    return left, right, y
