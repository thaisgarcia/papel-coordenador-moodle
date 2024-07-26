# Script de Inscrição e Atribuição de Papel do Usuário do Moodle

Este script Python automatiza a matrícula de usuários em cursos do Moodle e a atribuição de papéis, como coordenadores.

## Funcionalidades

1. **Obter Cursos por Categoria**: Recupera a lista de cursos que pertencem a uma categoria específica.
2. **Matricular Usuário em Curso**: Matrícula um usuário em um curso e atribui um papel específico a ele.
3. **Listar Usuários Matriculados**: Obtém a lista de usuários que estão matriculados em um curso.
4. **Buscar Informações do Usuário**: Recupera detalhes sobre um usuário específico.
5. **Verificar Papel de Coordenador**: Verifica se um usuário específico é coordenador em um curso.

## Pré-requisitos

- Python 3.x
- Biblioteca `requests` (instale com `pip install requests`)

## Configuração

1. **Token de Acesso**: Substitua `'your_token'` pelo seu token de autenticação da API do Moodle.
2. **URL do Moodle**: Substitua `'https://your-moodle-site.com/webservice/rest/server.php'` pela URL de seu servidor Moodle.
3. **Parâmetros**:
   - `user_id`: ID do usuário que você deseja matricular e atribuir o papel de coordenador.
   - `role_id`: ID do papel de coordenador.
   - `category_id`: ID da categoria de cursos onde o usuário deve ser matriculado.

## Uso

1. **Configure o Script**:
   - Atualize os valores de `token`, `moodle_url`, `user_id`, `role_id` e `category_id` no script.

2. **Execute o Script**:
   ```bash
   python moodle_coordinator_assignment.py
   ```
