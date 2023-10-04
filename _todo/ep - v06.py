ZASADNI OTAZKY:


    @ jak nazveme ten system?


    @ sampler_primuv je hda?
        ano a ma multiparm

    @ jsou dva druhy PRIMUV? point / line?
        asi ne, kdyz je pocet divisions 1, tak se generuje bod

    @ vystup primuv je polygon?
        ano ()

    @ jak udelat, aby dve PATH navazoval smer?
        resit to u jednotlivych eps atd je hodne prace
        attribute blur?
        connector line muze

    @ position smooth lag 
        animovany atribut (pro kazdou @ id linku)
        linka uz je cela hotova, ale neni na svem miste
        jak ho udelat parametricky? protoze nejde animovat jako parm... spis jako timeshift?

    @ pro kazdy typ generovani linek je vlastni HDA?
        asi jo!

    @ kam dat clumping?
        zvlast HDA, ruzne typy

    @ kam dat info o leak_type?


    @ vice targetu naraz


    @ co kdyz target je point?
        konverze na krivku? kazdy target ma aspon tri body?
            0:   in
            end: out

    @ jak se jmenujou atributy? dim+coord+fill


    @ jak se jmenujou typy fill / connector?


    @ musi byt na stridacku fill / nofill?



----------------------------------------------------------
##########################################################
#############    ABOVE TARGET nastroje     ###############
##########################################################


def clumping()
    # podle id, misto... na zacatku / na konci)



def reverse_detector()
    # podle blizkosti k bodu, podle vektoru?)
    # podle id?



def match_id()
    # id podle PREDCHOZIHO optimal transport)



def coord_from_trail()
    # cam/pop = musime prevest na DIM + COORD + SPREAD)
    



def create_connector()

    b-spline, nebo polyline?
    ramp, jak blizko jdou LINES k bodum?
        smer - podle polohy bodu
        delka vystupu, podle world vzdalenosti tech targetu






----------------------------------------------------------


def SAMPLER_PRIMUV ()
    TARGET je vzdycky referencovane jako Spare

    
    
    prim parametry:

        @fill
        @leak_pos
        @leak_fill


    druhy:
        polygon
            eps                                 @type:    fill
            silhouette                          @type:    fill
            isocurves                           @type:    fill
            omotavky                            @type:    fill
            flat multiline stroke sweep         @type:    
            two points (scatter on geometry)
            dop swirls
            connector


----------------------------------------------------------


FILL
    dva druhy
        animovana klasika - dim+coord
      - neighbours dim+coord

