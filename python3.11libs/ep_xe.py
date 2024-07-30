import hou


def build_curves_autoname (node_build) :
    # callback script:
    # import imp; import ep_xe ; imp.reload(ep_xe); node = kwargs["node"] ; ep_xe.build_curves_autoname(node)

    full_name = ""
    full_name = node_build.node("autoname").geometry().attribValue("b_name")
    full_name = full_name + "_"

    task = node_build.node("switch__task").parm("input").evalAsInt()
    if task == 0: full_name += "_INIT"
    if task == 1: full_name += ""
    if task == 2: full_name += "_COLLECT"


    # -------------
    if task == 1:
        if node_build.parm("use_follow_prev_node").evalAsInt() == 1:        full_name += "_follow"
        if node_build.parm("use_skeleton").evalAsInt() == 1:         full_name += "_skelet"
        if node_build.parm("use_target").evalAsInt() == 1:               full_name += "_target"
        if node_build.parm("use_transform_handle").evalAsInt() == 1:     full_name += "_xform"
        if node_build.parm("use_sdf").evalAsInt() == 1:                  full_name += "_sdf"
        if node_build.parm("use_noise").evalAsInt() == 1:                full_name += "_noise"
        if node_build.parm("use_collision").evalAsInt() == 1:            full_name += "_collision"

    node_build.setName(   full_name  , unique_name=True  )


    # -------------
    if task == 0: node_build.setUserData("nodeshape", "chevron_down")
    if task == 1: node_build.setUserData("nodeshape", "rect")
    if task == 2: node_build.setUserData("nodeshape", "chevron_up")



def create_gradient_group (node_guides) :
    # callback script:
    # import imp; import ep_xe ; imp.reload(ep_xe); node = kwargs["node"] ; ep_xe.create_gradient_group(node)
    connection = node_guides.inputConnections()[0]
    node_up = connection.inputNode()
    node_dn = connection.outputNode()
    node_up_index = connection.outputIndex()
    node_dn_index = connection.inputIndex()

    node_group = node_dn.createInputNode(node_dn_index, "groupcreate" )
    node_group.setNextInput(node_up, node_up_index)
    node_group.moveToGoodPosition(relative_to_inputs=False, move_inputs=False, move_outputs=True, move_unconnected=False)

    node_group.parm("groupname").set("start_gradient")
    node_group.parm("grouptype").set(1)
    node_group.parm("groupbase").set(0)
    node_group.parm("groupbounding").set(1)
    node_group.parm("sizex").set(0.1)
    node_group.parm("sizey").set(0.1)
    node_group.parm("sizez").set(5.0)

    node_group.setName(   node_guides.name()+"_gradient"    )



def create_paint_nodes (node_guides) :
    # callback script:
    # import imp; import ep_xe ; imp.reload(ep_xe); node = kwargs["node"] ; ep_xe.create_paint_nodes(node)


    # ----------

    connection = node_guides.inputConnections()[0]
    node_up = connection.inputNode()
    node_dn = connection.outputNode()
    node_up_index = connection.outputIndex()
    node_dn_index = connection.inputIndex()

    node_add = node_dn.createInputNode(node_dn_index, "attribcreate" )
    node_add.setNextInput(node_up, node_up_index)
    node_add.moveToGoodPosition(relative_to_inputs=False, move_inputs=False, move_outputs=True, move_unconnected=False)
    node_add.parm("name1").set("density")
    node_add.parm("value1v1").set(0.5)
    node_add.setName(   node_guides.name()+"__density_add"    )

    # ----------

    connection = node_guides.inputConnections()[0]
    node_up = connection.inputNode()
    node_dn = connection.outputNode()
    node_up_index = connection.outputIndex()
    node_dn_index = connection.inputIndex()


    node_paint = node_dn.createInputNode(node_dn_index, "attribpaint" )
    node_paint.setNextInput(node_up, node_up_index)
    node_paint.moveToGoodPosition(relative_to_inputs=False, move_inputs=False, move_outputs=True, move_unconnected=False)
    node_paint.parm("attribname1").set("density")
    node_paint.setName(   node_guides.name()+"__density_paint"    )