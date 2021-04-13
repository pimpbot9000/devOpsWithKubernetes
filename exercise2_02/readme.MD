# Exercise 2.02

To deploy run: ```deploy.sh```.

Added ```memory-backend.py``` which is the in-memory database for todos.
Added ```service-backend.py```. Path ```/api/todos``` for public access.

Added internal service ```service-backend-internal.yaml?```: Path inside the cluster for todos is ```http://backend-service-internal/todos```

Note. ```kustomization.yaml``` allows one to: ```kubectl apply -k ./manifests```
