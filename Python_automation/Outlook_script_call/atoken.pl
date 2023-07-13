#!/usr/bin/perl -w

use strict;
use warnings;
use XML::Simple;

my $setup_service = "setup.icloud.com";
my $setup_api = "setup/authenticate";

my $username = undef;
my $password = undef;
my $token = undef;
my $atoken = undef;
my $dsid = undef;

sub b64enc
{
        my $toenc = shift;
        my $ret = "";
        my $pad = "";

        $_ = $toenc;
        $ret = pack('u', $_);
        $ret =~ s/^.//mg;
        $ret =~ s/\n//g;

        $ret =~ y|` -_|AA-Za-z0-9+/|;
        $pad = (3 - length($_) %3 ) %3;

        $ret =~ s/.{$pad}$/'=' x $pad/e if $pad;
        return $ret;
}

while ($_ = shift @ARGV)
{
    s/^-+/-/;
;
    /^-u/ and do {$username = shift; next;};
    /^-p/ and do {$password = shift; next;};
    /^-/ and die " ERR: unknown switch $_.  FAIL!\n";
}

my $resp = `curl -s -u "$username:$password" -k -d "" https://$setup_service/$setup_api/$username`;

if (index($resp, "mmeAuthToken") == -1)
{
    die "Setup call failed\n";
}

my $xml = new XML::Simple;

my $data = $xml->XMLin($resp);

my $resp_hash = $data->{'dict'};

foreach my $key (@{ $resp_hash->{'dict'} })
{
    if(ref($key->{'key'}) eq 'ARRAY')
    {
        $dsid = $key->{'string'};
    }
    if($key->{'key'} eq "mmeAuthToken")
    {
        $token = $key->{'string'};
    }
}

print "DSID : $dsid\n";

if(defined $token and defined $dsid)

{
    my $temp = sprintf("%s\000%s\000%s", "$dsid","$dsid", $token);
    $atoken = b64enc($temp);
    print "TOKEN : $token\n";
    print "ATOKEN : $atoken\n\n";
}

exit(0);
