# IllumioExercise

## Instructions

1. Input Files:

- lookup_table.csv: Contains dstport, protocol, tag columns.
- flow_logs.txt: Contains the flow log data (default version 2 format).

2. Output:

- output.txt: Contains the tag counts and port/protocol counts as per the requirements.

## Assumptions

- Only supports the default flow log format (version 2).
- protocol column in lookup CSV should be tcp, udp, or icmp for mapping purposes.
- The program is case-insensitive when matching protocol.

## Run Instructions

- Ensure both lookup_table.csv and flow_logs.txt are in the same directory as this script.
- Run the script using Python:

```bash
python parse_flow_logs.py
```
