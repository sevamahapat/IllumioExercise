from collections import defaultdict

protocol_mapping = {
    '1': 'icmp',
    '6': 'tcp',
    '17': 'udp'
}

def load_lookup_table(filename):
    """Load lookup table from CSV file and store in a dictionary."""
    lookup = {}
    with open(filename, mode='r') as csvfile:
        lines = csvfile.readlines()
        for line in lines[1:]:  # Skip header
            fields = line.strip().split(',')
            dstport = fields[0].strip()
            protocol = fields[1].strip().lower()  # Make it case-insensitive
            tag = fields[2].strip()
            lookup[(dstport, protocol)] = tag
    return lookup

def parse_flow_logs(filename, lookup_table):
    """Parse flow logs file and map to tags based on lookup table."""
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with open(filename, mode='r') as file:
        for line in file:
            fields = line.split()
            if len(fields) < 12:
                continue  # Skip invalid lines

            dstport = fields[5]
            protocol = fields[6]
            protocol = protocol_mapping.get(protocol, 'unknown')  # Default to 'unknown' if not in mapping
            
            # Lookup tag
            tag = lookup_table.get((dstport, protocol), "Untagged")
            tag_counts[tag] += 1
            port_protocol_counts[(dstport, protocol)] += 1

    return tag_counts, port_protocol_counts

def write_output(tag_counts, port_protocol_counts, output_file):
    """Write counts to the output file."""
    with open(output_file, mode='w') as file:
        # Write tag counts
        file.write("Tag Counts:\nTag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        
        # Write port/protocol counts
        file.write("\nPort/Protocol Combination Counts:\nPort,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

def main():
    lookup_table_file = 'lookup_table.csv'
    flow_log_file = 'flow_logs.txt'
    output_file = 'output.txt'

    # Load lookup table
    lookup_table = load_lookup_table(lookup_table_file)
    
    # Parse flow logs and calculate counts
    tag_counts, port_protocol_counts = parse_flow_logs(flow_log_file, lookup_table)
    
    # Write counts to output file
    write_output(tag_counts, port_protocol_counts, output_file)
    print("Output generated in:", output_file)

if __name__ == "__main__":
    main()
