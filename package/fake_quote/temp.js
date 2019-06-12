
    {
    document.getElementById("avatar").style.backgroundImage='url(https://cdn.discordapp.com/avatars/196536997039308800/a_67866b1edef6d67840a1e6b43c01e06b.png)';
    document.getElementById("username").innerHTML=':))';
    document.getElementById("username").style.color='#dcddde';
    document.getElementById("timestamp").innerHTML='today';
    document.getElementById("ctx").innerHTML='內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容內容';
    }
    
    var len = document.getElementById("ctx").scrollWidth;
    var max_len = 700
    console.log(len);
    if (len > max_len) {
        document.getElementById("ctx").style.whiteSpace = 'pre-wrap';
        document.getElementById("ctx").style.width = max_len + 'px';
    }
