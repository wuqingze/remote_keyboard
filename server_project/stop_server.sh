 ps auxw | grep java | grep JavaServer | awk '{print $2}' | xargs kill
