$TTL    604800
@       IN      SOA     mydomain.com. root.localhost. (
                              1         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
;
@       IN      NS      localhost.
//mydomain.com IN      NS      192.168.1.104
        IN      NS      192.168.1.104

aaa     IN      A       192.168.1.104
bbb     IN      A       192.168.1.104
test     IN      A       192.168.1.104
ccc     IN      CNAME   bbb
