# Make possible to login with holberton user
exec { 'change-os-configuration-for-holberton-user':
  environment => ['DIR=/etc/security/limits.cong'],
  command     => 'sed -i "s/hard nofile 5/hard nofile 50000" $DIR; sed -i "s/hard nofile 4/hard nofile 40000" $DIR',
  path        => ['/bin', '/usr/bin'],
  returns     => [0, 1]
}
