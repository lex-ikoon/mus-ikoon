import hou
import os
# import subprocess
# import re
import pickle
import wf_selection

import hou



def generate_html() :


    # TODO:
    #------------------------------------------------------------
    # .gitignore
    # Q:\_packages\ep_ikoon\_library
    # Q:\_packages\ep_ikoon\_rnd

    # keep this folder to keep track of the updates
    # Q:\_packages\ep_ikoon\_web


    # init variables
    #------------------------------------------------------------
    # {"ep_path":       "Q:/_packages/ep_ikoon"},
    library_root = hou.getenv("ep_path") + "/_library/"
    web_root     = hou.getenv("ep_path") + "/_web/"


    # collect all directories
    # ---------------------------------------------------------------
    directories = []

    for directory in os.listdir(library_root):
        if os.path.isdir(os.path.join(library_root, directory)):
            directories.append(directory)


    # read index header and footer
    # ---------------------------------------------------------------
    with open(web_root + "index_template.html") as index_template:
        html_index = index_template.read() 
    index_template.close()
    
    find_HEADER = html_index.find("<!-- HEADER -->")
    find_FOOTER = html_index.find("<!-- FOOTER -->")
    html_header = html_index[:find_HEADER]
    html_footer = html_index[find_FOOTER:]


    # create item for each directory
    # ---------------------------------------------------------------
    with open(web_root + "video_template.html") as video_template:
        html_video = video_template.read() 
    video_template.close()
    
    for directory in directories :
        print(directory)
        # read category
        # replace category
        # change to lowercase


        


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------


def parse_tab_vex () :

    # init variables
    #------------------------------------------------------------
    toolname_prefix = "qw // "
    path_VEX_db      = hou.getenv("wf_path") + "/vex_src/_db/"
    path_VEX_vfl     = hou.getenv("wf_path") + "/vex_src/"


    # find files
    #------------------------------------------------------------


    # separate snippets and descriptions
    #------------------------------------------------------------
    snippets    = []
    nodenames   = []
    sourcefiles = []
    sourcelines = []
    toolnames   = []
    
    for vfl_path in vfl_paths:

        vfl_file  = open( vfl_path )
        uber_data = vfl_file.read()
        blocks    = uber_data.split('///---------------------')

        for block in blocks:

            block                 = block.strip("-")
            lines                 = block.split('\n')
            line_num              = len(lines)
            line_with_description = -1

            for i, line in enumerate(lines) :
                if line.startswith("///") :
                    line_with_description = i

            if line_with_description > -1:

                # block is a valid definition
                # sourceline
                all_lines   = uber_data.split('\n')
                description = lines[line_with_description]
                for i, line in enumerate(all_lines) :
                    if line.startswith(description) :
                        sourceline = i + 1

                # description
                description = lines[line_with_description]
                description = description.lstrip("/ ")

                # snippet
                snippet = ""
                for i in range( line_with_description + 1 , len(lines) ) :
                    snippet += lines[i]
                    snippet += "\n"

                # nodename
                nodename = validate_nodename(description)

                # toolname
                toolname = validate_toolname(description)
                toolname = toolname_prefix + description

                # arrays
                snippets.append(snippet)
                nodenames.append(nodename)
                sourcefiles.append(vfl_path)
                sourcelines.append(sourceline)
                toolnames.append(toolname)


    # write to disk
    #------------------------------------------------------------
    # paths
    path_snippets    = path_VEX_db + "tab_vex_snippets.db"
    path_nodenames   = path_VEX_db + "tab_vex_nodenames.db"
    path_sourcefiles = path_VEX_db + "tab_vex_sourcefiles.db"
    path_sourcelines = path_VEX_db + "tab_vex_sourcelines.db"
    path_toolnames   = path_VEX_db + "tab_vex_toolnames.db"
    # files
    file_snippets    = open( path_snippets, 'wb')
    file_nodenames   = open( path_nodenames, 'wb')
    file_sourcefiles = open( path_sourcefiles, 'wb')
    file_sourcelines = open( path_sourcelines, 'wb')
    file_toolnames   = open( path_toolnames, 'wb')
    # write
    pickle.dump(snippets, file_snippets )
    pickle.dump(nodenames, file_nodenames )
    pickle.dump(sourcefiles, file_sourcefiles )
    pickle.dump(sourcelines, file_sourcelines )        
    pickle.dump(toolnames, file_toolnames )
    # close
    file_snippets.close()
    file_nodenames.close()
    file_sourcefiles.close()
    file_sourcelines.close()
    file_toolnames.close()
