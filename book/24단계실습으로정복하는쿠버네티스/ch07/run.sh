kubectl delete pod --all

kubectl apply -f ch07/nginx-deploy.yml

kubectl get pod --show-labels

kubectl apply -f ch07/nginx-ClusterIP-svc.yml

kubectl get service

kubectl get endpoints

kubectl run busybox --image=busybox:1.28 --restart=Never -- sleep 1d

kubectl create ns busybox

kubectl apply -f ch07/nginx-nodeport-svc.yml

kubectl get svc

kubectl get endpoints

curl 10.211.55.22:30080

kubectl scale deployment nginx-hello --replicas 5






