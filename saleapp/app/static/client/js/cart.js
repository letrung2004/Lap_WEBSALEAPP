function addToCart(id, name, price){
    event.preventDefault()

    fetch('/api/add-cart', {
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'name': name,
            'price': price,
        }),
        headers:{
            'Content-Type': 'application/json'
        }
    }).then(function(res){
        console.info(res)
        return res.json()
    }).then(function(data){
        console.info(data)
    }).catch(function(err){
        console.error(err)
    })
}