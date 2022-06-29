import hou
import os
import wf_selection
from shutil import copyfile



def generate_html() :


    # TODO:
    #------------------------------------------------------------
    # category.XPU
    # category.VELLUM
    # category.UNREAL
    # category.SIMULATION



    # init variables
    #------------------------------------------------------------
    # {"mus_path":       "Q:/_packages/ep_ikoon"},
    library_root = hou.getenv("mus_path") + "/_library/"
    web_root     = hou.getenv("mus_path") + "/_web/"


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
        # read categories
        # read weight
        # replace category
        # change to lowercase







    src_py     = "python2.7libs/"
    src_shelf  = "toolbar/"
        

        # shelf
        try :
            src = root + src_shelf + "wf_" + file + ".shelf"
            dst = root + git + src_shelf + "/wf_" + file + ".shelf"
            copyfile(src, dst)
        except :
            pass

    # write index.html to disk
    #------------------------------------------------------------
    # paths
    # for (filenum, file) in enumerate(files):
    #     path_html = dir_root + dir_blog + file + ".html"
    #     file_html = open( path_html )

    # xml_data += xml_end
    # file_xml = open( path_xml, 'w' )
    # file_xml.write(xml_data)    
        


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


