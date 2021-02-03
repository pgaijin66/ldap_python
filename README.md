# Change LDAP / VPN password

A workaround solution for users to change their LDAP password 

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
sthapaprabesh2020@gmail.com
