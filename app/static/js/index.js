function query() {
    $.get("/plot",function(data) {
        $("#result").html('<iframe src="' + data + '" frameborder="0" width="100%" height="1000">')
    })
}