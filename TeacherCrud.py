class TeacherCrud:
    def __init__(self, database):
        self.db = database

    def create_teacher(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def get_teacher(self):
        query = "MATCH (p:Teacher ) RETURN p.name AS name, p.ano_nasc AS ano_nasc, p.cpf AS cpf"
        results = self.db.execute_query(query)
        return [(result["name"], result["ano_nasc"], result["cpf"]) for result in results]


    def update_teacherName(self, old_name, new_name):
        query = "MATCH (p:Teacher {name: $old_name}) SET p.name = $new_name"
        parameters = {"old_name": old_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def update_teacherAno_nasc(self, old_ano_nasc, new_ano_nasc):
        query = "MATCH (p:Teacher  {ano_nasc: $old_ano_nasc}) SET p.ano_nasc = $new_ano_nasc"
        parameters = {"old_ano_nasc": old_ano_nasc, "new_ano_nasc": new_ano_nasc}
        self.db.execute_query(query, parameters)

    def update_teacherCpf(self, old_cpf, new_cpf):
        query = "MATCH (p:Teacher  {cpf: $old_cpf}) SET p.cpf = $new_cpf"
        parameters = {"old_cpf": old_cpf, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)

    def delete_teacher(self, name):
        query = "MATCH (p:Teacher  {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

