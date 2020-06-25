 ps auxw | grep java | grep RMIServer | awk '{print $2}' | xargs kill
