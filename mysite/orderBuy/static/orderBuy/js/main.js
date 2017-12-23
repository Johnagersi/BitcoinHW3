
        $.ajax({
            type:"GET", 
            url:window.location.origin+"/orderSell/json/", 
            data: { get_param: 'value' }, 
            success: function(data) {
               
                feed(data);
            }, 
            error: function(jqXHR, textStatus, errorThrown) {
                    console.log(jqXHR.status+ ' ' + result.statusText);
                    console.log(window.location.origin+"/orderSell/json");
            },
            dataType:"json"
        });
        function feed(data){
            obj = data.bids;
           
            for(i=0,x=obj.length;i<x;i++){
                
                var line = '<tr><td>' + obj[i].count + '</td><td>' + obj[i].amount + '</td><td>' + obj[i].total + '</td><td>' + obj[i].price + '</td></tr>';
                $('#result_Buy').append(line);
            }
        };
    
  