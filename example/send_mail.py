#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@author: diange.du
@file: send_mail.py
@time: 2020/9/2 18:17
@desc: 发送附件邮件
'''


import datetime
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import xlsxwriter
import smtplib
from example.log_util import log


class SenMailDemo:

    def __init__(self):
        self.pre_dte = datetime.datetime.now() + datetime.timedelta(days=-1)
        self.mail_user = "邮箱地址"  # 用户名
        self.server = smtplib.SMTP_SSL("server-url", 465)
        self.server.login("login-name", "pwd")
        report_dte_str = self.pre_dte.strftime('%m%d')
        self.file_name = f'Report-{report_dte_str}.xlsx'
        self.workbook = xlsxwriter.Workbook(self.file_name)

        self.style = self.workbook.add_format({
            'bold': True,  # 字体加粗
            'border': 1,  # 单元格边框宽度
            'align': 'left',  # 水平对齐方式
            'valign': 'vcenter',  # 垂直对齐方式
            'fg_color': '#F4B084',  # 单元格背景颜色
            'text_wrap': True,  # 是否自动换行
        })

        self.mailto_list = ['a@163.com', 'b@126.com']
        pass

    def main(self):
        """
        生成excel并填充数据
        :return:
        """
        # 取数据sql
        data_sql = """SELECT
                        filed1 as 标题1,
                        filed2 as 标题2,
                        filed3 as 标题3,
                        filed4 as 标题4  
                    FROM
                        t_demo;"""
        self.get_set_data(data_sql, (), 'sheet11')
        """
        ......
        """

        self.workbook.close()
        msg = MIMEMultipart()
        report_dte_str_zn = self.pre_dte.strftime('%m{m}%d{d}').format(m='月', d='日')
        msg['Subject'] = f"日报-{report_dte_str_zn}"
        msg['From'] = self.mail_user
        msg['To'] = ','.join()

        part = MIMEText("见附件")
        msg.attach(part)

        part = MIMEApplication(open(self.file_name, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=self.file_name)
        msg.attach(part)
        self.server.sendmail(self.mail_user, self.mailto_list, msg.as_string())

        self.server.close()
        log.info(f"日报-{report_dte_str_zn} 发送成功")

    def get_set_data(self, sql, params, sheet_name, add_nummber=False):
        # data = self.db.get_all_dic(sql, params)  # 替换db查询
        row = 0
        if data:
            sheet = self.workbook.add_worksheet(sheet_name)
            for item in data:
                col = 0
                # 设置标题
                if row == 0:
                    if add_nummber:
                        sheet.write(row, col, '排名', self.style)
                        col += 1
                    for ii in item:
                        sheet.write(row, col, ii, self.style)
                        col += 1
                    row += 1

                col = 0
                if add_nummber:
                    sheet.write(row, col, row)
                    col += 1

                for key in item:
                    # 特殊处理
                    if key == '总直播时长' or key == '观看时长' or key == '观看时长':
                        sheet.write(row, col, str(item[key]) + 'h' if item[key] is not None else '')
                    else:
                        sheet.write(row, col, str(item[key] if item[key] is not None else ''))
                    col += 1
                row += 1


if __name__ == '__main__':
    SenMailDemo().main()