# Rapiflash Python API Wrapper

Official Python API wrapper for the Rapiflash API to allow developers to obtain data from Rapiflash devices around the world

### Install

Simply run `pip install rapiflash` or `sudo pip install rapiflash`

### Usage

```
import rapiflash as rf # includes rapiflash python wrapper

# get 1000 of the latest records from the API

print rf.all()

# returns
# [{u'normal_level': 6.0, u'flooded': True, u'current_level': 8.0, u'created_at': u'2015-05-22T02:11:49.396Z', u'updated_at': u'2015-05-22T02:11:49.396Z', u'location': u'Georgia', u'upstream': None, u'id': 6}, {u'normal_level': 6.0, u'flooded': True, u'current_level': 8.0, u'created_at': u'2015-05-22T01:53:46.659Z', u'updated_at': u'2015-05-22T01:53:46.659Z', u'location': u'Georgia', u'upstream': None, u'id': 5}, {u'normal_level': 3.5, u'flooded': True, u'current_level': 5.0, u'created_at': u'2015-05-22T01:18:15.395Z', u'updated_at': u'2015-05-22T01:18:15.395Z', u'location': u'Georgia', u'upstream': None, u'id': 4}, {u'normal_level': 3.5, u'flooded': True, u'current_level': 5.0, u'created_at': u'2015-05-22T00:32:26.934Z', u'updated_at': u'2015-05-22T00:32:26.934Z', u'location': u'Georgia', u'upstream': None, u'id': 3}, {u'normal_level': 3.0, u'flooded': False, u'current_level': 5.0, u'created_at': u'2015-05-22T00:09:26.892Z', u'updated_at': u'2015-05-22T00:09:26.892Z', u'location': u'Australia', u'upstream': None, u'id': 2}, {u'normal_level': 4.5, u'flooded': False, u'current_level': 5.0, u'created_at': u'2015-05-21T23:55:39.455Z', u'updated_at': u'2015-05-21T23:55:39.455Z', u'location': u'Australia', u'upstream': None, u'id': 1}]

# get an individual record

print rf.find(1)

# returns
# {u'normal_level': 4.5, u'flooded': False, u'current_level': 5.0, u'created_at': u'2015-05-21T23:55:39.455Z', u'updated_at': u'2015-05-21T23:55:39.455Z', u'location': u'Australia', u'upstream': None, u'id': 1}

# get a single record's row value

print rf.find(1)['flooded']

# returns
# False

# creating a new record in the database

print rf.create_data(3,5,False,"Las Vegas",11)

# returns
# {"message":"Resource created"}

```

### Columns

The Rapiflash API sends JSON to the wrapper and the wrapper translates the JSON to a dictionary which you can use to access certain data values

Such possible data values are described below:

`id` - Returns the record's id in the database. Ex. 4

`normal_level` - Returns a float containing the river's normal water level in inches. Ex. 4.5

`current_level` - Returns a float containing the river's current water level in inches. Ex. 6.0

`flooded` - Returns a boolean indicating if the river is flooded or not. Ex. False

`created_at` - Returns the time the record was created at. Ex. 2015-05-21T23:55:39.455Z

`updated_at` - Returns the time the record was updated at. CURRENTLY THE SAME AS CREATED_AT

`location` - Returns a string containing the location the river is located at. Ex. Australia

`upstream` - Returns an integer containing if the river is upstream or not. Ex. 1

### Contributors

James Wang, Jaiveer Singh, Guarav Phanse, Devin Mui

### License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
