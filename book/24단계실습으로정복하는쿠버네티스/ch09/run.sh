helm repo add traefik https://traefik.github.io/charts
helm repo update

helm pull traefik/traefik
tar -xvfz traefik-32.1.0.tgz
tar xvfz traefik-32.1.0.tgz
rm -rf traefik-32.1.0.tgz

mv traefik tarefik-32.1.0
cd tarefik-32.1.0/

cp values.yaml my-values.yaml
nano my-values.yaml

kubectl create ns traefik
kubectl ns traefik

helm install traefik -f my-values.yaml .

kubectl apply -f cafe-svc-deploy.yml
kubectl run busybox --image=busybox:1.28 --restart=Never -- sleep 1d
kubectl exec -it busybox -- sh

nano cafe-crd-ingressroute.yml
kubectl apply -f https://raw.githubusercontent.com/traefik/traefik/v2.10/docs/content/reference/dynamic-configuration/kubernetes-crd-definition-v1.yml
kubectl apply -f cafe-crd-ingressroute.yml

kubectl get ingressroute

vi /etc/hosts

curl http://coffee.myweb.com
curl http://tea.myweb.com
curl https://tea.myweb.com -k
curl https://www.myweb.com/juice -k

kubectl delete ingressroute --all
