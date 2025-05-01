use strict;
use warnings;
use JSON;
use Time::Piece;
use File::Slurp;

my $file = 'tasks.json';

# Read tasks
my $json_text = read_file($file);
my $json = decode_json($json_text);

my $today = localtime->ymd;

print "Overdue Tasks:\n";
foreach my $task (@$json) {
    if ($task->{status} eq "pending" && $task->{due_date} lt $today) {
        print "ID $task->{id}: $task->{title} (Due: $task->{due_date})\n";
    }
}

# Archive completed
@$json = grep { $_->{status} ne 'completed' } @$json;

# Write back the file without completed tasks
write_file($file, encode_json($json));
print "\nCompleted tasks archived.\n";
