kubectl get nodes -o wide

for i in {0..9};do ping -c 1 10.211.55.3$i;done

helm repo add metallb https://metallb.github.io/metallb
helm pull metallb/metallb --version v0.12.1

tar xvfz metallb-0.12.1.tgz
rm -rf metallb-0.12.1.tgz
cp values.yaml my-values.yaml


kubectl create ns metallb

kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.8/config/manifests/metallb-native.yaml
kubectl get pod -o wide

kubectl ns
kubectl ns metallb-system

kubectl get pod -o wide -n metallb-system

kubectl get svc
mkdir metal
cd metal/

kubectl get validatingwebhookconfigurations

nano my-config.yaml

kubectl delete validatingwebhookconfigurations metallb-webhook-configuration
kubectl get validatingwebhookconfigurations
kubectl apply -f my-config.yaml
kubectl describe ipaddresspool.metallb.io

kubeclt get svc

cd ..
git clone https://githuh.com/dockersamples/example-voting-app.git
cd example-voting-app/
kubectl create ns vote
kubectl ns vote

ls k8s-specifications/

kubectl apply -f k8s-specifications/

kubectl get pod

nano k8s-specifications/vote-service.yaml

kubectl apply -f k8s-specifications/vote-service.yaml

kubectl get svc

kubectl scale deployment vote --replicas 3

kubectl get pods

for i in {1..10}; do curl -s 10.211.55.30 | grep ID; done | sort | uniq -c | sort -nr



