
----------------------------------------------------------
lines__normal__through_waypoints
    bod (0) a (n-2) a posledni body podle normal?
    ramp, jak blizko jdou LINES k bodum?
    - smer vystupu
    - delka vystupu

----------------------------------------------------------


jak udelat, aby dve PATH navazovaly?
    - aby navazoval smer 
    - aby navazovala rychlost



----------------------------------------------------------


VICE TARGETU NARAZ
    sampler matchuje ("obarvuje") pro @id atribut a timelinu
    neco jako:
        dim         je tady     atribut na @id lince s hodnotama 0-RFEND
        coord       je tady     parametr z timeliny s hodnotama  0-RFEND
        fill        je tady     to co vidime

    na @id lince se ABOVE TARGET k bodum zapisuje @timedim 0-RFEND (je to prostredek carve???)
    na @id lince se ABOVE TARGET k bodum zapisuje aktualni delka

    co kdyz chceme, aby linka byla videt dlouho?
    muze se viditelnost na @id lince definovat pomoci @Cd?
    muze sampler hledat zacatek @Cd a konec @Cd?


    kdyz je zacatek/konec uncut, tak pocitame prechod?


----------------------------------------------------------

ABOVE TARGET nastroje
    clumping (podle id, misto... na zacatku / na konci)
    normal blend (srovnavac koncu)
    reverse detektor (podle blizkosti k bodu, podle vektoru?)
    match_id (id podle PREDCHOZIHO optimal transport)
    animate Cd
    animate coord 

----------------------------------------------------------


def SAMPLER_PRIMUV ()
    nositel COORD je TARGET
    jak funguje COORD u linek?
    jak funguje COORD u bodu?

    vystup PRIMUV:
        dvadruhy PRIMUV? TODO
        bod?
        krivka?

----------------------------------------------------------

COORD + LENGTH?
    {0.0, 1.0}

----------------------------------------------------------


# TIMING
#     - na path je FILL? nebo COORD?


----------------------------------------------------------

TARGET:
    je vzdycky referencovane jako Spare
    
    prim parametry:
        @N_in
        @N_out
        @m_in
        @m_out
        @coord


    vetsinou je animovany:
        poly:       YES
        point:      YES
        b-spline:   YES


    druhy:
        polygon
            eps                             @Cd cut:    
            silhouette                      @Cd cut:    
            isocurves                       @Cd cut:    
            omotavky                        @Cd cut:    
            flat multiline stroke sweep     @Cd cut:    

        point
            scatter on geometry 
            trasa bodu z kamery (jeden animovany bod)
            trasy POP animace   (trasa?)

        b-spline
            connector

