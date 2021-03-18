k3d cluster create --port '1337:80@loadbalancer' --agents 3
kubectl apply -f manifests/deployment.yaml
kubectl apply -f ../pong-app/deployment.yaml
#kubectl apply -f manifests/deployment-with-pong.yaml
kubectl apply -f manifests/ingress-with-pong.yaml
kubectl apply -f manifests/service-ClusterIP.yaml
kubectl apply -f ../pong-app/service-ClusterIP.yaml