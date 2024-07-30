import hou

# ramp library
# import imp; import wf_network_ui; imp.reload(wf_network_ui); wf_network_ui.parm_ramp_string_lib(kwargs["node"], kwargs["parm"])

def refresh_note_merge (node_notes) :
    # callback script:
    # import imp; import ep_xa_generator ; imp.reload(ep_xa_generator); node = kwargs["node"] ; ep_xa_generator.refresh_note_merge(node)
    merger = node_notes.glob("merge_notes")[0]
    merger.parm("enable1").set(0)
    merger.parm("enable1").set(1)