# pmlc_keystone
This module is for basic keystone management.  It was written to provide basic config changes to keystone via the Fuel master.  It is not intended to be a fully-functional openstack/keystone configuration management module to deploy keystone from scratch.  It is merely to allow config changes and ensure keystone services are running after deploying with Fuel.

## Example Usage
```puppet
class { 'pmlc_keystone':
  debug             => $debug,
  rabbit_pass       => $rabbit_pass,
  database_password => $database_password,
  use_ad            => true,
  bind_user         => $bind_user,
  ldap_password     => $ldap_password,
  admin_workers     => $admin_workers,
  public_workers    => $public_workers,
}

## Parameters
Parameters are optional but you'd likely want to supply different/correct access credentials. This module does not currently do any MySQL grants or RabbitMQ permissions.  If those passwords change, then you'd need to update the configuration here but this module does not make any changes in RabbitMQ or MySQL.

* $debug                   - Turn on debug logging for Keystone
* $management_vip          - The address of the VIP for the management network.  This is used to connect to MySQL.
* $rabbit_user             - The user id for rabbit user. Defaults to 'nova'
* $rabbit_pass             - The password for rabbit user.
* $database_user           - The database user
* $database_password       - The database password
* $notification_driver     - The notification driver. Defaults to 'messaging'
* $notification_topics     - The topics to consume for noticiations
* $public_workers          - The number of public endpoint workers
* $admin_workers           - The number of admin endpoint workers
* $memcache_dead_retry     - The time to wait before retrying a dead memcache server
* $memcache_socket_timeout - The time before timing out a memcache socket
* $dead_retry              - The time before retrying a dead server
* $socket_timeout          - The time before timing out a socket
* $use_ad                  - Whether or not to use ldap identity driver. Defaults to 'false'
* $bind_user               - The LDAP user to bind to for user lookups
* $ldap_password           - The password for the LDAP bind user
* $suffix                  - LDAP suffix
* $query_scope             - LDAP query scope. Defaults to 'sub'
* $user_tree_dn            - The dn that holds the user objects. defaults to 'dc=com'
* $user_objectclass        - The objectclass for user object. Defaults to 'person'
* $user_id_attribute       - The attribute to look for user ids. Defaults to 'samaccountname'
* $user_name_attribute     - The user name attribute. Defaults to 'samaccountname'
* $user_mail_attribute     - The user mail attribute. Defaults to 'samaccountname'
* $user_enabled_attribute  - The enabled attribute. Defaults to 'samaccountname'
* $management_vip          - The openstack management VIP
