import hou
import imp
import ep_xa
import nodesearch
imp.reload(ep_xa)


def note_create(node):
    # callback script:
    # import imp; import ep_xa_note ; imp.reload(ep_xa_note); node = kwargs["node"] ; ep_xa_note.note_create(node)
    notes_net = node.parent()

    positions = ep_xa.pane_scene_selectpositions(1)[0]
    new_note  = notes_net.createNode("xa::note","note_")
    new_note.moveToGoodPosition()
    new_note.parm("tx").set(positions[0])
    new_note.parm("ty").set(positions[1]) # - track_active.parm("ty").eval())

    note_create(node)


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def notes_align_y(node):
    # callback script:
    # import imp; import ep_xa_note ; imp.reload(ep_xa_note); node = kwargs["node"] ; ep_xa_note.notes_align_y(node)
    root    = node.parent()
    matcher = nodesearch.NodeType( "xa::note", hou.objNodeTypeCategory() )
    notes   = matcher.nodes( root, recursive=True )


    for note in notes :
        ty = note.parm("ty").eval()
        ty = round (ty/5) * 5
        ty = abs(ty)
        note.parm("ty").set(ty)


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def span_scope_notes(node):
    # callback script:
    # import imp; import ep_xa_note ; imp.reload(ep_xa_note); node = kwargs["node"] ; ep_xa_note.span_scope_notes(node)

    root    = node.parent()
    matcher = nodesearch.NodeType( "xa::span", hou.objNodeTypeCategory() )
    span    = matcher.nodes( root, recursive=True ) [0]

    merger = root.node("generator").glob("merge_notes")[0]
    merger.parm("enable1").set(0)
    merger.parm("enable1").set(1)


    notes_GEO_zoom = root.node("generator/GEO_zoom").geometry()

    if len(   notes_GEO_zoom.points()   )>0 :
        notes_left   = notes_GEO_zoom.boundingBox().minvec()[0]
        notes_right  = notes_GEO_zoom.boundingBox().maxvec()[0]
        sizex        = notes_right - notes_left
        centerx      = (notes_right + notes_left) / 2

        span.parm("sizex").set(sizex)
        span.parm("centerx").set(centerx)
    

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def span_scope_camera(node):
    # callback script:
    # import imp; import ep_xa_note ; imp.reload(ep_xa_note); node = kwargs["node"] ; ep_xa_note.span_scope_camera(node)
    root    = node.parent()
    matcher = nodesearch.NodeType( "xa::span", hou.objNodeTypeCategory() )
    span    = matcher.nodes( root, recursive=True ) [0]

    left, right, y = ep_xa.camera_get_LRY()

    sizex        = right - left
    centerx      = (left + right ) / 2
    span.parm("sizex").set(sizex)
    span.parm("centerx").set(centerx)


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def notes_delete_all(node):
    # callback script:
    # import imp; import ep_xa_note ; imp.reload(ep_xa_note); node = kwargs["node"] ; ep_xa_note.notes_delete_all(node)
    root    = node.parent()
    matcher = nodesearch.NodeType( "xa::note", hou.objNodeTypeCategory() )
    notes    = matcher.nodes( root, recursive=True )

    for note in notes :
        note.destroy()

