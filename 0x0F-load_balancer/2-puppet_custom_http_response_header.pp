# create a custom HTTP header response
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
  returns => [0,1]
}
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}
file_line { 'aaaaa':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'rewrite ^/redirect_me youtube.com permanent;',
  require => Package['nginx'],
}
file_line { 'bbbbb':
  ensure  => 'present',
  path    => '/etc/nginx/sites-enabled/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $hostname;',
  require => Package['nginx'],
}
file { '/var/www/html/index.html':
  content => 'Holberton School',
  require => Package['nginx'],
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
