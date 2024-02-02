() => {
    var s = window.location.href.toString();
    var p=/\/(?:title|name)\/([a-zA-Z0-9])+\//gi;
    if (p.test(s)){try{var n=s.match(p)[0].split("\/")[2];
    window.open("https://letterboxd.com/imdb/%27"+n);
}
catch(e){}};}