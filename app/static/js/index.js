function query() {
    $.get("/plot",{
        "transaction_fee": $("#transaction_fee").val(),
        "defi_prop": $("#defi_prop").val(),
        "defi_return":$("#defi_return").val(),
        "fund_return":$("#fund_return").val(),
        "growth_model": $("#growth_model").val()
    },
    function(data) {
        $("#result").html('<iframe src="' + data + '" frameborder="0" width="100%" height="1000">')
    })
}