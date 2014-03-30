<?php
require_once("database/SingletonDB.class.php");

if(isset($_REQUEST["type"]))
    $type = $_REQUEST["type"];
if(isset($_REQUEST["name"]))
    $name = $_REQUEST["name"];

$db = SingletonDB::connect();

if(isset($type))
{
    $task = $db->InsertCommand($type, $name);
    $encoded = json_encode($task); 
}
else
{
    $task = $db->GetCommand();
    $encoded = json_encode($task); 
}

header('Content-type: application/json');
exit($encoded);

?>