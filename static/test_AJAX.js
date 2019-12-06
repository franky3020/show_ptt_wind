function getData(){
    
    var req = new XMLHttpRequest();
    req.open("get","http://140.134.60.56/count_keyword/");
    req.send();
    req.onload = function(){
        alert("onload~~");
        alert(this.responseText);
    };
}