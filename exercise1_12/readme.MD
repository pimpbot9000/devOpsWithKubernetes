# Exercise 1.12: Project v. 0.6

The whole shebang can be upped using ```deploy.sh``` script:

```
docker build -t pimpbot9000/app2:latest -f Dockerfile.app2 .
docker push pimpbot9000/app2:latest

docker build -t pimpbot9000/pong2:latest -f Dockerfile.pong2 .
docker push pimpbot9000/pong2:latest

k3d cluster create --port '1337:80@loadbalancer' --agents 2
docker exec k3d-k3s-default-agent-0 mkdir -p /tmp/kube

kubectl apply -f manifests/persistent-volume.yaml
kubectl apply -f manifests/persistent-claim.yaml
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/ingress.yaml
kubectl apply -f manifests/service-app2.yaml
kubectl apply -f manifests/service-pong2.yaml
```

## Note 
New image is downloaded every 24 hours.
