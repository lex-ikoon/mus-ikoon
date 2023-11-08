##########################################################
#############            OTAZKY            ###############
##########################################################

@jak vyresit barevnost





##########################################################
#############    ABOVE TARGET nastroje     ###############
##########################################################

def "xe // lines / connector"

    NO resample
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


def "xe // lines / convert points" # three points
def "xe // lines / convert trails" # cam/pop = musime prevest na DIM + COORD + SPREAD)
def "xe // lines / dop swirls"
def "xe // lines / dop system"
def "xe // lines / eps"
def "xe // lines / intersect planes"
def "xe // lines / isocurves"
def "xe // lines / multiline sweep"
def "xe // lines / silhouette"
def "xe // lines / wrap"


-------------------------------------------------------------------

def "xf // animate / dim"
    - by id
    - linear / radial / vdb / id / "dim"


def "xf // animate / fill"
    - spread


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





##########################################################
#############           TARGET             ###############
##########################################################


def "xg // target"

    uvnitr je timeshift

    parm:
        spread_smooth timeshift?

    prim parametry:
        @dim
        @coord
        @spread

##########################################################
#############           SAMPLER            ###############
##########################################################



def "xg // sampler"

    asi na tom muze byt help
    AUTO / COORD

    parm:
        tog / first target is connector (to se zjisti z prvniho targetu)
        ------------
        int / pocet id #to musi byt vsude stejne
        ------------
        tog / output line #pokud ne, tak je to jen bod
        int / divisions

    uvnitr:


    VEX (over points):
        - najde vsechny targety (0-2-4 nebo 1-3)
        - na vsech najde coord
        - NE pocitam s tim, ze coord je 0-1 pouze na dvou targetech
        - spocita se COORD podel cele lajny
            - proste soucet vsech COORD
            # - vazeny prumer kazdeho targetu ... vaha je nizka u koncu
            # - kdyz je vedle sebe 1 a 0 ??? ... tak by u connection melo byt 0.5

        - musime zjistit, kam patri tento bod v ramci divisions
            - bod ma svoje @curveu
            - zjistime fill_to_coord (od-do)
        
        - samplujeme pozici
            - vzdy se sampluji dva sousedni targety, kvuli spread_smooth
            - podle toho, jak moc 

        # - dopocita se coord na vsech targetech
        #     - prev targetu (pokud < 0.5 )
        #     - next targetu (pokud > 0.5 )




