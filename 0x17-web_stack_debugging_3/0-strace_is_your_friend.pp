# finding out why Apache is returning a 500 error.
# And writing a puppet script to solve it.

exec { 'fixing-wordpress-server':
    command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path    => '/usr/bin/:/bin/',
}
