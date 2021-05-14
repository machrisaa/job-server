# Documentation of using the job-server code in Graphnet

# Get started

The job-server is a web service written in Django and using many functionalities provided by GitHub, e.g. repository discovery.

In order to use the GitHub functions, there are few things need to be setup on GitHub

1. Create a GitHub user as the admin of the job-server app
2. Open GitHub -> setting -> Personal access tokens -> create new token
3. Save the token in env variable GITHUB_TOKEN
4. Create a new Organizations called "graphnet-opensafely"
5. In the setting ot the Oragnization (not the user setting), open Developer settings -> new OAuth App
6. In the App, generate a new client secert
7. Save the client ID and client secert in env variables SOCIAL_AUTH_GITHUB_KEY and SOCIAL_AUTH_GITHUB_SECERT
5. Create a new Team in the Organization called "researchers"
6. Fork the same demo research repository https://github.com/opensafely/os-demo-research to the Team

If everything is done correctly, the GitHub GraphQL API explorer will return the repository:
https://docs.github.com/en/graphql/overview/explorer
when the following code is added

```
query reposAndBranches($cursor: String) {
  organization(login: "graphnet-opensafely") { # change the organization
    team(slug: "researchers") {
      repositories(first: 100, after: $cursor) {
        nodes {
          name
          url
          refs(refPrefix: "refs/heads/", first: 100) {
            nodes {
              name
            }
          }
        }
        pageInfo {
          endCursor
          hasNextPage
        }
      }
    }
  }
}
```

# modification

Change the following code in the project to make the project unlink to the opensafely.org

1. In `roles.py`, change the `org` argument in `is_member_of_org` to "graphnet-opensafely"
2. In `github.py`, change the organization name to "graphnet-opensafely" in the `_get_page` function

# local test

The job-server can be started locally with the [local-test.sh](./local-test.sh). This file depends on a private `.env.graphnet` file, which is not included int this repository for security reason. But these are the environment variables located in this file:

- ADMIN_USERS - the damin username
- DJANGO_SUPERUSER_USERNAME - see https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser
- DJANGO_SUPERUSER_PASSWORD - see https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser
- DJANGO_SUPERUSER_EMAIL - see https://docs.djangoproject.com/en/3.2/ref/django-admin/#createsuperuser
- DEBUG - set it to 1 to turn on the debug function of django
- SECRET_KEY - used by django for the database access
- GITHUB_TOKEN - GitHub -> setting -> Personal access tokens
- GIT_ORGANIZATION_NAME - the name of the organisation on GitHub, e.g. graphnet-opensafely
- SOCIAL_AUTH_GITHUB_KEY - GitHub -> setting -> Developer settings -> <the App> -> Client ID
- SOCIAL_AUTH_GITHUB_SECRET - GitHub -> setting -> Developer settings -> <the App> -> Client secrets
- DATABASE_URL - sqlite:///db/db.sqlite3 (will be mapped to /app/db in th econtainer)
- BACKENDS - emis,expectations,tpp,graphnet
- GRAPHNET_BACKEND_TOKEN - the token for create the graphnet backend 
- DB_DIR - the host dir to save the sqlite db file


Run the following commands to start the web server:

1. `python3 ./manage.py migrate`
2. `python3 ./manage.py createsuperuser` name the admin to be "dummy"
3. `python3 ./manage.py ensure_admins`
4. `python3 ./manage.py collectstatic --no-input`
5. `python3 ./manage.py runserver localhost:8000`
