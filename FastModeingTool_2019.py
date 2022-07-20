import os
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QDockWidget
from PySide2.QtWidgets import QPushButton,QRadioButton,QSlider,QLineEdit,QCheckBox
from PySide2.QtCore import QFile
from PySide2 import QtCore
from PySide2.QtUiTools import QUiLoader
#import qtmax
from pymxs import runtime as rt
from PySide2 import QtWidgets
import pymxs

import MaxPlus
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
        # 经典写法，继承父类的构造函数,也就是拥有父类的属性和方法
        super(TestDialog, self).__init__(parent)

        # 实列化QuiLoder对象， 主要负责加载UI外部文件
        loader = QUiLoader()
        ui_file_path = os.path.join(  os.path.dirname(os.path.realpath(__file__)), 'ui/ui.ui')

        # 打开文件
        ui_file = QFile(ui_file_path)

        # 文件只读
        ui_file.open(QFile.ReadOnly)

        # 导入ui内部的信息
        self.ui = loader.load(ui_file, self)
        ui_file.close()


        # 设置窗口属性
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setWindowTitle("技术中心_日常效率工具")


        self.creatwidget()
        self.creatconnection()



        self.resize(316, 478)

    def creatwidget(self):
        self.radio_coord_local = self.ui.findChild(QRadioButton,"radioButton_3")
        self.radio_coord_view = self.ui.findChild(QRadioButton, "radioButton")
        self.radio_coord_world = self.ui.findChild(QRadioButton, "radioButton_2")
        self.radio_coord_screen = self.ui.findChild(QRadioButton, "radioButton_8")

        self.radio_constrations_none = self.ui.findChild(QRadioButton, "radioButton_4")
        self.radio_constrations_edge = self.ui.findChild(QRadioButton, "radioButton_6")
        self.radio_constrations_face = self.ui.findChild(QRadioButton, "radioButton_7")
        self.radio_constrations_normal = self.ui.findChild(QRadioButton, "radioButton_5")

        self.button_collstack = self.ui.findChild(QPushButton,"pushButton_21")
        self.button_xform = self.ui.findChild(QPushButton, "pushButton_22")
        self.button_pivot_to_center = self.ui.findChild(QPushButton, "pushButton_25")
        self.button_obj_to_zero = self.ui.findChild(QPushButton, "pushButton_20")

        self.button_lock_selection = self.ui.findChild(QPushButton, "pushButton")
        self.button_unlock_selection = self.ui.findChild(QPushButton, "pushButton_2")

        self.button_open_maxfile = self.ui.findChild(QPushButton, "pushButton_23")
        self.button_save_backupfile = self.ui.findChild(QPushButton, "pushButton_16")
        self.button_save_selectfile = self.ui.findChild(QPushButton, "pushButton_17")

        self.button_fbx_setting = self.ui.findChild(QPushButton, "pushButton_6")
        self.button_select_path = self.ui.findChild(QPushButton, "pushButton_7")

        self.button_exportCharacter = self.ui.findChild(QPushButton, "pushButton_9")
        self.button_exportEnvirtonment = self.ui.findChild(QPushButton, "pushButton_10")

        self.lineedit_exportPath = self.ui.findChild(QLineEdit, "lineEdit")
        self.lineedit_exportName = self.ui.findChild(QLineEdit, "lineEdit_2")

        self.checkbox_yUp = self.ui.findChild(QCheckBox, "checkBox")
        # self.button_save_selectfile = self.ui.findChild(QPushButton, "pushButton_17")

        self.button_one_material = self.ui.findChild(QPushButton,"pushButton_24")
        self.button_mulity_material = self.ui.findChild(QPushButton, "pushButton_26")
        self.button_clear_material = self.ui.findChild(QPushButton, "pushButton_27")
        self.button_clear_materialColor = self.ui.findChild(QPushButton, "pushButton_28")

        self.button_open_uv = self.ui.findChild(QPushButton, "pushButton_29")
        self.button_bake = self.ui.findChild(QPushButton, "pushButton_30")

        self.button_clone_node = self.ui.findChild(QPushButton, "pushButton_18")
        self.button_pivot_to_zero = self.ui.findChild(QPushButton, "pushButton_19")

        self.button_cut = self.ui.findChild(QPushButton,"pushButton_3")
        self.button_LoopEdge = self.ui.findChild(QPushButton, "pushButton_4")
        self.button_MergePoint = self.ui.findChild(QPushButton, "pushButton_5")
        self.button_Remove = self.ui.findChild(QPushButton, "pushButton_12")
        self.button_TargetWeld = self.ui.findChild(QPushButton, "pushButton_11")
        self.MakePlane_One = self.ui.findChild(QPushButton, "pushButton_8")

        self.button_plane = self.ui.findChild(QPushButton, "pushButton_13")
        self.button_box = self.ui.findChild(QPushButton, "pushButton_14")
        self.button_cyliner = self.ui.findChild(QPushButton, "pushButton_15")
        self.button_sphere = self.ui.findChild(QPushButton, "pushButton_31")

        self.checkbox_pivot_0 = self.ui.findChild(QCheckBox,"checkBox_3")
        self.checkbox_pos_0 = self.ui.findChild(QCheckBox, "checkBox_4")
        self.checkbox_recorve_pivot = self.ui.findChild(QCheckBox, "checkBox_2")




    def creatconnection(self):
        self.radio_coord_local.toggled.connect(lambda: self.set_coord(0))
        self.radio_coord_view.toggled.connect(lambda: self.set_coord(1))
        self.radio_coord_world.toggled.connect(lambda: self.set_coord(2))
        self.radio_coord_screen.toggled.connect(lambda: self.set_coord(3))

        self.radio_constrations_none.toggled.connect(lambda: self.set_constrations(0))
        self.radio_constrations_edge.toggled.connect(lambda: self.set_constrations(1))
        self.radio_constrations_face.toggled.connect(lambda: self.set_constrations(2))
        self.radio_constrations_normal.toggled.connect(lambda: self.set_constrations(3))

        self.button_collstack.clicked.connect(self.collstack)
        self.button_xform.clicked.connect(self.xform)
        self.button_pivot_to_center.clicked.connect(self.pivot_to_center)
        self.button_obj_to_zero.clicked.connect(self.obj_to_zero)

        self.button_lock_selection.clicked.connect(lambda: self.lock_selection(0))
        self.button_unlock_selection.clicked.connect(lambda: self.lock_selection(1))


        self.button_open_maxfile.clicked.connect(self.open_maxfile)
        self.button_save_backupfile.clicked.connect(self.save_backupfile)
        self.button_save_selectfile.clicked.connect(self.save_selectfile)

        self.button_fbx_setting.clicked.connect(self.fbx_setting)
        self.button_select_path.clicked.connect(self.select_path)


        self.button_exportCharacter.clicked.connect(self.export_fbx_unity_character)
        self.button_exportEnvirtonment.clicked.connect(self.export_fbx_unity_envir)

        self.button_one_material.clicked.connect(self.one_material)
        self.button_mulity_material.clicked.connect(self.mulity_material)
        self.button_clear_material.clicked.connect(self.clear_material)
        self.button_clear_materialColor.clicked.connect(self.clear_materialColor)

        self.button_open_uv.clicked.connect(self.open_uv)
        self.button_bake.clicked.connect(self.bake)

        self.button_clone_node.clicked.connect(self.clone_node)

        self.button_cut.clicked.connect(lambda: self.poly_modeing_action(0))
        self.button_LoopEdge.clicked.connect(lambda: self.poly_modeing_action(1))
        self.button_MergePoint.clicked.connect(lambda: self.poly_modeing_action(2))
        self.button_Remove.clicked.connect(lambda: self.poly_modeing_action(3))
        self.button_TargetWeld.clicked.connect(lambda: self.poly_modeing_action(4))
        self.MakePlane_One.clicked.connect(lambda: self.poly_modeing_action(5))

        self.button_pivot_to_zero.clicked.connect(self.pivot_to_zero)

        self.button_plane.clicked.connect(lambda: self.creat_simple_poly(0))
        self.button_box.clicked.connect(lambda: self.creat_simple_poly(1))
        self.button_cyliner.clicked.connect(lambda: self.creat_simple_poly(2))
        self.button_sphere.clicked.connect(lambda: self.creat_simple_poly(3))

    '''
    set_coord
    设置当前坐标系空间
    '''
    def set_coord(self,value):

        if(value == 0):
            rt.toolMode.coordsys(rt.Name("local"))

        if(value == 1):
            rt.toolMode.coordsys(rt.Name("view"))

        if (value == 2):
            rt.toolMode.coordsys(rt.Name("world"))

        if (value == 3):
            rt.toolMode.coordsys(rt.Name("screen"))


    '''
    set_constrations
    设置约束方式
    '''
    def set_constrations(self,value):
        obj = rt.selection[0]
        if(value == 0 ):
            obj.constrainType = 0

        if (value == 1):
            obj.constrainType = 1

        if (value == 2):
            obj.constrainType = 2

        if (value == 3):
            obj.constrainType = 3


    '''
    collstack
    塌陷
    '''
    def collstack(self):
        rt.convertToPoly(rt.selection)
        return


    '''
    xform
    '''
    def xform(self):
        a = rt.selection
        for x in a:
            rt.ResetXForm(x)
            rt.convertToPoly(x)


    '''
    pivot_to_center
    坐标到物体中心
    '''
    def pivot_to_center(self):
        with pymxs.undo(True):
            rt.CenterPivot(rt.selection)

    '''
    obj_to_zero
    物体位置归零
    '''
    def obj_to_zero(self):
        with pymxs.undo(True):
            s = rt.selection
            for x in s:
                rt.setProperty(x, "pos.x", 0.0)
                rt.setProperty(x, "pos.y", 0.0)
                rt.setProperty(x, "pos.z", 0.0)
            rt.redrawViews()



    '''
    锁定物体的旋转缩放
    '''
    def lock_selection(self,value):
        if(value == 0):
            rt.setTransformLockFlags(rt.selection,rt.Name("all"))
        if(value == 1):
            rt.setTransformLockFlags(rt.selection, rt.Name("none"))



    '''
    打开项目目录
    '''
    def open_maxfile(self):
        maxfile_path = rt.maxFilePath
        os.startfile(maxfile_path)



    '''
    保存选择文件为max
    '''
    def save_selectfile(self):
        maxfile_name = rt.maxFileName
        maxfile_path = rt.maxFilePath
        print(maxfile_path + maxfile_name)
        select_maxfile = maxfile_name.replace('.max', '')  # replace方法来进行字符串的删除
        rt.saveNodes(rt.selection,maxfile_path + select_maxfile + "_select.max")
        os.startfile(maxfile_path)


    '''    
    保存一个备份
    '''
    def save_backupfile(self):
        maxfile_name = rt.maxFileName
        maxfile_path = rt.maxFilePath
        print(maxfile_path+maxfile_name)
        backup_maxfile = maxfile_name.replace('.max','') #replace方法来进行字符串的删除
        rt.saveMaxFile(maxfile_path + backup_maxfile + "_backup.max",useNewFile = False)#传入参数false来防止max保存



    '''
    导出模块： 路径选择
    '''
    def select_path(self):
        directory = os.path.dirname(self.lineedit_exportPath.text())
        if not os.path.exists(directory):
            directory = ''
        output_path = QtWidgets.QFileDialog.getExistingDirectory(dir=directory)
        output_path = output_path
        self.lineedit_exportPath.setText(output_path)

    def RotatePivotOnly(self, obj, rotation):
        rotValInv = rt.inverse(rt.r2q(rotation))
        with pymxs.animate(False):
            obj.rotation *= rotValInv
            obj.objectoffsetpos *= rotValInv
            obj.objectoffsetrot *= rotValInv


    '''
    导出模块：fbx设置
    '''
    def fbx_setting(self):
        rt.OpenFbxSetting()



    '''
    导出模块：场景导出
    '''
    def export_fbx_unity_envir(self):
        rt.execute("fn r2q r = (return r as quat)")
        old_path = self.lineedit_exportPath.text()
        new_path = old_path + '/'
        name = self.lineedit_exportName.text()

        obj = rt.selection
        rotation = rt.EulerAngles(90, 0, 0)
        if (len(rt.selection)):
            for x in obj:
                mulity_name = "SM_" + x.Name
                posx = rt.getProperty(x,"pos.x")
                posy = rt.getProperty(x,"pos.y")
                posz = rt.getProperty(x,"pos.z")
                rt.setProperty(x, "pos.x", 0.0)
                rt.setProperty(x, "pos.y", 0.0)
                rt.setProperty(x, "pos.z", 0.0)
                if(self.checkbox_yUp.isChecked()):
                    self.RotatePivotOnly(x, rotation)
                else:
                    pass
                rt.select(x)
                rt.exportFile(new_path + mulity_name, rt.name('noPrompt'), selectedOnly=True, using=rt.FBXEXP)
                rt.ResetXForm(x)
                rt.convertToPoly(x)
                rt.setProperty(x, "pos.x", posx)
                rt.setProperty(x, "pos.y", posy)
                rt.setProperty(x, "pos.z", posz)

        else:
            rt.messageBox("没有选择物体")

        rt.redrawViews()


    '''
    导出模块：角色模块
    '''
    def export_fbx_unity_character(self):
        old_path = self.lineedit_exportPath.text()
        new_path = old_path + '/'
        name = self.lineedit_exportName.text()

        obj = rt.selection
        rotation = rt.EulerAngles(90, 0, 0)
        rt.execute("fn r2q r = (return r as quat)")

        # 判断是否选择物体
        if(len(rt.selection)):
            if(name != ""):
                for x in obj:
                    # 坐标系是否归零
                    if(self.checkbox_pivot_0.isChecked()):
                        x.pivot = rt.Point3(0, 0, 0)

                    #  位置移动到【0，0，0】
                    if(self.checkbox_pos_0.isChecked()):
                        rt.setProperty(x, "pos.x", 0.0)
                        rt.setProperty(x, "pos.y", 0.0)
                        rt.setProperty(x, "pos.z", 0.0)

                    #  是否Y轴朝上
                    if (self.checkbox_yUp.isChecked()):
                        self.RotatePivotOnly(x, rotation)

                    else:
                        pass


                rt.exportFile(new_path + name, rt.name('noPrompt'), selectedOnly=True, using=rt.FBXEXP)

                # 导出后是否恢复原始轴
                if(self.checkbox_recorve_pivot.isChecked()):
                    for x in obj:
                        rt.ResetXForm(x)
                        rt.CenterPivot(x)
                        rt.convertToPoly(x)

            else:
                rt.messageBox("请输入导出的物体的名字")
        else:
            rt.messageBox("没有选择物体")



    def export_obj(self):
        objpath = self.path_line.text()
        obj_new_path = objpath + '/'
        obj_name = self.name_line.text()

        if(len(rt.selection)):
            rt.exportFile(obj_new_path + obj_name, rt.name('noPrompt'), selectedOnly=True, using=rt.ObjExp)
        else:
            rt.messageBox("没有选择物体")


    '''
    打开烘培
    '''
    def bake(self):

        rt.execute('actionMan.executeAction 1858480148 "23214332"')



    '''
    打开uv
    '''
    def open_uv(self):
        a = rt.selection
        uv = rt.Unwrap_UVW()
        for x in a:
            rt.addModifier(x, uv)

        rt.setCommandPanelTaskMode(rt.name('create'))
        rt.setCommandPanelTaskMode(rt.name('modify'))
        uv.edit()



    '''
    材质：统一一个材质
    '''

    def one_material(self):
        with pymxs.undo(True):
            a = rt.selection
            m = rt.ai_Standard_Surface()
            for x in a:
                x.material = m
            rt.redrawViews()  # 视图更新

    '''
    材质：复合材质
    '''
    def mulity_material(self):
        with pymxs.undo(True):
            a = rt.selection
            for x in a:
                m = rt.ai_Standard_Surface()
                m.name = "M_" + x.name
                m.base_color = rt.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
                m.specular = 0.0
                x.material = m
            rt.redrawViews()  # 视图更新
        return




    '''
    材质：清理材质
    '''
    def clear_material(self):
        with pymxs.undo(True):
            for obj in rt.selection:
                obj.material = rt.undefined
            rt.redrawViews()





    '''
    材质：颜色设为灰色
    '''
    def clear_materialColor(self):
        with pymxs.undo(True):
            for obj in rt.selection:
                obj.material.base_color = rt.color(150,150,150)
            rt.redrawViews()

    '''
    复制
    '''
    def clone_node(self):
        with pymxs.undo(True):
            rt.copy(rt.selection)

    '''
    模型操作命令集合
    '''
    def  poly_modeing_action(self,value):
        if(value == 0):
            rt.execute('macros.run "Ribbon - Modeling" "CutsCut"')
        if (value == 1):
            rt.execute('macros.run "PolyTools" "SwiftLoop"')
        if (value == 2):
            rt.execute('macros.run "Ribbon - Modeling" "GeometryCollapse"')
        if (value == 3):
            rt.execute('macros.run "Ribbon - Modeling" "VertexRemove"')
        if (value == 4):
            rt.execute('macros.run "Editable Polygon Object" "EPoly_TargetWeld"')
        if (value == 5):
            with pymxs.undo(True):
                rt.execute('$.EditablePoly.ConvertSelection #Face #Edge')
                rt.execute('$.EditablePoly.makeSmoothEdges 1')
                rt.execute('$.EditablePoly.ConvertSelectionToBorder #Face #Edge')
                rt.execute('$.EditablePoly.makeHardEdges 1')
                rt.execute('$.EditablePoly.makePlanar #Face')

    def  pivot_to_zero(self):
        for x in rt.selection:
            x.pivot = rt.Point3(0,0,0)


    '''
    maya模式快速创建基本体
    '''
    def  creat_simple_poly(self,value):
        if(value == 0 ):
            with pymxs.undo(True):
                a = rt.plane()
                a.lengthsegs = 1
                a.widthsegs = 1
                rt.redrawViews()

        if(value == 1):
            with pymxs.undo(True):
                a = rt.box()
                rt.redrawViews()

        if (value == 2):
            with pymxs.undo(True):
                a = rt.cylinder()
                a.sides = 12
                rt.redrawViews()

        if (value == 3):
            with pymxs.undo(True):
                a = rt.sphere()
                a.segs = 12
                rt.redrawViews()



if __name__ == '__main__':

    try:
        Fasttool_window.close()
        Fasttool_window.deleteLater()

    except:
        pass
    main_window2 = MaxPlus.GetQMaxMainWindow()
    Fasttool_window= TestDialog(parent=main_window2)
    Fasttool_window.setFloating(True)
    Fasttool_window.show()

