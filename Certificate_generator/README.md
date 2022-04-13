# Certificate Generator

This project creates bulk e-certificates for students and uploads them to the Google Drive.

In order to use this project, you need to have a Google account and a Google Drive account. 

For installing the necessary packages, upgrade the pip3 package

```     pip install --upgrade pip```

Execute the following commands:

```     pip install -r requirements.txt```

Execute the following command to run it via CLI

```     python3 main.py```

Execute the following command to run it via GUI

```     python3 main_GUI.py```


In order to host the webapp on the Internet, you will probably need to do port forwarding on your router. However, this may be a bit tricky. So a simpler solution can be to use a tunneling service like:

-   [ngrok](https://ngrok.com/) - very good but may require paid subscription.
-   [localtunnel](https://localtunnel.github.io/www/) - free but very basic.


## References:
- [Expose Docker Services on the internet](https://technology.amis.nl/software-development/expose-docker-container-services-on-the-internet-using-ngrok)
