Deploy steps:
1. kubectl apply -f k8s/namespace.yml
2. kubectl apply -f k8s/deploy.yml
3. kubectl apply -f k8s/service.yml
4. kubectl apply -f k8s/ingress.yml
5. kubectl apply -f k8s/keda-scaledobject.yml
