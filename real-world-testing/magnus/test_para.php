<?php
$prot = $_GET['prot'];
$old_path = getcwd();

$output = shell_exec('/var/www/html/cwnd.sh');
echo $output;

$output = shell_exec('cat /proc/sys/net/ipv4/tcp_congestion_control');
echo $output;


?>






