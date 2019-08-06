from datetime import datetime

from flask import Blueprint, jsonify, request, current_app

from app.db_manager.models import Person, Parents
from app import db
from app.helpers.date_conversion import str_to_date

bp = Blueprint('person', __name__, url_prefix='/person')


@bp.route('/crud', methods=['POST'])
def crud():
    """Assumes a lot.
    - Either both or neither parent is provided
    - That an individual is unique across first name, last name, birthdate
    """
    ##TODO(expand crud)
    if request.method == 'POST':
        ##TODO(dwojtak): validate json
        payload = request.get_json()
        people = {}
        for person_dict in payload:
            info = person_dict['info']
            info['birthDate'] = str_to_date(info['birthDate'])
            ## person check
            if Person.person_exists(info['firstName'], info['lastName'],
                                    info['birthDate']):
                person = Person.get_person(info['firstName'], info['lastName'],
                                           info['birthDate'])
            else:
                person = Person(first_name=info['firstName'],
                                last_name=info['lastName'],
                                phone_number=info.get('phoneNumber'),
                                email_address=info.get('emailAddress'),
                                address_id=info.get('addressId'),
                                birth_date=info['birthDate'])
                db.session.add(person)
            people[person_dict['who']] = person

        ## parents check
        if people.get('mother') and people.get('father'):
            mother = people['mother']
            father = people['father']
            if Parents.parents_exist(mother.id, father.id):
                parents = Parents.get_parents(mother.id, father.id)
            else:
                parents = Parents(mother_person_id=mother.id,
                                  father_person_id=father.id)
                db.session.add(parents)
            people['child'].parents_id = parents.id
        
        db.session.commit()
        return jsonify({'message': 'success'}), 200


@bp.route('/id', methods=['GET'])
def person_id():
    if Person.person_exists(first_name=request.args['first_name'],
                            last_name=request.args['last_name'],
                            birth_date=request.args['birth_date']):
        return Person.get_person(first_name=request.args['first_name'],
                                 last_name=request.args['last_name'],
                                 birth_date=request.args['birth_date'])
    return jsonify({'message': 'the requested person does not exist'}), 404


@bp.route('/relations/<person_id>')
def relations(person_id):
    """Assumes user knows the database id of the individual
    """
    person = Person.get_person(person_id=person_id)
    relation_type = request.args['type']
    if relation_type == 'parents':
        people = person.parents
    elif relation_type == 'siblings':
        people = person.siblings
    elif relation_type == 'children':
        people = person.children
    elif relation_type == 'grandparents':
        people = person.grandparents
    elif relation_type == 'cousins':
        people = person.cousins
    else:
        return jsonify({'message': 'not a valid relation type'}), 400
    
    people = list(map(lambda x: x.to_dict(), people))
    return jsonify(people), 200
