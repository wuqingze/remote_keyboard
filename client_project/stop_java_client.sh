ps auxw | grep JavaClient | awk '{print $2}' | xargs kill
