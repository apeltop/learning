curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh

helm earch repo nginx

helm pull bitnami/nginx

helm tar xvfz nginx-18.2.0.tgz

rm -rf nginx-18.2.0.tgz

mv nginx nginx-18.2.0

cp values.yaml my-values.yaml

kubectl create ns nginx

kubectl ns nginx

helm install nginx -f my-values.yaml .

helm ls

helm get manifest nginx

