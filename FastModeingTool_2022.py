import os
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QDockWidget
from PySide2.QtWidgets import QPushButton,QRadioButton,QSlider
from PySide2.QtCore import QFile
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
import qtmax
from pymxs import runtime as rt
'''
3dmax2022  
法线工具
继承QDockWidget 版本，窗口属于3dmax工具面板


'''


#继承Qdialog类，代表对话框类
class TestDialog(QDockWidget):
    #TestDialog类的构造函数，传入参数，参数为类类型
    def __init__(self, parent=None):
        # 继承父类的构造方法
        # 经典类的写法： 父类名称.__init__(self, 参数1，参数2，...)
        # 新式类的写法：super(子类，self).__init__(参数1，参数2，....)
        # 当testDialog被实例化之后，调用顺序  自己的__init__ ——> 父类__init__
        super(TestDialog, self).__init__(parent)#经典写法，继承父类的构造函数,也就是拥有父类的属性和方法
        loader = QUiLoader()#QuiLoder类 主要负责加载UI外部文件
        ui_file_path = os.path.join(  os.path.dirname(os.path.realpath(__file__)), 'ui/ui.ui')
        ui_file = QFile(ui_file_path)#打开文件
        ui_file.open(QFile.ReadOnly)#文件只读
        self.ui = loader.load(ui_file, self)#导入ui内部的信息
        ui_file.close()
        #-----
        self.setWindowFlags(QtCore.Qt.Tool)#设置窗口属性，枚举
        self.setWindowTitle("技术中心_FastMdeingToolv1.0")

        self.resize(500, 550)




if __name__ == '__main__':

    try:
        tool_window.close()
        tool_window.deleteLater()

    except:
        pass
    main_window2 = qtmax.GetQMaxMainWindow()
    tool_window = TestDialog(parent=main_window2)
    tool_window.setFloating(True)
    tool_window.show()

