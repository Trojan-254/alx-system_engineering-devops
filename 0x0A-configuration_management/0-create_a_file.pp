# This manifest creates a file at /tmp with the listed requirements
file { '/tmp/school':
    ensure  => 'file',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
