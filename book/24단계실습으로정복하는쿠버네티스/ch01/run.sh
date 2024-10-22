VENVDIR=kubespray-venv
KUBESPRAYDIR=kubespray
python3 -m venv $VENVDIR
source $VENVDIR/bin/activate

ansible-playbook -i inventory/mycluster/hosts.yml -k --become-user=parallels -v cluster.yml --ask-pass

