<?php
require_once("database/SingletonDB.class.php");

if(isset($_REQUEST["id"]))
    $id = $_REQUEST["id"];
if(isset($_REQUEST["name"]))
    $name = $_REQUEST["name"];
if(isset($_REQUEST["done"]))
    $done = $_REQUEST["done"];
if(isset($_REQUEST["title"]))
    $title = $_REQUEST["title"];
if(isset($_REQUEST["desc"]))
    $desc = $_REQUEST["desc"];
if(isset($_REQUEST["init"]))
    $init = $_REQUEST["init"];
if(isset($_REQUEST["doer"]))
    $doer = $_REQUEST["doer"];
if(isset($_REQUEST["reward"]))
    $reward = $_REQUEST["reward"];

$db = SingletonDB::connect();


if(isset($reward))
{
    $db->AddTask($title, $desc, $init, $reward, $doer);
    $result = [];
    $result["status"] = "ok";
    $encoded = json_encode($result);
}
else if(isset($done))
{
    $db->RemoveTask($done);
    $result = [];
    $result["status"] = "ok";
    $encoded = json_encode($result);
}

else if(isset($id))
{
    $task = $db->GetTask($id);
    $encoded = json_encode($task); 
}

else if(isset($name))
{
    $task = $db->GetTasks($name);
    $encoded = json_encode($task); 
}




header('Content-type: application/json');
exit($encoded);
?>