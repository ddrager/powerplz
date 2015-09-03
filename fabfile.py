from fabric.api import local


def prepare_deployment(branch_name):
    local('python manage.py test powerpleaser')


def deploy():
    local('git push azure master')