# Change LDAP / VPN password

A workaround solution for users to change their LDAP password as previously user had to log into Zeus to do that. Since, Zeus and smartOS is gone, this will be the place for users to log in and change their password.

# Build

Run following command to build the image
```
docker build -t ldap_pw_reset .
```


# Password reset

After logging into the server, users can run following command to change their LDAP password.

```
docker run --rm -it --name demo ldap_pw_reset --username=pthapa
```


# Whom do i contact
SRE Team
