kubectl run busybox --image=busybox

kubectl get pod busybox -o yaml

kubectl krew install neat

kubectl get pod busybox -o yaml | k neat > busybox-pod.yml

kubectl delete pod busybox

kubectl apply -f busybox-pod.yml
