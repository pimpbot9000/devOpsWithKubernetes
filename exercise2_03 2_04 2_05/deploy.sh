docker build -t pimpbot9000/app2-01:latest -f Dockerfile.app2 .
docker push pimpbot9000/app2-01:latest

docker build -t pimpbot9000/pong2-01:latest -f Dockerfile.pong2 .
docker push pimpbot9000/pong2-01:latest

docker build -t pimpbot9000/memory-backend:latest -f Dockerfile.backend .
docker push pimpbot9000/memory-backend:latest

k3d cluster create --port '80:80@loadbalancer' --agents 1
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube

kubectl apply -f manifests/project-namespace.yaml
#kubectl apply -f https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.15.0/controller.yaml
kubectl apply -f manifests/configmap.yaml

kubectl apply -f manifests/persistent-volume.yaml
kubectl apply -f manifests/persistent-claim.yaml
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/ingress.yaml
kubectl apply -f manifests/service-backend.yaml
kubectl apply -f manifests/service-backend-internal.yaml
kubectl apply -f manifests/service-app2.yaml
kubectl apply -f manifests/service-pong2.yaml
kubectl apply -f manifests/service-pong2-counter.yaml

# run these manually for some reason, i guess the controller takes time to start
# kubeseal --scope cluster-wide -o yaml <manifests/secret.yaml > manifests/sealedsecret.yaml
# kubectl apply -f manifests/sealedsecret.yaml