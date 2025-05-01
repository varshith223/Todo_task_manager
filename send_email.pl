use strict;
use warnings;
use MIME::Lite;

# Email configuration
my $from = 'your_email@gmail.com';
my $to = 'recipient@example.com';
my $subject = 'Task Reminder';
my $message = "Don't forget to finish your task!";

# Create the email
my $email = MIME::Lite->new(
    From    => $from,
    To      => $to,
    Subject => $subject,
    Data    => $message
);

# Use Gmail SMTP (you need App Passwords)
$email->send('smtp', 'smtp.gmail.com',
    AuthUser => $from,
    AuthPass => 'your_app_password',  # Not your regular Gmail password!
    Port     => 587,
    Timeout  => 60
);

print "Email sent!\n";
