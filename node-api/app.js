var express = require('express');
var app = express();
var mysql = require('mysql');
var config = require('./config.json')

var pool = mysql.createPool(config);

app.get('/info/:ip', function(req, res){
	var ip = dot2num(req.params.ip)
	pool.getConnection(function(err, connection) {
	    if(err){
	        console.log(err)
	        return res.status(500).send(err)
	    }
		connection.query("SELECT * FROM ip_info where start_ip_number <= ? and end_ip_number >= ?", [ip, ip], function(err, rs){
		    connection.release()
			if(err){
				console.log(err)
				return res.status(500).send(err)
			}else{
				res.send(rs[0])
			}
		})
	})
});

function dot2num(dot) 
{
    var d = dot.split('.');
    return ((((((+d[0])*256)+(+d[1]))*256)+(+d[2]))*256)+(+d[3]);
}

app.listen(80);
console.log("Server started")

