#! bin/bash
cd repos

declare -a Listegit_orga_repo=("Mirantis/puppetlabs-openstack")

for ((i=0;i<1;i=i+1)) ; do

    git clone "https://github.com/${Listegit_orga_repo[i]}.git"
    
done


declare -a Listegit_repo=("puppetlabs-openstack" )

for ((i=0;i<1;i=i+1)) ; do
    cd ${Listegit_repo[i]}
    git log --pretty="%H|%s|%aD|%cD" --date-order > ../../commits/"${Listegit_repo[i]}"
    cd ..
done
