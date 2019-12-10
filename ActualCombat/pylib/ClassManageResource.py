# -*- coding: utf-8 -*-
# from ActualCombat.cfg import vcode,URL
from cfg import vcode,URL
from pprint import pprint
import requests


class ClassManageResource:
    def list_classes_by_schoolgrade(self,gradeid=None):
        '''
        根据年级id列出班级，若年级id未传入，则列出所有
        :param gradeid:年级id
        :return: 返回dict形式的数据
        '''
        if gradeid:
            params={"vcode":vcode,
                    "action":"list_classes_by_schoolgrade",
                    "gradeid":gradeid
                    }
        else:
            params = {"vcode": vcode,
                      "action": "list_classes_by_schoolgrade"
                      }
        respDict=requests.get(URL,params=params).json()
        pprint(respDict)
        return respDict

    def add_class(self,gradeid,name,studentlimit):
        '''
        添加班级
        :param gradeid:年级id
        :param name: 班级名次
        :param studentlimit: 班级人数限制
        :return: 返回dict形式的数据
        '''
        payload={
            "vcode":vcode,
            "action":"add",
            "grade":gradeid,
            "name":name,
            "studentlimit":studentlimit
        }
        respDict=requests.post(URL,data=payload).json()
        pprint(respDict)
        return respDict

    def modify_class_by_classid(self,classid,name,studentlimit):
        '''
        根据班级id，修改班级
        :param classid:班级id
        :param name: 班级名次
        :param studentlimit: 班级人数限制
        :return: 返回dict形式的数据
        '''
        payload={
            "vcode":vcode,
            "action":"modify",
            "name":name,
            "studentlimit":studentlimit
        }
        respDict=requests.put(f'{URL}/{classid}',data=payload).json()
        pprint(respDict)
        return respDict

    def delete_class_by_classid(self,classid):
        '''
        根据班级id，删除班级
        :param classid:班级id
        :return: 返回dict形式的数据
        '''
        payload={
            "vcode":vcode
        }
        respDict=requests.delete(f'{URL}/{classid}',data=payload).json()
        pprint(respDict)
        return respDict

    def deleteAllClasses(self):
        '''
        删除所有班级
        '''
        classes=self.list_classes_by_schoolgrade()['retlist']
        for one in classes:
            resp=self.delete_class_by_classid(one['id'])
            assert resp['retcode']==0


if __name__ == '__main__':
    obj=ClassManageResource()
    # obj.add_class(1,'newclass1',80)
    # obj.deleteAllClasses()
    obj.delete_class_by_classid(276346)
    obj.list_classes_by_schoolgrade()