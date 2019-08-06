from app import db



class Person(db.Model):
    id            = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name    = db.Column(db.String(100), nullable=False)
    last_name     = db.Column(db.String(100), nullable=False)
    phone_number  = db.Column(db.String(20))
    email_address = db.Column(db.String(255))
    ##TODO(dwojtak): implement address table
    address_id    = db.Column(db.Integer)
    birth_date    = db.Column(db.Date, nullable=False)
    parents_id    = db.Column(db.Integer, db.ForeignKey('parents.id'),
                              nullable=True)
    db.UniqueConstraint('first_name', 'last_name', 'birth_date')    

    @property
    def parents(self):
        if self.parents_id is None:
            return []
        parents = Parents.query.get(self.parents_id)
        mother = Person.query.get(parents.mother_person_id)
        father = Person.query.get(parents.father_person_id)
        return [mother, father]

    @property
    def siblings(self):
        siblings = []
        if self.parents_id is None:
            return siblings
        siblings_rows = db.session.execute(
            'SELECT id FROM person WHERE parents_id = :pa_id',
            {'pa_id': self.parents_id})
        for s in siblings_rows:
            sibling = Person.query.get(s['id'])
            siblings.append(sibling)
        return siblings

    @property
    def children(self):
        parents_rows = db.session.execute(
            'SELECT id FROM parents ' \
            'WHERE mother_person_id = :pe_id OR father_person_id = :pe_id',
            {'pe_id': self.id})
        parents_ids = [p['id'] for p in parents_rows]
        children = db.session.query(Person).filter(Person.parents_id.in_(parents_ids))
        return children


    @property
    def grandparents(self):
        grandparents = []
        if self.parents:
            for parent in self.parents:
                grandparents += parent.parents
        return grandparents

    @property
    def cousins(self):
        cousins = []
        aunts_uncles = []
        ## parents siblings' children
        if self.parents:
            for parent in self.parents:
                aunts_uncles += parent.siblings
            for aunt_uncle in aunts_uncles:
                cousins += aunt_uncle.children
        return cousins

    def to_dict(self):
        return {
              'id': self.id
            , 'firstName': self.first_name
            , 'lastName': self.last_name
            , 'birthDate': self.birth_date
            , 'parentsId': self.parents_id
        }

    @staticmethod
    def person_exists(first_name, last_name, birth_date):
        person = db.session.query(Person).filter_by(first_name=first_name,
                                                    last_name=last_name,
                                                    birth_date=birth_date).first()
        if person:
            return True
        return False

    @staticmethod
    def get_person(first_name=None, last_name=None, birth_date=None,
                   person_id=None):
        if person_id:
            return Person.query.get(person_id)
        return db.session.query(Person).filter_by(first_name=first_name,
                                                  last_name=last_name,
                                                  birth_date=birth_date).first()


    def __repr__(self):
        return f'<Person {self.id}>'


class Parents(db.Model):
    id               = db.Column(db.Integer, primary_key=True,
                                 autoincrement=True)
    mother_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    father_person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    db.UniqueConstraint('mother_person_id', 'father_person_id')

    @staticmethod
    def parents_exist(mother_id, father_id):
        parents = db.session.query(Parents).filter_by(
            mother_person_id=mother_id, father_person_id=father_id).first()
        if parents:
            return True
        return False

    @staticmethod
    def get_parents(mother_id, father_id):
        return db.session.query(Parents).filter_by(
            mother_person_id=mother_id, father_person_id=father_id).first()
        

    def __repr__(self):
        return f'<Parents {self.id}>'

