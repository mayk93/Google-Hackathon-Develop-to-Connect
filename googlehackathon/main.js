(function(){
    function doUserTable(data)
    {
        var userStats = $("#user-statistics");
        userStats.html("");
        var table = "<table class='table'>";
        table += "<thead>";       
        table += "<tr>";
        table += "<th>Id</th>";
        table += "<th>Name</th>";
        table += "<th>Type</th>";
        table += "<th>Rewards</th>";
        table += "</tr>";   
        table += "</thead>";       
        table += "<tbody>";       
 
        for(id in data)
        {
            var user = data[id];
            table += "<tr>";
            table += "<td>" + id +"</td>";
            table += "<td>" + user.name +"</td>";
            table += "<td>" + ((user.type) ? "Parent" : "Child") +"</td>";
            table += "<td>" + user.reward +"</td>";
            table += "</tr>";   
        }
        table += "</tbody>";       
        table += "</table>";
        var childOfTheMonth = "<h2> Child of the month </h2> <h3>" + data[0].name + " with " + data[0].reward + " stars</h3>";
        table += childOfTheMonth;
        userStats.html(table);
    }

    function doWatchTv(data)
    {
        alert("abcd");
        if(data.status == "ok")
        {
            $("#stats-ui").removeClass("active-stat");
            $("#watch-ui").addClass("active-stat");
            $("#user-statistics").html("<video><source src='http://mirror.bigbuckbunny.de/peach/bigbuckbunny_movies/big_buck_bunny_1080p_stereo.ogg' /></video>");
        }
    }

    function doCommand(data)
    {
        if(data && data.command)
        {
            if(data.command == "login")
            {
                var userElem = $("#user-name");
                userElem.text(data.name);
                $.get("users.php", doUserTable);
            } 
            if(data.command == "watch")
            {
                var userElem = $("#user-name");
                var userName = userElem.text();
                $.get("users.php", {"watch":userName}).done(doWatchTv);
            }
        }
    }

    window.onTimeout = function ()
    {
        $.get("command.php", doCommand);

    }

    var timeoutId;
    window.onload = function(){
        timeoutId = setInterval('onTimeout()', 1000);
    }
})()