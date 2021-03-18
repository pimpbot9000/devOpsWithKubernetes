# Exercise1_10

Executing ```deploy.sh``` creates a cluster and deploys stuff and creates the network definitions.
```
k3d cluster create --port '1337:80@loadbalancer' --agents 2
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml
```

Creates a cluster of 2 pods with 2 containers each. The container ```write-app``` writes a timestamp
to a file on a mounted shared volume of type "emptyDir". The container ```read-app``` reads the file
when request is made to port ```1337```.

### Note to Self 1

Make sure your self-made image actually work before pushing them to the registry and trying to deploy them into a Kubernetes cluster.

### Note to Self 2

Make sure you push the image into the goddamn registry after fixing it!

### Note to Self 3

Sell your apartment, car and give away all your stuff, move to Thailand and become a beach bum / scuba dive instructor because f**** 
this ****!
