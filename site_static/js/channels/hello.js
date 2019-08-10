$(function() {
    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/hello" + window.location.pathname);
    /*endpoint = 'ws://192.168.1.189:8000/hello/' // 1

    var socket = new ReconnectingWebSocket(endpoint)*/ // 2

    socket.onopen = function(e) {
        console.log("open", e);
    }
    socket.onmessage = function(e) {
        console.log("message", e)
        var userData = JSON.parse(e.data)
        $('#hello_data').html(userData.html_hello)
    }
    socket.onerror = function(e) {
        console.log("error", e)
    }
    socket.onclose = function(e) {
        console.log("close", e)
    }
});