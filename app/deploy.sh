k3d cluster create --port '8082:30080@agent[0]' --port '8081:80@loadbalancer' --agents 5
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service.yaml
