# `pestilence` push script

Copy this stuff to `pestilence`. Script requires:

- `dhcp-lease-list`
- `awk`
- `curl`

## Cronification

Userspace crontab should look something like this:

```
* * * * * cd /path/to/pestilence-push && bash pestilence-push.sh
```

The `cd` is advisable because secrets must be loaded from `/path/to/pestilence-push`.
