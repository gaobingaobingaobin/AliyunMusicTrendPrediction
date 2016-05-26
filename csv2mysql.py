#! /usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb


if __name__ == '__main__':
    MySQLdb.connect(host='121.42.188.55', user='root', passwd='tianchi',
                    db='WeiBo', port=3306, charset="utf8")
