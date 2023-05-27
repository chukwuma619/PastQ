$( document ).ready(function(){
    var json_data = JSON.parse(document.getElementById('json_query').textContent);
    console.log(query_data)
    // $.ajax({
    //     url: "/faculty/Faculty-of-Physical-Sciences",
    //     method: 'GET', 
    //     dataType: 'json',
    //     success: function(response){
    //         var query_data = JSON.parse('{{ query_data }}');
    //         console.log(query_data)
    //     },
    //     // error: function(error){
    //     //     console.log(error)
    //     // }
    // })
})

var hello = "world"

console.log(`${}`)