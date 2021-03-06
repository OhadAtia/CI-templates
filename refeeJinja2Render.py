'''
Created on May 28, 2015

This is a small jinja2 template render engine.
made mostly to learn how to build j2 templates and test them before uploading to rafee

Instructions:
htmlslide is the name of the new template (.html or j2, doesn't matter)
json url - the engine gets a Json and treats it as a dict (python style), so it can populate the vars in the template itself.
data_source - a variable name "data source" exists in the template. it represents the dict. to access it's info, just add 'data source.key' 
to get the value of a specified key in your template file.
@author: tzure
'''
import jinja2
import json
from urllib import urlopen

#rendered slides folder
htmlslide = "output.html"

env = jinja2.Environment(loader=jinja2.FileSystemLoader(''))
template = env.get_template('template.j2')


# This is the Data source address.
# just add the address that returns a JSON we can use. Current JSON takes all jobs from jenkins
json_url = urlopen("http://hsg-ci.xiv.ibm.com/view/CI/view/StatusByProject/api/json?pretty=true")
data_source=json.load(json_url)

# just checking
# print data_source['jobs']


# Finally, process the template to produce our final text.
html = template.render(data_source = data_source)
o = open(htmlslide, 'w')
o.write(html)
o.close()


if __name__ == '__main__':
    pass