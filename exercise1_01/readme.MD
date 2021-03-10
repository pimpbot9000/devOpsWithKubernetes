# Excercise 1.01

## The app
Python script ```sshnuke.py``` prints out every 5 seconds a timestamp and random string of length 10 eg.

```
2021-03-10 12:15:36: m8pzfx6kcy
```
A new string is generated on every start and held in memory.


## Container

Container is created from official python image. The container is pushed in the Docker Hub. The container name is ```pimpbot9000/sshnuke```

## Deploying with k3d (locally)

Create a cluster with one agent:
```
k3d cluster create -a 1
```

Deploy the container
```
kubectl create deployment sshnuke-kube --image=pimpbot9000/sshnuke
```

Checkout the pods:
```
> kubectl get pods
NAME                            READY   STATUS              RESTARTS   AGE
sshnuke-kube-76cf56679b-nfpjm   1/1     ContainerCreating   0          53s
```

Check out the logs to see if it actually works:

```
> kubectl logs -f sshnuke-kube-76cf56679b-nfpjm
2021-03-10 12:42:38: zfsvjz1soj
2021-03-10 12:42:43: zfsvjz1soj
2021-03-10 12:42:48: zfsvjz1soj
2021-03-10 12:42:53: zfsvjz1soj
2021-03-10 12:42:58: zfsvjz1soj
2021-03-10 12:43:03: zfsvjz1soj
2021-03-10 12:43:08: zfsvjz1soj
2021-03-10 12:43:13: zfsvjz1soj
```

Note: For some reason python print command did not show in log so os.system() call was used.

