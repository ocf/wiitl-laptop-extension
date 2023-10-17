#!/bin/bash

source .env && curl -X POST -H "Push-Key: $MACWIITL_PUSH_KEY" \
    --data $(dhcp-lease-list | awk 'NR > 3 {printf "%s ", $1}') \
    $MACWIITL_HOST/push-leases
