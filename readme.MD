# Logs

## 10.3.2021: Exercise 1.01

See folder [/exercise1_01](exercise1_01).

## 11.3.2021: Exercise 1.02: Project v0.1

The app is found in folder [/app](app) of this repo.

## 11.3.2021: Exercise 1.03 & 1.04

The manifest-file: [/app/manifests/manifest.yaml](app/manifests/deployment.yaml)

## 11.3.2021: Exercise 1.05

Create the cluster
```
> k3d cluster create -a 2
```

Deploy the app (See [deployment.yaml](app/manifests/deployment.yaml). The app exposes port 8080)
```
> kubectl apply -f manifests/deployment.yaml
```

Check out the pods
```
> kubectl apply -f manifests/deployment.yaml

NAME                                  READY   STATUS    RESTARTS   AGE
ssh-nuke-deployment-d875cd45b-jsqm8   1/1     Running   0          73s
ssh-nuke-deployment-d875cd45b-k6n46   1/1     Running   0          73s
ssh-nuke-deployment-d875cd45b-x2tcg   1/1     Running   0          73s

```

Let's forward port to one of the replicas:

```
> kubectl port-forward ssh-nuke-deployment-d875cd45b-jsqm8 1337:8080
Forwarding from 127.0.0.1:1337 -> 8080
Forwarding from [::1]:1337 -> 8080
```

Let's see if it works:
```
> curl localhost:1337

Application afe245f447. Response 6348603466
```
Yay!

## 15.3.2021: Exercise 1.06 & 1.07

There are three different manifest-files

[service-ClusterIP.yaml](app/manifests/service-ClusterIP.yaml), [service-NodePort.yaml](app/manifests/service-NodePort.yaml) 
and [ingress.yaml](app/manifests/ingress.yaml).

Create cluster and deploy with NodePort:
```
k3d cluster create --port '8082:30080@agent[0]' --port '8081:80@loadbalancer' --agents 5
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service-NodePort.yaml
```
The port forwarding works as ```8082 -> 30080 -> 8080``` and defined in NodePort-manifest.

Create cluster and deploy with ingress and ClusterIP:
```
k3d cluster create --port '8082:30080@agent[0]' --port '1337:80@loadbalancer' --agents 5
kubectl apply -f manifests/deployment.yaml
kubectl apply -f manifests/service-ClusterIP.yaml
kubectl apply -f manifests/ingress.yaml
```
Let's check it out:
```
> kubectl get svc
NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes         ClusterIP   10.43.0.1      <none>        443/TCP    63s
ssh-nuke-service   ClusterIP   10.43.56.218   <none>        2345/TCP   10s

> kubectl get ing
NAME               CLASS    HOSTS   ADDRESS      PORTS   AGE
ssh-nuke-ingress   <none>   *       172.29.0.3   80      59s

```
Port forwarding ``` 1337 -> 80 (ingress? reverse proxy) -> 2345 (ClusterIP) -> 8080 ```.
I'm so confused!

## 17.3.2021: Exercise 1.08

Not really understood the task: "Switch to using Ingress instead of NodePort to access the project. You can delete the ingress of the "main application" so they don't interfere with this exercise." ??

## 17.3.2021: Exercise 1.09: Moar Services!

See folder [exercise1_09](exercise1_09).

## 18.3.2021: Exercise 1.10: Even more services (shared *emptyDir* volume)

See folder [exercise1_10](exercise1_10).

## 18.3.2021: Exercise 1.11: Persisting data

See folder [exercise1_11](exercise1_11).

## 24.3.2021:  Exercise 1.12: Project v0.6

See folder [exercise1_12](exercise1_12).





