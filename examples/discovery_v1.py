
# coding: utf-8

# In[1]:

import sys,pprint
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud


# In[2]:

DISCOVERY_USERNAME='CHANGE_ME'
DISCOVERY_PASSWORD='CHANGE_ME'
pp = pprint.PrettyPrinter(indent=4)


# In[10]:

discovery = watson_developer_cloud.DiscoveryV1(
    '2016-11-07',
    username=DISCOVERY_USERNAME,
    password=DISCOVERY_PASSWORD)

environments = discovery.get_environments()
pp.pprint(environments)

news_environments = [x for x in environments['environments'] if
                     x['name'] == 'Watson News Environment']
news_environment_id = news_environments[0]['environment_id']
pp.pprint(news_environment_id)

collections = discovery.list_collections(news_environment_id)
news_collections = [x for x in collections['collections']]
pp.pprint(collections)


# In[11]:

pp.pprint(discovery.list_configurations(environment_id=news_environment_id))
default_config_id = discovery.get_default_configuration_id(environment_id=news_environment_id)
pp.pprint(default_config_id)


# In[12]:

default_config = discovery.get_configuration(environment_id=news_environment_id, configuration_id=default_config_id)
pp.pprint(default_config)


# In[13]:

new_environment = discovery.create_environment(name="new env", description="bogus env")


# In[18]:

pp.pprint(new_environment)

if (discovery.get_environment(environment_id=new_environment['environment_id'])['status'] == 'active'):
    writable_environment_id = new_environment['environment_id']
    new_collection = discovery.create_collection(environment_id=writable_environment_id,
                                                name='Example Collection',
                                                description="just a test")
    
    pp.pprint(new_collection)
    #pp.pprint(discovery.get_collections(environment_id=writable_environment_id))
    #res = discovery.delete_collection(environment_id='10b733d0-1232-4924-a670-e6ffaed2e641',
    #                                  collection_id=new_collection['collection_id'])
#    pp.pprint(res)


# In[23]:

collections = discovery.list_collections(environment_id=writable_environment_id)
pp.pprint(collections)


# In[21]:

with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:
    pp.pprint(discovery.test_document(environment_id=writable_environment_id, fileinfo=fileinfo))


# In[25]:

with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:
    res = discovery.add_document(environment_id=writable_environment_id,
                                 collection_id=collections['collections'][0]['collection_id'],
                                 fileinfo=fileinfo)
    pp.pprint(res)


# In[29]:

res = discovery.get_collection(environment_id=writable_environment_id,
                               collection_id=collections['collections'][0]['collection_id'])
pp.pprint(res['document_counts'])


# In[30]:

res = discovery.delete_environment(environment_id=writable_environment_id)
pp.pprint(res)


# In[ ]:



