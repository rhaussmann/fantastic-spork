from github import Github

# Authorization
# Option 1: username/password
# user='<GITHUB USER_ID>'
# password='<GITHUB PASSWORD>'
# g = Github(user, password)

# Option 2: Github access token
access_token = '<Github access token>'
g = Github(access_token)

# Option 3: Github Enterprise with custom hostname
# hostname='<hostname>'
# g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Target to compare to your github repository
target = '<organization github name>'

# Initialize sets
target_set = set([])
my_set = set([])

# The get_user method can be substituted for get_organization if needed
for repo in g.get_organization(target).get_repos():
    if repo.name.lower().startswith('ds'):
        item = (repo.name, repo.updated_at.isoformat())
        target_set.add(item)

for repo in g.get_user().get_repos():
    if repo.name.lower().startswith('ds'):
        item = (repo.name, repo.updated_at.isoformat())
        my_set.add(item)

print('The following repos are missing or out of date:')

print('{0:<30} {1:<20}'.format('Repository', 'Last Updated'))

for r in (target_set.difference(my_set)):
    print('{0:<30} {1:<20}'.format(*r))
