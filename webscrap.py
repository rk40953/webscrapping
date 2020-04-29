


import requests
from bs4 import BeautifulSoup
from lxml import html
import json

url='https://parivahan.gov.in/rcdlstatus/?pur_cd=101'

response1=requests.get(url)

soup=BeautifulSoup(response.content,'html5lib')
y=soup.find('input',attrs={'name':'javax.faces.ViewState'})['value']

response=requests.post(url)
tree=html.fromstring(response.content)
infor1=tree.xpath('//table[@class="table table-responsive table-striped table-condensed table-bordered data-table"]/text()')

infor2=tree.xpath('//tr[@class="ui-widget-content ui-datatable-even"]/text()')
a=json.dumps(infor1)
b=json.dumps(infor2)

print(a)

print(b)
def get_captcha()
  pass
  

login_Data={'javax.faces.partial.ajax': 'true',
'javax.faces.source': 'form_rcdl:tf_dlNO',
'javax.faces.partial.execute': 'form_rcdl:tf_dlNO',
'javax.faces.partial.render': 'form_rcdl:tf_dlNO',
'javax.faces.behavior.event': 'valueChange',
'javax.faces.partial.event': 'change',
'form_rcdl': 'form_rcdl',
'form_rcdl:tf_dlNO': 'DL-0420110149646',
'form_rcdl:tf_dob_input':'09/02/1976',
'form_rcdl:j_idt34:CaptchaID':'rxhh5',
'javax.faces.ViewState': 'y'}
