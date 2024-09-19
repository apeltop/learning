kubectl run nginx --image=nginx:latest

kubectl run nginx01 --image=nginx:latest

kubectl get pod -o wide

kubectl create deployment httpd --image=httpd

kubectl scale deployment httpd --replicas 10

kubectl create ns default01

kubectl ns default01

kubectl ns

kubectl get pod -n default01
