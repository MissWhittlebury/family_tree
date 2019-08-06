##TODO(dwojtak): actually validate responses instead of smoketest
import requests



def test_relations(endpoint, id, relation_type):
    params = {'type': relation_type}
    resp = requests.get(f'{endpoint}/{id}', params=params)
    assert resp.status_code == 200
    print(resp.json())


def test_all():
    endpoint = 'http://localhost:5000/person/relations'
    test_pairs = {
          'siblings': 6
        , 'parents': 7
        , 'children': 2
        , 'grandparents': 10
        , 'cousins': 9
    }
    for k, v in test_pairs.items():
        print(k.upper())
        test_relations(endpoint, v, k)

if __name__=='__main__':
    test_all()
