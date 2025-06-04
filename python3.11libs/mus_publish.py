import hou
import os
import re
import wf_selection
# import mus_tabulate
from shutil import copyfile



# --------------------------------------------------------------------------------------------------------------------------------

def atoi (string) :
    integer  = 0
    for char in string:
        integer = integer * 10 + ord(char) - ord("0")
    return integer 

# --------------------------------------------------------------------------------------------------------------------------------

def validate_unix (text) :
    return re.sub("[^0-9a-zA-Z\.]+", "_", text)


# --------------------------------------------------------------------------------------------------------------------------------
def file_find (directory, extension) :

    result = "None"

    for file in os.listdir(directory) :
        if file.endswith("." + extension) :
            result = file.split(".")[0]
    
    if result == "None" :
        if extension == "weight":
            return 0
        if extension == "inspiration":
            return "unknown"
    else:
        if extension == "weight":
            return atoi(result)
        if extension == "inspiration":
            return result


# --------------------------------------------------------------------------------------------------------------------------------
def file_date (file_path) :
    try:
        date = os.path.getmtime(file_path)
        return date
    except:
        return 0


# --------------------------------------------------------------------------------------------------------------------------------


def mus_generate_html () :

    # init variables
    # -----------------------------------------------------------------------------
    weight_minimum_mus = 0
    weight_minimum_www = 0
    new_total_count    = 6



    # init variables
    # -----------------------------------------------------------------------------
    mus_cats = ["flip", "kinefx", "pyro", "rbd", "rnd_tools", "vellum", "vex", "cop"]

    mus_root = "Q:/_mus/"
    out_root_mus = "Q:/_mus/__publish/__out_mus/"
    out_root_www = "Q:/_mus/__publish/__out_www/"

    web_root_mus = "Q:/_mus/__publish/templates/mus/"
    web_root_www = "Q:/_mus/__publish/templates/www/"


    # read index header and footer
    # -----------------------------------------------------------------------------
    with open(web_root_mus + "video_template.html") as video_template_mus: html_video_mus = video_template_mus.read()
    with open(web_root_www + "video_template.html") as video_template_www: html_video_www = video_template_www.read()

    with open(web_root_mus + "index_template.html") as index_template_mus: html_index_mus = index_template_mus.read()
    with open(web_root_www + "index_template.html") as index_template_www: html_index_www = index_template_www.read()

    video_template_mus.close()
    video_template_www.close()

    index_template_mus.close()
    index_template_www.close()

    find_FOOTER_mus = html_index_mus.find("<!-- FOOTER -->")
    find_FOOTER_www = html_index_www.find("<!-- FOOTER -->")
    find_HEADER_mus = html_index_mus.find("<!-- HEADER -->")
    find_HEADER_www = html_index_www.find("<!-- HEADER -->")
    html_footer_mus = html_index_mus[find_FOOTER_mus:]
    html_footer_www = html_index_www[find_FOOTER_www:]
    html_header_mus = html_index_mus[:find_HEADER_mus]
    html_header_www = html_index_www[:find_HEADER_www]


    # init lists
    # -----------------------------------------------------------------------------
    MUS_job_names    = []
    MUS_mp4_src      = []
    MUS_dates        = []
    MUS_categories   = []
    MUS_weights      = []
    MUS_inspirations = []
    MUS_news         = []


    # fill lists
    # -----------------------------------------------------------------------------
    for mus_cat in mus_cats:

        # collect all jobs
        # ------------------------------------
        job_names = []
        jobs_root = mus_root + mus_cat
        for job_name in os.listdir(jobs_root) :
            if os.path.isdir(os.path.join(jobs_root, job_name)) :
                job_names.append(job_name)


        # each job 
        # ------------------------------------
        for job_name in job_names :

            job_path    = mus_root + mus_cat + "/" + job_name
            mp4_src     = job_path + "/_out/out_web.mp4"
            date        = file_date(mp4_src)
            weight      = file_find(job_path, "weight")
            inspiration = file_find(job_path, "inspiration")

            # check validity   
            # --------------
            valid = 1
            if weight < weight_minimum_mus :
                valid = 0
            if not os.path.exists(mp4_src) :
                valid = 0

            # append if valid
            # --------------
            if valid == 1 :
                MUS_job_names.append(job_name)
                MUS_mp4_src.append(mp4_src)
                MUS_dates.append(date)
                MUS_categories.append(mus_cat)
                MUS_weights.append(weight)
                MUS_inspirations.append(inspiration)
                MUS_news.append(False)



    # find NEW in list
    # -----------------------------------------------------------------------------

    index                = MUS_dates
    MUS_job_names_new    = [x for (y,x) in sorted(zip(index,MUS_job_names)     , key=lambda pair: pair[0] , reverse=True )]
    MUS_mp4_src_new      = [x for (y,x) in sorted(zip(index,MUS_mp4_src)       , key=lambda pair: pair[0] , reverse=True )]
    MUS_dates_new        = [x for (y,x) in sorted(zip(index,MUS_dates)         , key=lambda pair: pair[0] , reverse=True )]
    MUS_categories_new   = [x for (y,x) in sorted(zip(index,MUS_categories)    , key=lambda pair: pair[0] , reverse=True )]
    MUS_weights_new      = [x for (y,x) in sorted(zip(index,MUS_weights)       , key=lambda pair: pair[0] , reverse=True )]
    MUS_inspirations_new = [x for (y,x) in sorted(zip(index,MUS_inspirations)  , key=lambda pair: pair[0] , reverse=True )]
    MUS_news_new         = [x for (y,x) in sorted(zip(index,MUS_news)          , key=lambda pair: pair[0] , reverse=True )]

    for i in range(0, new_total_count-1) :
        MUS_news_new[i] = True


    # sort by weight
    # -----------------------------------------------------------------------------

    index            = MUS_weights_new
    MUS_job_names    = [x for (y,x) in sorted(zip(index,MUS_job_names_new)     , key=lambda pair: pair[0] , reverse=True )]
    MUS_mp4_src      = [x for (y,x) in sorted(zip(index,MUS_mp4_src_new)       , key=lambda pair: pair[0] , reverse=True )]
    MUS_dates        = [x for (y,x) in sorted(zip(index,MUS_dates_new)         , key=lambda pair: pair[0] , reverse=True )]
    MUS_categories   = [x for (y,x) in sorted(zip(index,MUS_categories_new)    , key=lambda pair: pair[0] , reverse=True )]
    MUS_weights      = [x for (y,x) in sorted(zip(index,MUS_weights_new)       , key=lambda pair: pair[0] , reverse=True )]
    MUS_inspirations = [x for (y,x) in sorted(zip(index,MUS_inspirations_new)  , key=lambda pair: pair[0] , reverse=True )]
    MUS_news         = [x for (y,x) in sorted(zip(index,MUS_news_new)          , key=lambda pair: pair[0] , reverse=True )]


    # preview lists
    # -----------------------------------------------------------------------------

    # print(MUS_job_names_new)
    # print(MUS_mp4_src_new)
    # print(MUS_dates_new)
    # print(MUS_categories_new)
    # print(MUS_weights_new)
    # print(MUS_inspirations_new)


    # apply lists
    # -----------------------------------------------------------------------------

    html_mus = html_header_mus
    html_www = html_header_www

    for index in range(len(MUS_job_names)):

        # MP4 newname    ------------------
        MUS_mp4_newname = MUS_categories[index] + "___" + validate_unix(MUS_job_names[index]) + ".mp4" 

        # MP4 copy MUS   ------------------
        src = MUS_mp4_src[index]
        dst = out_root_mus + "vid/" + MUS_mp4_newname
        copyfile(src, dst)

        # MP4 copy WWW   ------------------
        if MUS_weights[index] > (weight_minimum_www-1) :
            dst = out_root_www + "vid/" + MUS_mp4_newname
            copyfile(src, dst)

        # category update    ------------------
        MUS_category = MUS_categories[index]
        if MUS_news[index] :
             MUS_category += " new"

        # job directory for clipboard    ------------------
        MUS_job_directory = mus_root + MUS_categories[index] + "/" + MUS_job_names[index]

        # prepare inspiration ------------------
        if MUS_inspirations[index] == "unknown" :
            MUS_inspiration = ""
        else :
            MUS_inspiration = '<div class="credit-text scale-anm all rbd"> Based on R&D by: '
            MUS_inspiration += MUS_inspirations[index]
            MUS_inspiration += "</div>"

        # customize VIDEO template MUS   ------------------
        html_video_job_mus = html_video_mus
        html_video_job_mus = html_video_job_mus.replace("CATEGORIES",  MUS_category  )
        html_video_job_mus = html_video_job_mus.replace("JOB_DIRECTORY",  MUS_job_directory  )
        html_video_job_mus = html_video_job_mus.replace("MP4_NEW_NAME", "vid/" + MUS_mp4_newname   )
        html_video_job_mus = html_video_job_mus.replace("<!-- INSPIRATION -->",  MUS_inspiration  )


        # customize VIDEO template WWW   ------------------
        html_video_job_www = html_video_www
        html_video_job_www = html_video_job_www.replace("CATEGORIES",  MUS_category  )
        html_video_job_www = html_video_job_www.replace("JOB_DIRECTORY",  MUS_job_directory  )
        html_video_job_www = html_video_job_www.replace("MP4_NEW_NAME", "vid/" + MUS_mp4_newname   )
        html_video_job_www = html_video_job_www.replace("<!-- INSPIRATION -->",  MUS_inspiration  )

        # append completed video    ------------------
        html_mus += html_video_job_mus
        html_www += html_video_job_www



    # append footer
    # -----------------------------------------------------------------------------
    html_mus += html_footer_mus
    html_www += html_footer_www


    # write index.html to disk
    # -----------------------------------------------------------------------------
    # paths
    path_html_mus = out_root_mus + "index.html"
    path_html_www = out_root_www + "index.html"
    file_html_mus = open( path_html_mus, 'w' )
    file_html_www = open( path_html_www, 'w' )
    file_html_mus.write(html_mus)
    file_html_www.write(html_www)




    # -----------------------------------------------------------------------------
    # update the README.md
    # -----------------------------------------------------------------------------

    web_root_mus_git = "Q:/_mus/__publish/templates/mus_git/"

    # read index header and footer
    # -----------------------------------------------------------------------------
    with open(web_root_mus_git + "README.md") as readme_template_file:
        readme_template = readme_template_file.read()

    readme_template_file.close()


    find_HEADER_md = readme_template.find("<!-- HEADER -->")
    find_FOOTER_md = readme_template.find("<!-- FOOTER -->") + 16
    readme_header  = readme_template[:find_HEADER_md]
    readme_footer  = readme_template[find_FOOTER_md:]

    readme_new = readme_header

    for index in range(len(MUS_job_names_new)):
        line  = (MUS_categories_new[index]+":").ljust(16, " ")
        line += MUS_job_names_new[index].ljust(60, " ")
        if MUS_news_new[index] :
            line += " // NEW"
        readme_new += line + "\n"
        
    readme_new += readme_footer

    path_readme_new = "Q:/_gd/houdini_packages/mus_ikoon/README.md"
    file_readme_new = open( path_readme_new, 'w' )
    file_readme_new.write(readme_new)



    # -----------------------------------------------------------------------------
    # everything is done :)
    # -----------------------------------------------------------------------------

