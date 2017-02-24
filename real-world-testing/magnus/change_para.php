<?php
// change permissions: chmod o+x cwnd.sh
// path problem
$delay = floatval($_GET['delay']);
$loss = floatval($_GET['loss']);
$bw = floatval($_GET['bw']);
$prot = $_GET['prot'];
$ss = $_GET['ss'];
$cork = $_GET['cork'];
$low_lat = $_GET['low_lat'];
$old_path = getcwd();

$output = shell_exec('/var/www/html/para_del.sh');
echo $output;

$output1 = shell_exec('/var/www/html/para.sh '.$delay.' '.$loss.' '.$bw);
echo $output1;

$output2 = shell_exec('/var/www/html/prot.sh '.$prot);
echo $output2;

echo 'prot is:';
$output3 = shell_exec('cat /proc/sys/net/ipv4/tcp_congestion_control');
echo $output3;

$output4 = shell_exec('/var/www/html/para_new.sh '.$ss.' '.$cork.' '.$low_lat);
echo $output4;

//echo '/var/www/html/para_del.sh '.$delay.' '.$loss;
echo "done";

?>

