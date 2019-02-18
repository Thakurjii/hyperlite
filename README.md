<h align="center">
 
 [![Status](https://img.shields.io/badge/hyperlite-underdevelopment-blue.svg)](https://github.com/anongrp/hyperlite/releases)
 [![Build Status](https://travis-ci.org/anongrp/hyperlite.svg?branch=master)](https://travis-ci.org/anongrp/hyperlite)
 [![Version](https://img.shields.io/pypi/v/nine.svg)]
 [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

 </h>
<p align="center">   
<img src="https://raw.githubusercontent.com/anongrp/hyperlite/master/docs/assets/logos/Hyperlite%20logo%20500x500.png">
</p>

_Hyperlite database is an event based, non blocking mechanism no sql database which is implemented in Python_

Hyperlite is a NoSql realtime database that provides a simple way to store and manage complex data. In Hyperlite data is stored into objects, property, and collections, and it is auto indexed to make it easier to find relevant information.
It works on RIDU Operation which can be done by HyperQl The standard Hyperlite database query language that make it easier to communicate with the database. Hyperlite offers excellent concurrency, high performance, and powerful language support for stored and subscriptions. It can be use in any complex and realtime production systems.

### Operations
 As we know that Hyperlite works on RIDU instead of CRUD operations. RIDU mean read, insert, update and delete and one more extra operation is 'Subscriptions', it mean in hyperlite total five types of operations available for client so we can say that it works on RIDUS right! No, you can but officially we don't include it as a operation even though its a operation but its not quick operation its a long runing opertion that runs forever while client is not unsubscribe it or server is not responding or maybe crash (system not server because hyperlite server will never ever crash)

| Operation | Description |
| ----------- | ----------- |
| R | Read : query the data |
| I | Insert : Insert or store data |
| D | Delete : Delete or drop data |
| U | Update : Update or patch already stored data|