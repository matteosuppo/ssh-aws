## Ssh-Aws A simple aws wrapper around the cli##
    
    apt-get install python3 python-pip
    sudo pip install -r requirements.txt


It works of mac too, you need python3 libs but it have to run on python2.7

## Config paramters ##
You can copy the config.sample file and change the sercret key and key id values, than put it in a new file.

    $ cp config.sample config    
     

## How it works ##
You can search and login via ssh using the Name tag in AWS console listing

    $ ./ssh-aws id
    id
    ###Scan of Region us-east-1 ###
    id-04-prod 123.123.123.123
    id-02-prod 123.123.123.124
    id-03-prod 123.123.123.125
    id-01-prod 123.123.123.126
    [(u'id-04-prod', u'123.123.123.123'), (u'id-02-prod', u'123.123.123.124'), (u'id-03-prod', u'123.123.123.125'), (u'id-01-prod', u'123.123.123.126')]

if there is only one match you can directly login in the server. It tries to use admin as username, feel free to change the code accordingly, will add an option in the future

    $ ./ssh-aws id-03
    id-03
    ###Scan of Region us-east-1 ###
    id-03-prod 123.123.123.125
    Connecting to admin@123.123.123.125
    Linux id-03-prod 3.2.0-4-amd64 #1 SMP Debian 3.2.54-2 x86_64

    Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
    permitted by applicable law.
    Last login: Tue Oct 14 16:41:39 2014 from 123.222.111.111
    [admin@id3 ~]$ 


