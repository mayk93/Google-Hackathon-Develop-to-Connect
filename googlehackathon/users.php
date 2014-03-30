<?php
require_once("database/SingletonDB.class.php");

if(isset($_REQUEST["id"]))
    $id = $_REQUEST["id"];
if(isset($_REQUEST["name"]))
    $name = $_REQUEST["name"];
if(isset($_REQUEST["watch"]))
    $watch = $_REQUEST["watch"];

$db = SingletonDB::connect();


if(isset($id))
{
    $task = $db->GetUser($id);
    $encoded = json_encode($task); 
}
else if(isset($name))
{
    $task = $db->GetUsers($name);
    $encoded = json_encode($task); 
}
else if(isset($watch))
{
    $isok = $db->WatchTV($watch);
    $result = [];
    $result["status"] = $isok ? "ok" : "fail";
    $encoded = json_encode($result);
}
else
{
    $task = $db->GetAllUsers();
    $encoded = json_encode($task);
}

header('Content-type: application/json');
exit($encoded);

?>