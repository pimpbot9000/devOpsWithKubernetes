k3d cluster create --port '1337:80@loadbalancer' --agents 2
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml