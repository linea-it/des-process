import unittest
import snapshottest
import requests
from des_process import process

class TestProcesses(snapshottest.TestCase):

  def setUp(self):
    self.url = "http://scienceportal-dev.linea.gov.br/api/graphql"

  def test_all(self):
    query = """{
      processesList(first: 5) {
        edges {
          node {
            processId
            startTime
            endTime
            name
            productLog
            processDir
            size
            processStatus {
              displayName
            }
          }
        }
      }
    }"""


    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])

  def test_by_id(self):
    query = """{
      processByProcessId(processId: 10007628) {
        processId
        startTime
        endTime
        name
        productLog
        processDir
        size
        processStatus {
          displayName
        }
      }
    }"""

    response = requests.post(self.url, json={ 'query': query })
    self.assertMatchSnapshot(response.json()['data'])

    self.assertEqual(process.by_id(10007628), {'processId': 10007628, 'startTime': '2012-01-11T01:08:06', 'endTime': '2012-01-11T06:06:42', 'name': 'Cluster Finder', 'productLog': 'http://testing.linea.gov.br/VP/getViewProcessCon?process_id=10007628', 'processDir': '/24/34/000010007628', 'size': None, 'processStatus': {'displayName': 'Failure'}})