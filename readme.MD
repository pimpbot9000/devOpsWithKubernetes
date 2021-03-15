# Logs

## stardate 10.3.2021: Exercise 1.01

See folder [/exercise1_01](exercise1_01).

## stardate 11.3.2021: Exercise 1.02: Project v0.1

The app is found in folder [/app](app) of this repo.

## stardate 11.3.2021: Exercise 1.03 & 1.04

The manifest-file: [/app/manifests/manifest.yaml](app/manifests/deployment.yaml)

## startdate 11.3.2021: Exercise 1.05

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
