import logging
logging.info(f"{__file__}")

import sys
from main.python.context import appctxt
from main.python.widget import MainWin
from main.python.appwin import AboutDialog
import qtawesome as qta
import profile

import main.python.parameters as parameters

import main.python.template.tempview as tempview

if 1:

    # application style
    # read qss
    qss_files = [
        "style_clean_base.qss",
        "style_clean_sidebar.qss",
        "style_clean_header.qss",
        "style_clean_table.qss",
        "style_clean_tree.qss",
        "style_clean_view_item.qss",
        "style_clean_menu.qss",
        "style_qtabwidget.qss",
        "style_app.qss",
        "style_scrollbar.qss",
        "style_dlg.qss",
    ]
    def qss_text(p) :
        with open(appctxt.get_resource(p), "r") as f:
            qss = f.read()
            return qss    
    appctxt.app.setStyleSheet( "\n".join([qss_text(p) for p in qss_files]))

    if 1: # about dialog
        about = AboutDialog() 
        about.setWindowTitle(parameters.application_title)
        # about.show()

    if 1: # main windows
        main = MainWin()        
        from main.python.icons import icon_app_mainwin
        main.setWindowIcon(icon_app_mainwin)
        main.sigAbout.connect(lambda _ : about.show())

        main.addPage(tempview.TempView(main))

        main.setCurrent(0)

        # main.showMaximized() #(1300, 800)
        # main.resize(1920, 960)
        main.resize(1366, 768)
        main.show()

        main.setTitle(parameters.application_title)
        main.setIcon(icon_app_mainwin.pixmap(64, 64))

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)



# if __name__ == '__main__':
#     # profile.run("run()")
#     run()