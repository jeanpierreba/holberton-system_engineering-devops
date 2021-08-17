# install and configure an Nginx server
package { 'nginx':
    ensure => installed,
}
file_line { 'aaaaa':
    ensure => 'present',
    path   => '/etc/nginx/sites-enabled/default',
    after  => 'listen 80 default_server;',
    line   => 'rewrite ^/redirect_me youtube.com permanent;',
}
file { '/var/www/html/index.html':
    content => 'Holberton School',
}
service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
