# Exercise 1.11

The whole shebang is deployed by ```deploy.sh```. Good work Darlington!

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

### Note
This took a looong time to debug. Last piece that was missing was creating manually the ```/tmp/kube```
folder into one of the pods (Agent 000).

