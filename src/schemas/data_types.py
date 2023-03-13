api_data_types = {
    'hired_employees': {
        'id': int,
        'name': str,
        'datetime': str,
        'department_id': int,
        'job_id': int
    },
    'departments': {
        'id': int,
        'department': str
    },
    'jobs': {
        'id': int,
        'job': str
    }
}

batch_data_types = {
    'hired_employees.csv': {
        'id': int,
        'name': str,
        'datetime': str,
        'department_id': int,
        'job_id': int
    },
    'departments.csv': {
        'id': int,
        'department': str
    },
    'jobs.csv': {
        'id': int,
        'job': str
    }
}