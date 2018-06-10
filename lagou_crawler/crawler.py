# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')
code_type = sys.getfilesystemencoding()
# print code_type

def write_line_add_enter(fp,line):
    fp.write(line)
    fp.write('\n')

def crawl_detail(fp,url):
    headers = {
        "Cookie": '_ga=GA1.2.533694627.1528471668; _gid=GA1.2.1271869461.1528471668; user_trace_token=20180608232438-0eb9f43f-6b30-11e8-9431-5254005c3644; LGUID=20180608232438-0eb9fa25-6b30-11e8-9431-5254005c3644; ab_test_random_num=0; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20180610185406-163e954eabee-0dc86cf8599037-52693478-1024000-163e954eabf72d; JSESSIONID=ABAAABAAAGGABCBE028258DB4468CDBFD1E5448089681F1; TG-TRACK-CODE=index_navigation; X_HTTP_TOKEN=fca1c3dcf077377bb707def81e887335; LGSID=20180610223123-f379bef2-6cba-11e8-9978-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0x8726ae740002cded%26issp%3D1%26f%3D3%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D1%26rsv_sug1%3D1%26rsv_sug7%3D001%26rsv_sug2%3D1%26rsp%3D5%26rsv_sug9%3Des_2_1%26rsv_sug4%3D4966%26rsv_sug%3D9; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528550561,1528628047,1528628058,1528641276; _putrc=4CD7F8C02C245D16123F89F2B170EADC; login=true; hasDeliver=0; unick=test; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=8870a5eeed6bbf2bb3eef40ea30c6cdabffd9c8edfbd41587aeca80770a9ffcf; mds_login_authToken="RBecBkqrRrPd9qoihXO0E4XlrBhlSxTVzAeTmG2D3twQbg+lYbjY2UnPnHfe1HRFfdamQWhUHq6OSd2VufqlLsxby+6k09M9FW9zT5SCUCXBcc3M6UlLi9TEfJayXqM0d139cSC6vNksFsibQ29gs3HzHjCujnVhcch9/2tKoZ54rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163ea225d7c6b-0cd0d41be1f1c-52693478-1024000-163ea225d7e267%22%2C%22%24device_id%22%3A%22163ea225d7c6b-0cd0d41be1f1c-52693478-1024000-163ea225d7e267%22%7D; sajssdk_2015_cross_new_user=1; _gat=1; SEARCH_ID=5aff59f0874144b08f999acfe25d47a7; LGRID=20180610225414-243de3b5-6cbe-11e8-997a-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528642649',
        "Host": "www.lagou.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content,"html.parser")
    need_tag_list = ['job-advantage', 'job_bt', 'job-address clearfix']
    # job_bt = soup.find("dl", attrs={'class':'job_detail'})
    # with open('conpany_info.txt', 'a') as fp:
    for class_name in need_tag_list:
        job_bt = soup.find("dd", attrs={'class': class_name})
        fp.write(job_bt.text.decode('utf-8').encode(code_type))
def main():
    # 请求头部，可直接复制Request Header中对应参数，Cookie隔一段时间可能会变
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie": '_ga=GA1.2.533694627.1528471668; _gid=GA1.2.1271869461.1528471668; user_trace_token=20180608232438-0eb9f43f-6b30-11e8-9431-5254005c3644; LGUID=20180608232438-0eb9fa25-6b30-11e8-9431-5254005c3644; ab_test_random_num=0; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20180610185406-163e954eabee-0dc86cf8599037-52693478-1024000-163e954eabf72d; JSESSIONID=ABAAABAAAGGABCBE028258DB4468CDBFD1E5448089681F1; TG-TRACK-CODE=index_navigation; X_HTTP_TOKEN=fca1c3dcf077377bb707def81e887335; LGSID=20180610223123-f379bef2-6cba-11e8-9978-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26rsv_spt%3D1%26rsv_iqid%3D0x8726ae740002cded%26issp%3D1%26f%3D3%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D1%26rsv_sug1%3D1%26rsv_sug7%3D001%26rsv_sug2%3D1%26rsp%3D5%26rsv_sug9%3Des_2_1%26rsv_sug4%3D4966%26rsv_sug%3D9; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528550561,1528628047,1528628058,1528641276; _putrc=4CD7F8C02C245D16123F89F2B170EADC; login=true; hasDeliver=0; unick=test; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=8870a5eeed6bbf2bb3eef40ea30c6cdabffd9c8edfbd41587aeca80770a9ffcf; mds_login_authToken="RBecBkqrRrPd9qoihXO0E4XlrBhlSxTVzAeTmG2D3twQbg+lYbjY2UnPnHfe1HRFfdamQWhUHq6OSd2VufqlLsxby+6k09M9FW9zT5SCUCXBcc3M6UlLi9TEfJayXqM0d139cSC6vNksFsibQ29gs3HzHjCujnVhcch9/2tKoZ54rucJXOpldXhUiavxhcCELWDotJ+bmNVwmAvQCptcy5e7czUcjiQC32Lco44BMYXrQ+AIOfEccJKHpj0vJ+ngq/27aqj1hWq8tEPFFjdnxMSfKgAnjbIEAX3F9CIW8BSiMHYmPBt7FDDY0CCVFICHr2dp5gQVGvhfbqg7VzvNsw=="; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22163ea225d7c6b-0cd0d41be1f1c-52693478-1024000-163ea225d7e267%22%2C%22%24device_id%22%3A%22163ea225d7c6b-0cd0d41be1f1c-52693478-1024000-163ea225d7e267%22%7D; sajssdk_2015_cross_new_user=1; _gat=1; LGRID=20180610224725-30823725-6cbd-11e8-9446-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1528642237; SEARCH_ID=365393e0ad5048518886c92dd6fa7eca',
        "Host": "www.lagou.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    }
    with open('conpany_info.txt', 'w') as fp:
        # 请求频繁时，网站可能会不响应，或者报错（请求频繁），这时每次请求完后，等待几秒
        for page in range(1, 31):
            url = "https://www.lagou.com/zhaopin/Python/%s/?filterOption=3" % page
            # General中查看对应的Request Method,如果是Post方法,需要获取对应的post表单数据
            result = requests.get(url, headers=headers)          
            soup = BeautifulSoup(result.content,"html.parser")
            # 根据class名称过滤
            company_infos = soup.find_all("li", attrs={'class':"con_list_item default_list"})
            for company_info in company_infos:
                write_line_add_enter(fp, "公司名称：".decode('utf-8').encode(code_type) + company_info.get('data-company').decode('utf-8').encode(code_type))
                write_line_add_enter(fp, "薪资待遇：".decode('utf-8').encode(code_type)+ company_info.get('data-salary').decode('utf-8').encode(code_type))
                job_url = 'https://www.lagou.com/jobs/%s.html' % company_info.get('data-positionid')
                crawl_detail(fp, job_url)
                write_line_add_enter(fp, '-'*160)
                write_line_add_enter(fp, '-'*160)



if __name__ == '__main__':
    main()