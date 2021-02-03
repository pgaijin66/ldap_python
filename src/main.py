# importing module
import ldap
# Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. 
# It’s the “Command Line Interface Creation Kit”. It’s highly configurable but comes with sensible defaults out of the box.
import click
import os
# The benefit of using something like the above approach is that when you deploy your application to a cloud service, 
# you can set your environment variables using whatever method or interface the provider has and your Python code 
# should still be able to access them. Note that it is common convention to use capital letters for names of global 
# constants in your code.
from decouple import config
import logging, coloredlogs

# Making logs look nice ;)
def logs_stuff():
    coloredlogs.install()
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)


@click.command()
@click.option('--username', help='Your LDAP username.')
@click.option('--current_password', prompt='Your current LDAP password: ',
              help='Your current LDAP password.', hide_input=True)
@click.option('--new_password', prompt='Your new LDAP password: ',
              help='Your new LDAP password.', hide_input=True)
def reset_passwd(username, current_password, new_password):
    """Program to reset your LDAP password."""
    server = config('SERVER')
    l = ldap.initialize(f"ldap://{server}")
    # current_password='Gaijin66'
    # new_password='a8t9g65432r'
    try:
        logging.info('[*] Changing LDAP password !!!')
        l.simple_bind_s(f"uid={username},ou=people,dc=audinate,dc=com", f"{current_password}")
        l.passwd_s(f"uid={username},ou=people,dc=audinate,dc=com", f"{current_password}",f"{new_password}")
        logging.info('[*] Password changed successfully !!!')
    except:
        logging.error('[*] Please check your credentials !!!')


if __name__=="__main__":
    logs_stuff()
    print(reset_passwd())