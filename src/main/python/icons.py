import logging
logging.info(f"{__file__}")
import qtawesome as qta

def get_icon(oid):
    return qta.icon(oid,
                        color='blue',
                        color_active='orange',
                        opacity=0.7)
                        
icon_app_main = get_icon('mdi.google-analytics')

icon_db_refresh = get_icon("mdi.database-refresh")

icon_app_search = get_icon("fa5s.search-location")

icon_app_mainwin = get_icon('fa5s.globe')

icon_app_clean = get_icon("mdi.delete-forever")

icon_general_next = get_icon("mdi.skip-next")
icon_general_prev = get_icon("mdi.skip-previous")

icon_question = get_icon("mdi.comment-question-outline")

icon_metrics_new = get_icon("mdi.new-box")
icon_metrics_show     = get_icon("fa5s.envelope-open-text")
icon_metrics_rename = get_icon("fa5s.envelope-open-text")
icon_metrics_import   = get_icon("mdi.database-import")
icon_metrics_export   = get_icon("mdi.database-export")
icon_metrics_file      = get_icon("fa5.file-alt")
icon_metrics_sqlite   = get_icon("fa.database")
icon_metrics_excel    = get_icon("fa5.file-excel")

icon_metrics_open = get_icon("mdi.folder-open-outline")
icon_metrics_save = get_icon("mdi.content-save-all-outline")
icon_metrics_save_as = get_icon("mdi.content-save-move-outline")
icon_metrics_close = get_icon("mdi.close-box-multiple-outline")
icon_metrics_new_metrics = get_icon("mdi.newspaper-plus")
icon_metrics_new_group = get_icon("mdi.account-group-outline")
icon_metrics_modify = get_icon("fa5s.exchange-alt")
icon_metrics_insert = get_icon("fa5.address-card")
icon_metrics_export_template = get_icon("mdi.application-export")
icon_metrics_remove = get_icon("mdi.playlist-remove")
icon_metrics_input_matrix = get_icon("mdi.matrix")
icon_metrics_weight = get_icon("mdi.weight-lifter")
icon_metrics_weight_sum = get_icon("mdi.view-grid-plus-outline")
icon_metrics_weight_sqrt = get_icon("mdi.square-root")
icon_metrics_weight_eign = get_icon("mdi.format-line-weight")
icon_metrics_weight_msr = get_icon("fa.meanpath")

icon_delete         = get_icon("mdi.text-box-remove-outline")

icon_data_eval = get_icon("mdi.file-table-box-outline")

icon_eval_table     = get_icon("mdi.file-table-box-outline")
icon_eval_hist  = get_icon("mdi.chart-histogram")
icon_eval_scatter = get_icon('mdi.chart-scatter-plot-hexbin')
icon_eval_joint = get_icon("mdi.chart-scatter-plot-hexbin")
icon_eval_pie = get_icon("mdi.chart-pie")
icon_eval_radar = get_icon("mdi.radar")
icon_eval_sys = get_icon("mdi.file-tree-outline")
icon_eval_add = get_icon("fa5s.plus-circle")
icon_eval_rem = get_icon("mdi.minus-circle")
icon_eval_run = get_icon("mdi.run-fast")

icon_searchbar = get_icon("fa5b.searchengin")
icon_searchbar_remove = get_icon("mdi.text-box-remove-outline")
icon_next = get_icon("mdi.page-next-outline")
icon_prev = get_icon("mdi.page-previous-outline")