import requests

# Configurações do Moodle (substituir)
token = 'your_token'
moodle_url = 'https://your-moodle-site.com/webservice/rest/server.php'

# Parâmetros (substituir)
user_id = 4  # ID do Coordenador
role_id = 9  # ID do Papel de Coordenador
category_id = 2  # ID da Categoria

# Funções da API REST
function_get_courses_by_field = 'core_course_get_courses_by_field'
function_enrol_user = 'enrol_manual_enrol_users'
function_get_enrolled_users = 'core_enrol_get_enrolled_users'
function_get_users = 'core_user_get_users'

# Obtém a lista de cursos pertencentes a uma categoria específica
def get_courses_by_category(category_id):
    data = {
        'wstoken': token,
        'wsfunction': function_get_courses_by_field,
        'moodlewsrestformat': 'json',
        'field': 'category',
        'value': category_id
    }
    response = requests.post(moodle_url, data=data)
    if response.status_code == 200:
        response_data = response.json()
        if 'exception' in response_data:
            print(f"Erro na resposta: {response_data['message']}")
            return None
        return response_data.get('courses', [])
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

# Matricula um usuário em um curso e atribui um papel a ele
def enrol_user(course_id, user_id, role_id):
    data = {
        'wstoken': token,
        'wsfunction': function_enrol_user,
        'moodlewsrestformat': 'json',
        'enrolments[0][roleid]': role_id,
        'enrolments[0][userid]': user_id,
        'enrolments[0][courseid]': course_id
    }
    response = requests.post(moodle_url, data=data)
    if response.status_code == 403:
        print("Acesso proibido. Verifique o token e permissões.")
    response_data = response.json()
    if response_data and 'exception' in response_data:
        print(f"Erro na resposta: {response_data['message']}")
    return response_data

# Retorna a lista de usuários matriculados
def get_enrolled_users(course_id):
    data = {
        'wstoken': token,
        'wsfunction': function_get_enrolled_users,
        'moodlewsrestformat': 'json',
        'courseid': course_id
    }
    response = requests.post(moodle_url, data=data)
    if response.status_code == 200:
        response_data = response.json()
        if 'exception' in response_data:
            print(f"Erro na resposta: {response_data['message']}")
            return None
        return response_data
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

def get_user(user_id):
    data = {
        'wstoken': token,
        'wsfunction': function_get_users,
        'moodlewsrestformat': 'json',
        'criteria[0][key]': 'id',
        'criteria[0][value]': user_id
    }
    response = requests.post(moodle_url, data=data)
    if response.status_code == 200:
        response_data = response.json()
        if 'exception' in response_data:
            print(f"Erro na resposta: {response_data['message']}")
            return None
        return response_data.get('users', [])
    else:
        print(f"Erro na requisição: {response.status_code}")
        return None

# Verifica se o usuário está matriculado e se possui o papel de coordenador
def user_is_coordinator(user_id, course_id):
    enrolled_users = get_enrolled_users(course_id)
    if enrolled_users:
        for user in enrolled_users:
            if user['id'] == user_id:
                return any(role['roleid'] == role_id for role in user.get('roles', []))
    return False

courses = get_courses_by_category(category_id)

if courses:
    if isinstance(courses, list):
        for course in courses:
            course_id = course.get('id')
            context_id = course_id + 1  # Calculando context_id 

            if user_is_coordinator(user_id, course_id):
                print(f"\nUsuário {user_id} já é coordenador no curso {course_id}.")
            else:
                enrolled_users = get_enrolled_users(course_id)

                if enrolled_users:
                    user_ids = [user['id'] for user in enrolled_users]

                    if user_id in user_ids:
                        print(f"\nUsuário {user_id} é professor ou outro papel no curso {course_id}.")
                    
                    else:
                        print(f"\nUsuário {user_id} não está matriculado no curso {course_id}. Adicionando como coordenador.")
                        enrol_result = enrol_user(course_id, user_id, role_id)
                        if enrol_result is None or 'exception' in enrol_result:
                            print(f"Erro ao matricular usuário no curso {course_id}: {enrol_result}")
    else:
        print("A resposta não é uma lista de cursos.")
else:
    print("Nenhum curso encontrado ou erro na requisição.")