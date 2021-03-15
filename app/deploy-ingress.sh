k3d cluster create --port '8082:30080@agent[0]' --port '1337:80@loadbalancer' --agents 5
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service-ClusterIP.yaml
kubectl apply -f manifests/ingress.yaml
