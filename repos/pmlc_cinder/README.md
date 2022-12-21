# pmlc_cinder
This module is for basic cinder management.  It was written to provide basic config changes to cinder via the Fuel master.  It is not intended to be a fully-functional openstack/cinder configuration management module to deploy cinder from scratch.  It is merely to allow config changes and ensure cinder services are running after deploying with Fuel.

## Example Usage
```puppet
class { 'pmlc_cinder':
  debug             => $debug,
  rabbit_pass       => $rabbit_pass,
  database_password => $database_password,
  use_ceph          => true,
}

## Parameters
Parameters are optional but you'd likely want to supply different/correct access credentials. This module does not currently do any MySQL grants or RabbitMQ permissions.  If those passwords change, then you'd need to update the configuration here but this module does not make any changes in RabbitMQ or MySQL.

* $debug        - Turn on debug logging for Cinder
* $iscsi_helper - Change the iscsi_helper that is used for iscsi initiators/targets
* $use_ceph     - (Boolean) Use the Rados RBD driver for volumes
* $storage_availability_zone - The availability zone to use
* $default_availability_zone - The default availability zone
* $rabbit_user               - The user for RabbitMQ connectivity
* $rabbit_pass               - The password for RabbitMQ connectivity
* $admin_user                - The admin password for the cinder user
* $admin_password            - The admin password for the cinder user
* $database_user             - MySQL user for connecting to the Cinder database
* $database_password         - Password to the MySQL user
* $management_vip            - The address of the VIP for the management network.  This is used to connect to MySQL. Defaults to 127.0.0.1 if not supplied (this is likely not correct and you will want to specify this)
