import requests
import uuid

ENDPOINT = 'https://todo.pixegami.io'

# response = requests.get(ENDPOINT)
# data = response.json()
# print(data)

def test_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_create_task():
    payload = new_task_payload()
    # response = requests.post(ENDPOINT + '/create-task', json=payload)
    response = create_task(payload)
    data = response.json()
    print(data)

    task_id = data['task']['task_id']
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data['content'] == payload['content']
    assert get_task_data['user_id'] == payload['user_id']

def test_update_task():
    # pass
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']

    new_payload = {
        'content': 'my updated content',
        "user_id": payload['user_id'],
        "task_id": task_id,
        'is_done': True,
    }

    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200

    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']

def test_list_users():
    n = 4 
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200

    user_id = payload['user_id']
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    tasks = data['tasks']
    assert len(tasks) == n 
    print(data)

def test_delete_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']

    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200 

    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404 

def update_task(payload):  
    return requests.put(ENDPOINT + '/update-task', json=payload)


def create_task(payload):
    return requests.put(ENDPOINT +'/create-task', json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f'/get-task/{task_id}')

def list_tasks(user_id):
    return requests.get(ENDPOINT + f"/list-tasks/{user_id}")

def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")

def new_task_payload():
    user_id = f"test_user_{uuid.uuid4().hex}" 
    content = f"test_content_{uuid.uuid4().hex}"
    
    print(f"Creating task for user {user_id} with content {content}")

    return {
        'content': content,
        'user_id': user_id,
        # 'task_id': 'test_task_id',
        'is_done': False
    }

