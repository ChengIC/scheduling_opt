def parse_rcmpsp_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    line_index = 0

    # Read portfolio information
    num_projects = int(lines[line_index].strip())
    line_index += 1
    num_resources = int(lines[line_index].strip())
    line_index += 1
    resource_availability = list(map(int, lines[line_index].split()))
    line_index += 1

    projects = []
    for _ in range(num_projects):
        # Skip empty lines
        while not lines[line_index].strip():
            line_index += 1

        # Read project information
        num_activities, release_date = map(int, lines[line_index].split())
        line_index += 1

        resource_usage = list(map(int, lines[line_index].split()))
        line_index += 1

        activities = []
        for _ in range(num_activities):
            # Skip empty lines
            while not lines[line_index].strip():
                line_index += 1

            activity_data = lines[line_index].split()
            duration = int(activity_data[0])
            resource_requirements = list(map(int, activity_data[1:1+num_resources]))
            num_successors = int(activity_data[1+num_resources])
            successors = activity_data[2+num_resources:]
            line_index += 1

            activities.append({
                'duration': duration,
                'resource_requirements': resource_requirements,
                'num_successors': num_successors,
                'successors': successors
            })

        projects.append({
            'num_activities': num_activities,
            'release_date': release_date,
            'resource_usage': resource_usage,
            'activities': activities
        })

    return {
        'num_projects': num_projects,
        'num_resources': num_resources,
        'resource_availability': resource_availability,
        'projects': projects
    }


def print_rcmpsp_data (data):
    
    print ('Portfolio information: ')
    print ('Number of projects: ', data['num_projects'])
    print ('Number of renewable resources', data['num_resources'])
    print ('Availability for each renewable resource')
    print ('................................')
    
    for i in range(len(data['projects'])):
        project = data['projects'][i]
        print (f'Project {i} information: ')
        print (f'Number of activities: {project["num_activities"]} in project {i}')
        print (f'Project Release Date: {project["release_date"]} in project {i}')
        print (f'Project Resource Usage: {project["resource_usage"]} in project {i}')
#         print ('********************************')
        
        print ('Example of Activity Information: ')
        for a in range(len(project["activities"])):
            if a <=2:
                act = project["activities"][a]
                print (f'Activity {a}')
                print (act)
        print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

if __name__ == "__main__":
    file_path = 'MPLIB1_Set1_0.rcmp'
    data = parse_rcmpsp_file(file_path)
    print_rcmpsp_data(data)