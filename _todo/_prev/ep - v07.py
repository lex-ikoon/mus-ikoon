ZASADNI OTAZKY:

    # @ jak nazveme ten system?
    #     xf // 

    # @ sampler_primuv je hda?
    #     ano a ma multiparm

    # @ jsou dva druhy PRIMUV? point / line?
    #     asi ne, kdyz je pocet divisions 1, tak se generuje bod

    # @ vystup primuv je polygon nebo bod?
    #     kdyz je pocet divisions 1, tak se generuje bod

    # @ jak udelat, aby dve PATH navazoval smer?
        # to bude delat jen connector line
        # resit to u jednotlivych eps atd je hodne prace

    # @ pro kazdy typ generovani linek je vlastni HDA?
    #     asi jo!

    # @ kam dat clumping?
    #     zvlast HDA

    # @co kdyz to ma jit naraz connA/targetA a pak targetB/connB???
    #     tak se to vyresi pomoci coord na targetech
    #     target A+B musi byt merge do jednoho
    #     conn  A+B musi byt merge do jednoho


    # @ kam dat info o target_type?
    #     neni to nahodou vzdy a b a b a b a b a ? 
    #     musi byt na stridacku fill / nofill?
    #     JO

    # @ vice targetu naraz
    #     to se resi pomoci id a stejneho time


    # @ jak se jmenujou atributy? dim+coord+spread


    # @ jak se jmenujou typy fill / connector?


    @ position smooth lag
        "linka uz je cela hotova, ale neni na svem miste"
        nastaveny u targetu
        vyresi to vetsi spread?
        dopredu zvlast, dozadu zvlast?
        spread_smooth_pos


    @ co kdyz target je point?
        konverze na krivku? kazdy target ma dva/tri body?
            0-1:    smer in
            1-2:    smer out

    @ musime vyresit spread >1



##########################################################
#############    ABOVE TARGET nastroje     ###############
##########################################################


def "xe // create / connection"
def "xe // create / dop swirls"
def "xe // create / eps"
def "xe // create / isocurves"
def "xe // create / multiline sweep"
def "xe // create / wrap"
def "xe // create / scatter" # three points
def "xe // create / silhouette"


def "xf // connection / clumping"
    # podle id, misto... na zacatku / na konci)



def "xf // connection / reverse detector"
    # podle blizkosti k bodu, podle vektoru?)
    # podle id?



def "xf // connection / match id"
    # id podle PREDCHOZIHO optimal transport)



def "xf // connection / coord from trail"
    # cam/pop = musime prevest na DIM + COORD + SPREAD)
    

def "xf // create connection"

    b-spline, nebo polyline?
    polyline ma vyhodu, ze
    ramp, jak blizko jdou LINES k bodum?
        smer - podle polohy bodu
        delka vystupu, podle world vzdalenosti tech targetu



##########################################################
#############           TARGET             ###############
##########################################################


def "xf // target"

    jakoby null
    parm:
        spread_smooth mult?

    prim parametry:
        @dim
        @coord
        @spread

##########################################################
#############           SAMPLER            ###############
##########################################################



def "xf // sampler primuv"

    parm:
        # - first target is connector (to se zjisti z prvniho targetu)


    VEX (over points):
        - najde vsechny targety (0-2-4 nebo 1-3)
        - na vsech najde coord
        - NE pocitam s tim, ze coord je 0-1 pouze na dvou targetech
        - dopocita se coord na vsech targetech
            - prev targetu (pokud < 0.5 )
            - next targetu (pokud > 0.5 )

        - mame pro kazdy target coord, tak:
        - musime zjistit, kam patri tento bod 
        - @curveu
        - vzdy se sampluji dva targety, kvuli spread_smooth


