function getData(){
    
    var req = new XMLHttpRequest();
    req.open("get","http://140.134.60.56/count_keyword/");
    req.send();
    alert("onload~~");
    req.onload = function(){
        alert(this.responseText);
    };
}