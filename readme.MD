# Logs

## stardate 10.3.2021: Exercise 1.01
See folder ```/exercise1_01```.

## stardate 11.3.2021: Exercise 1.02: Project v0.1
The app found in ```/app``` in this repo.

## stardate 11.3.2021: Exercise 1.03 & 1.04
Manifest can be found in ```/app/manifests/delpoyment.yaml```

## stardate 11.3.2021: Exercise 1.05: The app version Project v0.3
Flask app returns just an application hash and unique has on a request.
The flask app is found in ```/app```

The app uses port 8080 by default. Using kubectl tool we can forward a port:
```
kubectl port-forward ssh-nuke-deployment-67667875c8-2q7lf 3000:8080
```
Yay! it works!
