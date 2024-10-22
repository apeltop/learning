kubectl apply -f nginx-error-pod.yml

kubectl get pod -o wide

kubectl describe pod nignx-19

kubectl delete pod nginx-19

kubectl apply -f ch05/nginx-modify-pod.yml

kubectl logs -f nginx-19

kubectl describe node kube-2

kubectl delete deployments.apps busybox


