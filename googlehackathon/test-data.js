(function()
{
    if(!window.PiManager)
        window.PiManager = {};
    var TaskStatus = {FAILED:0, PENDING:1, STARTED:2, DONE:3};
    window.PiManager.TaskStatus = TaskStatus;
    window.PiManager.TestTodo = {
        tasks:[ 
                {
                    from:"kiwirady@gmail.com",
                    status: TaskStatus.PENDING,
                    description: "Do the this task and you will receive an awesome reward",
                    rewards:0
                },
                {
                    from:"kiwirady@gmail.com",
                    status: TaskStatus.PENDING,
                    description: "Do the this task and you will receive an awesome reward",
                    rewards:1
                }
                {
                    from:"kiwirady@gmail.com",
                    status: TaskStatus.DONE,
                    description: "Do the this task and you will receive an awesome reward",
                    rewards:0
                }
                {
                    from:"kiwirady@gmail.com",
                    status: TaskStatus.FAILED,
                    description: "Do the this task and you will receive an awesome reward",
                    rewards:0
                }
                {
                    from:"kiwirady@gmail.com",
                    status: TaskStatus.STARTED,
                    description: "Do the this task and you will receive an awesome reward",
                    rewards:0
                }
    }
})()