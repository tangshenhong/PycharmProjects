# -*- coding: utf-8 -*-
import pymssql


class DataBaseOperation:
    '''数据库工具类'''
    def __init__(self,server,user,password,database):
        self.server=server
        self.user=user
        self.password=password
        self.database=database

    def get_connection(self):
        '''
        获得数据库连接
        :return:返回数据库cursor
        '''
        self.conn=pymssql.connect(self.server,self.user,self.password,self.database)
        self.conn.autocommit(True)
        cursor=self.conn.cursor()
        if not cursor:
            raise (NameError,'连接数据库失败')
        else:
            return cursor

    def execute_sql(self,sql,valueList=None,isDele=False):
        '''
        插入、删除或者查询数据
        :param sql: 要执行的sql语句
        :param valueList:插入的数据列表
        :param isDele:是否要执行数据删除操作
        :return:返回查询结果
        '''
        cursor = self.get_connection()
        if valueList:#插入数据
            cursor.executemany(sql, valueList)
        elif isDele==True:#删除数据
            cursor.execute(sql)
        else:#查询数据
            cursor.execute(sql)
            results = cursor.fetchall()
            self.conn.close()
            return results
        self.conn.close()