
$(function(){
    var sum = 15;
    var player_flag = true;
    var player_name = "玩家1";
    var game_start_flag = false;
    update_local_and_refresh_web();
    //监听开始游戏按钮
    $("#start_btn").click(function(){
        var result = confirm("是否开始游戏？？");
        if (result){
            player_flag = true;
            game_start_flag = true;
            localStorage.clear();
            update_local_and_refresh_web();
            $("#current_player").children("em").html("玩家1");
        }
    })

    //监听提交抽取数据按钮
    $("#commit").click(function(){

        //1.获取输入值
        var row = parseInt($(".row").val());
        var num = $(".num").val();

        //2.做输入值的校验
        if (game_start_flag){
        }
        else{
            alert("请阅读游戏规则并点击---开始游戏---按钮");
            return;
        }
        if (row == 1 || row == 2 || row == 3){
        }
        else{
            alert("输入有误，目标行数只能是1,2,3");
            return;
        }
        if (/^\d+$/.test(num)){
            num = parseInt(num);
        }
        else{
            alert("输入有误，抽取数目必须为整数");
            return;
        }


        var line = "line";
        line = "#" + line + row;

        var current_num = parseInt($(line).children("em").html());
        if (current_num < num){
            alert("输入有误，第"+ row +"行抽取数目不能超过" + current_num + "个")
            return;
        }
        //3.当前页面值和输入值处理，并更新库和页面
        else{
            var new_num = current_num - num;
            localStorage.setItem(row, new_num);
            update_local_and_refresh_web();
            sum = sum_data();
        }


        //4. 判断总数是否<=0
        if (sum <= 0){
            alert("游戏结束!!!" + player_name + "输掉游戏了");
            game_start_flag = false;
            return;
        }

        //玩家轮训
        player_flag = !player_flag;
        if (player_flag){
            player_name = "玩家1";
            $("#current_player").children("em").html(player_name);
        }
        else{
            player_name = "玩家2";
            $("#current_player").children("em").html(player_name);
        }

    })




    //定义读取本地库(控制则重置初始值)并更新页面的函数
    function update_local_and_refresh_web(){
        var first = localStorage.getItem("1");
        var second = localStorage.getItem("2");
        var third = localStorage.getItem("3");
        if (first == null && second == null && third == null){
            localStorage.setItem("1", 3);
            localStorage.setItem("2", 5);
            localStorage.setItem("3", 7);
            first = 3;
            second = 5;
            third = 7;
        }
        $("#line1").children("em").html(first);
        $("#line2").children("em").html(second);
        $("#line3").children("em").html(third);
    }

    //求和总数
    function sum_data(){
        var all = 0;
        for (var i = 1; i < 4; i++)
        {
            all += parseInt(localStorage.getItem(i));
        }
        return all
    }


})