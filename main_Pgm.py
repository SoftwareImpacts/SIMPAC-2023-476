from objFcn import objUpdate
from ACO_GA_Fcn import acoGA_Fcn
import easygui

if __name__ == '__main__':
    file_path = easygui.fileopenbox(msg="Choose Input File", default=r".\Dataset\*.txt")

    graph = objUpdate(file_path)
    acoGaModel = acoGA_Fcn(graph, 10, 2, 0.1, True)
    acoGaModel.run_ACO_GA_Fcn()
