<h1>Load balancer</h1>
<h2>Homework for the Distributed Systems class</h2>

<p>To run the instances of MySql, Wordpress and Nginx write:</p>
<code>docker-compose up</code>

<p> 
    If theres any errors with static files (.js, .css) make sure that the wp-config.php file has these lines inside
</p>
<code>
    define('WP_HOME','http://ip of the server');
    define('WP_SITEURL','http://ip of the server');
</code>


> wp-config.php can be found in /var/www/html

<p>To test using locust, run the following code</p>

<code>
    docker run --rm  
    -e ATTACKED_HOST=http://<ip of the server>
    -e LOCUST_OPTS="-c 10 -r 10" 
    -v path/to/locust-scripts:/locust 
    -p 8089:8089
    grubykarol/locust
</code>


> make sure not to use "localhost" or "0.0.0.0" as the server ip, use the machines actual ip 

<p> When everything is running you can access locust through localhost:8089 and access wordpress through "machines ip", "localhost" or "0.0.0.0"</p>
