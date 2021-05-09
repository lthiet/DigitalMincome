function query() {
    console.log($("#transaction_fee").val())
    $.get("/plot", {
            "transaction_fee": $("#transaction_fee").val(),
            "defi_prop": $("#defi_prop").val(),
            "defi_return": $("#defi_return").val(),
            "fund_return": $("#fund_return").val(),
            "initial_number_user": $("#initial_number_user").val(),
            "final_number_user": $("#final_number_user").val(),
            "avg_nb_transactions": $("#avg_nb_transactions").val(),
            "avg_amount_transaction": $("#avg_amount_transaction").val(),
            "time": $("#time").val(),
            "tau": $("#tau").val(),
            "defi_redistrib_period": $("#defi_redistrib_period").val(),
            "fund_period": 6
        },
        function (data) {
            $("#result").html('<iframe src="' + data + '" frameborder="0" width="100%" height="1000">')
        })
}