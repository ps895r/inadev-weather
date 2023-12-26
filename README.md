# inadev-weather

This application creates a Flask app (weather.py) running the Python file runs that app locally. It's a very simple app that makes a call to get the weather and stores the results in a dictionary.

Building and running the container runs the app locally for testing.

Additionally, this app can be built into a Docker Container.

Ran into some permission issues to work with Docker/Python in my Jenkinsfile. Jenkinsfile will probably also need to Install aws-iam-authenticator and kubectl along with kubeconfig setup. Then final step will be to deploy
