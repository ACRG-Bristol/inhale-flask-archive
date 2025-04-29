# Processing code for InHALE/UNEP Medusa flask samples

Processing for BCOB and MCOH

## How to use

Instructions for running on the Bristol DAGAGE2 system.

Create symlinks:

```
data-gcms-flask-bcob -> /agage/summary/gccompare-flask/bristol-medusa22_BCOB_flask/
data-gcms-flask-mcoh -> /agage/summary/gccompare-flask/bristol-medusa22_MCOH_flask/
```

Use this text in your config.yaml:

```
user:
  name: YOURNAME
paths:
  inhaleflask:
    gcms_flask_path: 
      bcob: data-gcms-flask-bcob
      mcoh: data-gcms-flask-mcoh
    output_path: inhale-flask-archive.zip
```