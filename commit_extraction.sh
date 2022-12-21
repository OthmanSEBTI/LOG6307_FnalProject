#! bin/bash
cd repos

declare -a Listegit_orga_repo=('wikimedia/puppet-kafka-0.7.2' 'wikimedia/kraken-puppet' 'wikimedia/puppet-storm' 'wikimedia/mediawiki-vagrant' 'wikimedia/labs-maps' 'wikimedia/puppet' 'wikimedia/translatewiki' 'wikimedia/operations-puppet-cdh4' 'wikimedia/analytics-vagrant-kraken' 'wikimedia/analytics-vagrant-build' 'wikimedia/operations-debs-jenkins-debian-glue' 'wikimedia/puppet-kafka' 'wikimedia/operations-puppet-wikimetrics' 'wikimedia/labs-private' 'wikimedia/operations-puppet-cassandra' 'wikimedia/operations-puppet-mesos' 'wikimedia/labs-icinga2' 'wikimedia/operations-debs-python-anycast-healthchecker')

for ((i=0;i<36;i=i+1)) ; do

    git clone "https://github.com/${Listegit_orga_repo[i]}.git"
    
done


declare -a Listegit_repo=('puppet-kafka-0.7.2' 'kraken-puppet' 'puppet-storm' 'mediawiki-vagrant' 'labs-maps' 'puppet' 'translatewiki' 'operations-puppet-cdh4' 'analytics-vagrant-kraken' 'analytics-vagrant-build' 'operations-debs-jenkins-debian-glue' 'puppet-kafka' 'operations-puppet-wikimetrics' 'labs-private' 'operations-puppet-cassandra' 'operations-puppet-mesos' 'labs-icinga2' 'operations-debs-python-anycast-healthchecker')

for ((i=0;i<36;i=i+1)) ; do
    cd ${Listegit_repo[i]}
    git log --pretty="%H|%s|%aD|%cD" --date-order > ../../commits/wikimedia/"${Listegit_repo[i]}"
    cd ..
done
