
##########################################################
#############            OTAZKY            ###############
##########################################################

@ jak vyresit barevnost
    - colorize table
    - random along curves:
            hue
            saturation
            value
    - random at start: HSV
    - random at end: HSV
    - similar targetting as clumping?


    
@ vsechny xe lines = maji svoje id? ANO
@ vsechny xe lines = maji grouped first/last points? 


##########################################################
#############    ABOVE TARGET nastroje     ###############
##########################################################

def "xe // curves / connector"

    resample by asi mohl byt?
    b-spline? nebo subdiv curves
    NO smooth


    output polyline #ma vyhodu, ze muze mit podobny sampling jako targety

    @inputy:
        prvni     = vezme dva body (z ledky, z geometrie a podobne)
        uprostred = dalsich X bodu, jak je seradit? merge...
        treti     = vezme dva body (z ledky, z geometrie a podobne)

    @parm:
        -------------
        number of lines

        -------------
        first:
            new points:
                0-10

            direction:
                two last points on the line
                point normals

            distance:
                relative (to next point)
                absolute (unit length)


        -------------
        middle:
            transpose [rows / columns]
            optimal transport to first
            optimal transport to last


        -------------
        last:
            
        -------------

    @priklady:
        z jedne geometrie
                pak kruznice
                pak na geometrii
        z okraju ledky, pak swirl a pak na geometrii
        # podel kamery asi nepotrebujem




-------------------------------------------------------------------


def "xe // curves / connector"
def "xe // curves / divergence trails" 
def "xe // curves / eps"
def "xe // curves / from points"      # three points
def "xe // curves / from trails" # cam/pop = musime prevest na DIM + COORD + SPREAD)
def "xe // curves / intersect planes" #cut in some direction
def "xe // curves / multiline sweep"
def "xe // curves / silhouettes"
def "xe // curves / wrap"


-------------------------------------------------------------------

def "xe // edit / clumping"
    # podle id, misto... na zacatku / na konci)


def "xe // edit / reverse detector"
    # podle blizkosti k bodu, podle vektoru?)
    # podle id?


def "xe // edit / match id"
    # optimal transport
    # 2nd input - previous target


-------------------------------------------------------------------

def "xf // animate / dim"

def "xf // animate / fill"



##########################################################
#############           SAMPLER            ###############
##########################################################



def "xg // sampler"




