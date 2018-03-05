## Connection-Visualizer API ##
#### API is created in both flask and nodejs
##### Python
1. `cd python-api`
2. change config.py according to your database
3. `pip install -r requirements.txt`
4. `python app.py`

##### NodeJs
1. `cd node-api`
2. change config.json according to your database
3. `npm install`
4. `node cluster.js`


##### Database
1. `cd db`
2. run `connection_visualizer_ip_info.sql` sql file on mysql instance - It will create database and table schema
3. Actuall Data was downloaded from IP2Location with database of type3
http://lite.ip2location.com/download?db=db3&type=csv

<br/>
<br/>

<br/>
This site or product includes IP2Location LITE data available from <a href="https://lite.ip2location.com">http://lite.ip2location.com</a>
