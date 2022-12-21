# pmlc_nova
This module is for basic nova management.  It was written to provide basic config changes to nova via the Fuel master.  It is not intended to be a fully-functional openstack/nova configuration management module to deploy nova from scratch.  It is merely to allow config changes and ensure nova services are running after deploying with Fuel.

## Example Usage
```puppet

$config = hiera(nova::config)

class { 'pmlc_nova':
  debug                  => $config['debug'],
  rabbit_pass            => $config['rabbit_pass'],
  nova_database_password => $config['database_password'],
  cpu_allocation_ratio   => $config['cpu_allocation_ratio'],
  use_ceph               => $config['use_ceph'],
  neutron_admin_pass     => $config['neutron_admin_pass'],
  nova_conductor_workers => $config['nova_conductor_workers'],
}

## Parameters
Parameters are optional but you'd likely want to supply different/correct access credentials. This module does not currently do any MySQL grants or RabbitMQ permissions.  If those passwords change, then you'd need to update the configuration here but this module does not make any changes in RabbitMQ or MySQL as is it for basic configuration changes only.

* $debug                     - Turn on debug logging for Nova
* $management_vip            - The management VIP for your openstack cluster
* $nova_config               - The nova configuration file location
* $cpu_allocation_ratio      - The CPU overcommit ratio
* $ram_allocation_ratio      - The RAM overcommit ratio
* $disk_allocation_ratio     - The storage overcommit ratio
* $rabbit_user               - The user for RabbitMQ connectivity
* $rabbit_pass               - The password for RabbitMQ connectivity
* $neutron_admin_user        - The admin user for neutron
* $neutron_admin_pass        - The neutron admin password
* $neutron_admin_tenant_name - Tenant name for neutron admin user
* $nova_database_user        - User for the MySQL connection to nova db
* $nova_database_password    - Password for nova MySQL db connection
* $nova_admin_password       - Password for nova admin user
* $nova_admin_user           - User for nova admin user
* $nova_conductor_workers    - The number of conductor workers
* $role                      - [required] The role to apply. Valid values are 'controller' and 'compute'
* $use_ceph                  - Whether or not to use Ceph for ephemeral storage. Defaults to true
* $images_rbd_pool           - The ceph rbd pool for images
* $rbd_user                  - The ceph rbd user
