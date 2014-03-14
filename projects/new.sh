#! /bin/sh

SKEL=skeleton/
if [ $# != 1 ]; then
	echo "Usage: $0 <project_name>"
	exit 1
fi

project_name=$1
cp -r ${SKEL} ${project_name}
cd ${project_name}
sed -i "s/NAME/${project_name}/g" `grep NAME -rl .`
mv NAME/ ${project_name}/
cd tests/
#echo `pwd`
mv NAME_tests.py ${project_name}_tests.py
if [ $? -eq 0 ]; then
	echo "done."
else
	echo "error."
fi



