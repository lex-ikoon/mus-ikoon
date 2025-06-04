import hou
import imp
import mus_job 
imp.reload(mus_job)



def create(parm_item):
    imp.reload(mus_job)
    node    = hou.pwd()
    parm    = node.parm("menu_" + parm_item)
    command = parm.evalAsString()

    # send command to external:
    mus_job.job_create(node, parm, command)



def names(nodes):
    return [node.name() for node in nodes]


def menu_items(key):
    node = hou.pwd()
    singles = names(   node.glob(key + "__*")   )  
  
    menuitems = []
    
    for single in singles:
        token = single
        label = single.replace(key + "__","")
        label = label.replace("_"," ")
        menuitems.append(token)
        menuitems.append(label)
    
    return menuitems