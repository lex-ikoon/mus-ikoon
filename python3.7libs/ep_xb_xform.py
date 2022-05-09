import hou
import nodesearch 


def base_to_origin (node_xform) :
    # callback script:
    # import imp; import ep_xb_xform ; imp.reload(ep_xb_xform); node = kwargs["node"] ; ep_xb_xform.base_to_origin(node)

    root        = hou.node("/obj")
    matcher     = nodesearch.NodeType( "xb::xform", hou.objNodeTypeCategory() )
    nodes_xform = matcher.nodes( root, recursive=True )
    matrix_base = node_xform.worldTransform()
    

    color_node_grey = hou.Color(0.8, 0.8, 0.8)
    color_node_dark = hou.Color(0.306, 0.306, 0.306)
    
    for node in nodes_xform :
        matrix_update = node.worldTransform() * matrix_base.inverted()
        node.setWorldTransform(matrix_update)
        node.setColor(color_node_grey)


        if node == node_xform :
            node.setColor(color_node_dark)
            matrix_update.setToIdentity()
            node.setWorldTransform(matrix_update)
            node.parmTuple("t").set((0.0, 0.0, 0.0))
            node.parmTuple("r").set((0.0, 0.0, 0.0))






#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
