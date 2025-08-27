import hou
import imp
# import nodegraphutils

import wf_network_layout
imp.reload(wf_network_layout)




def job_create (node_job, parm, command) :
    # typical command:
    # points_sop__instance_-_many

    try:
        context = command.split("__")[0]
        context = context.split("_")[1]
    except:
        context = "none"

    # --------------------------------------------------------------------------------------------------
    # SOP

    if context == "sop" :


        # ----------------
        # copypaste
        clipboard = node_job.node(command).inputAncestors()
        hou.copyNodesTo(clipboard, node_job.parent())
        # print(pasted)

        job_link_top = node_job.parent().glob("JOB_LINK_TOP*")[0]
        job_link_bot = node_job.parent().glob("JOB_LINK_BOT*")[0]

        # ----------------
        # connect top
        try:
            job_link_top.setInput(0, node_job.input(0), output_index=0)
        except:
            # there was no input node
            pass

        # ----------------
        # connect bottom
        node_job.setInput(0, job_link_bot, output_index=0)

        
        # ----------------
        # # reconnect & blast
        # TODO
        # nodegraphutils.reconnectAroundItems([job_link_top], False)
        # nodegraphutils.reconnectAroundItems([job_link_bot], False)
        job_link_top.destroy()
        job_link_bot.destroy()        

        # ----------------
        # reconnect & blast
        wf_network_layout.lay()



    
    # --------------------------------------------------------------------------------------------------
    # LOP
    if context == "lop" :
        # ----------------
        # find target
        # ----------------
        # copypaste

        # -----------------------
        # define
        offsetx = 4
        offsety = 0


        # -----------------------
        # find the LOP karma
        # create it if needed
        node_lop = hou.node("/obj/karma_" + node.parent().name())
        if node_lop == None :
            wf_job.create_job_karma_from_geo(   node.parent()   )
        node_lop = hou.node("/obj/karma_" + node.parent().name())
        node_GEO = node_lop.node("GEO")

        # -----------------------
        # position
        root                = node_lop
        matcher             = nodesearch.NodeType( "sopimport", hou.lopNodeTypeCategory() )
        existing_sopimports = matcher.nodes( root, recursive=True )

        if len(existing_sopimports) == 0:
            posx = node_GEO.position()[0] + 0
            posy = node_GEO.position()[1] + 6

        else:
            posx = -10000
            posy = -10000
            for existing_sopimport in existing_sopimports:
                posx = max(posx,existing_sopimport.position()[0])
                posy = max(posy,existing_sopimport.position()[1])
            posx = posx + offsetx
            posy = posy + offsety


        # -----------------------
        # create SOP Import
        node_sopimport = node_lop.createNode( "sopimport", node.name() )
        node_sopimport.setPosition( [posx,posy] )
        node_sopimport.setComment("`")
        node_sopimport.parm("soppath").set(node.path())
        node_sopimport.parm("bindmaterials").set("createbind")
        node_sopimport.parm("pathprefix").set("geo/$OS")
        node_sopimport.parm("enable_savepath").set(1)
        node_sopimport.parm("savepath").set('$JOB/_usd/`chs("../file")`_${OS}_savepath.usd')





        pass



    # --------------------------------------------------------------------------------------------------
    # MAT
    if context == "mat" :
        clipboard = node_job.node(command).children()
        # target = 
        # hou.copyNodesTo(clipboard, node_job.parent())

