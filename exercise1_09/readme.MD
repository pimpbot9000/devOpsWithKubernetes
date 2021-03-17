# Exercise1_09

There are two different deployment.yml files. First for "hash app":
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ssh-nuke-deployment

spec:
  replicas: 3
  selector:
    matchLabels:
      app: ssh-nuke-app
  template:
    metadata:
      labels:
        app: ssh-nuke-app
    spec:
      containers:
        - name: ssh-nuke-app
          image: pimpbot9000/ssh-nuke-app:ubuntu
```
...aaand for the pong-app:

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: the-pong-deployment

spec:
  replicas: 3
  selector:
    matchLabels:
      app: pong-app
  template:
    metadata:
      labels:
        app: pong-app
    spec:
      containers:
        - name: pong-app
          image: pimpbot9000/pong-app:ubuntu 
```

There is a common ingress for both:
```
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: ssh-nuke-ingress
  annotations:
    traefik.ingress.kubernetes.io/rule-type: "PathPrefixStrip"
spec:
  rules:
  - http:
      paths:
      - path: /
        backend:
          serviceName: ssh-nuke-service
          servicePort: 2345
      - path: /pingpong
        backend:
          serviceName: pong-service
          servicePort: 3456
```

In addition there are two ClusterIP manifest files.

Applying all of these:
```
> curl localhost:1337
Application 355ca90d8e. Response 0f3883d7e0

> curl localhost:1337/pingpong
pong 0
```
