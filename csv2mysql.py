#! /usr/bin/python
# -*- coding: utf-8 -*-
import csv
import MySQLdb


if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(host='121.42.188.55', user='root', passwd='tianchi',
                               db='AliyunMusic', port=3306, charset="utf8")
        print "Remote MySQL Database Connected, Supported By Aliyun ECS!"
        cur = conn.cursor()
        conn.select_db('AliyunMusic')
        swap_list = []
        with open('mars_tianchi_user_actions.csv', 'r') as fp:
            for line in csv.reader(fp, delimiter=',', quoting=csv.QUOTE_NONE):
                swap_list.append((line[0], line[1], line[2],
                                  line[3], line[4]))
        sql = "INSERT INTO mars_tianchi_user_actions(user_id, song_id, gmt_create, " \
              "action_type, ds) VALUES(%s, %s, %s, %s, %s);"
        cur.executemany(sql, swap_list)
        conn.commit()
        print "DataSet Has Been Inserted Into Database successfully!"
        cur.close()
        conn.close()
        print "Remote MySQL Database Closed!"
    except MySQLdb.OperationalError, e:
        print e[1]
