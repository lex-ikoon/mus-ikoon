
lines__normal__through_waypoints
    bod (0) a (n-2) a posledni body podle normal?
    ramp, jak blizko jdou LINES k bodum?
    - smer vystupu
    - delka vystupu


jak udelat, aby dve PATH navazovaly?
    - aby navazoval smer 
    - aby navazovala rychlost




TARGET nastroje
    srovnavac koncu
    reverse detektor (podle blizkosti k bodu, podle vektoru?)
    hledac id



def SAMPLER_PRIMUV ()
    nositel COORD je TARGET
    jak funguje COORD u linek?
    jak funguje COORD u bodu?

    vystup PRIMUV:
        dvadruhy PRIMUV? TODO
        bod?
        krivka?


COORD
    {0.0}



TIMING
    - na path je FILL? nebo COORD?


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
            eps
            silhouette
            isocurves
            omotavky

        point
            scatter on geometry
            trasa bodu z kamery (asi radsi jako jeden animovany bod)
            trasy POP animace

        b-spline
            connector

