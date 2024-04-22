definition = hou.node('/obj/geo1/curves_connector').type().definition()
definition.copyToHDAFile("Q:/xe_curves_eps.hdalc",                   "xe::curves_eps::1.0",                             "xe // curves / eps"                       )
definition.copyToHDAFile("Q:/xe_curves_from_points.hdalc",           "xe::curves_from_points::1.0",                     "xe // curves / from points"                       )
definition.copyToHDAFile("Q:/xe_curves_from_trails.hdalc",           "xe::curves_from_trails::1.0",                     "xe // curves / from trails"                       )
definition.copyToHDAFile("Q:/xe_curves_intersect_planes.hdalc",      "xe::curves_intersect_planes::1.0",                "xe // curves / intersect planes"                       )
definition.copyToHDAFile("Q:/xe_curves_multiline_sweep.hdalc",       "xe::curves_multiline_sweep::1.0",                 "xe // curves / multiline sweep"                       )
definition.copyToHDAFile("Q:/xe_curves_silhouettes.hdalc",           "xe::curves_silhouettes::1.0",                     "xe // curves / silhouettes"                       )
definition.copyToHDAFile("Q:/xe_curves_wrap.hdalc",                  "xe::curves_wrap::1.0",                            "xe // curves / wrap"                       )
definition.copyToHDAFile("Q:/xe_edit_clumping.hdalc",                "xe::edit_clumping::1.0",                          "xe // edit / clumping"                       )
definition.copyToHDAFile("Q:/xe_edit_match_id.hdalc",                "xe::edit_match_id::1.0",                          "xe // edit / match id"                       )
definition.copyToHDAFile("Q:/xe_edit_reverse_detector.hdalc",        "xe::edit_reverse_detector::1.0",                  "xe // edit / reverse detector"                       )
definition.copyToHDAFile("Q:/xf_animate_dim.hdalc",                  "xf::animate_dim::1.0",                            "xf // animate / dim"                       )
definition.copyToHDAFile("Q:/xf_animate_fill.hdalc",                 "xf::animate_fill::1.0",                           "xf // animate / fill"                       )
definition.copyToHDAFile("Q:/xf_target.hdalc",                       "xf::target::1.0",                                 "xf // target"                       )
definition.copyToHDAFile("Q:/xg_sampler.hdalc",                      "xg::sampler::1.0",                                "xg // sampler"                       )




definition.copyToHDAFile("Q:/edit.hdalc","aaaa","bbb")
file_name  = "Q:/edit.hdalc"
type_name  = "aaaa"
label      = "bbb"

definition.copyToHDAFile(file_name, type_name, label)


@separator





