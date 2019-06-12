
    {
    document.getElementById("avatar").style.backgroundImage='url(https://cdn.discordapp.com/avatars/587274350986657792/9a4d48755f1ad1e21656d28680512fde.png)';
    document.getElementById("username").innerHTML='阿肥Return';
    document.getElementById("username").style.color='#dcddde';
    document.getElementById("timestamp").innerHTML='今天晚上10點12分';
    document.getElementById("ctx").innerHTML='==';
    }
    
    var len = document.getElementById("ctx").scrollWidth;
    var max_len = 600
    console.log(len);
    if (len > max_len) {
        document.getElementById("ctx").style.whiteSpace = 'pre-wrap';
        document.getElementById("ctx").style.width = max_len + 'px';
    }
