#! /usr/bin/python
# -*- coding: utf-8 -*-
import csv
import MySQLdb
import sys


if __name__ == '__main__':
    try:
        conn = MySQLdb.connect(host='121.42.188.55', user='root', passwd='tianchi',
                               db='AliyunMusic', port=3306, charset="utf8")
        print "Remote MySQL Database Connected, Supported By Aliyun ECS!"
        cur = conn.cursor()
        conn.select_db('AliyunMusic')
        swap_list = []
        with open('mars_tianchi_songs.csv', 'r') as fp:
            for line in fp.readlines():
                split_items = line.split(',')
                swap_list.append((split_items[0], split_items[1],
                                  split_items[2], split_items[3],
                                  split_items[4], split_items[5]))
                sql = "INSERT INTO mars_tianchi_songs(song_id, artist_id, publish_time, " \
                      "song_init_plays, language_type, gender) VALUES(%s, %s, %s, %s, %s, %s);"
                cur.executemany(sql, swap_list)
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.OperationalError, e:
        print e[1]
