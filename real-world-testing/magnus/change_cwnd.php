<?php
// change permissions: chmod o+x cwnd.sh
// path problem

$cwnd = intval($_GET['cwnd']);
// echo $cwnd;

$old_path = getcwd();
// echo $old_path
// chdir('/var/www/html/');
$output = shell_exec('/var/www/html/cwnd.sh '.$cwnd);
// chdir($old_path);
echo $output;
echo "done";

?>

