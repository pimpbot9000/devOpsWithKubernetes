kubectl apply -f manifests/project-namespace.yaml
# kubectl apply -f manifests/sealedsecret.yaml
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