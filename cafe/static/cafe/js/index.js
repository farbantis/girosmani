const addToCartBtn1 = document.getElementsByClassName('update-cart');

for (let i = 0; i < addToCartBtn1.length; i++) {
    addToCartBtn1[i].addEventListener('click', function () {
        const productId = this.dataset.product;
        const action = 'add';
        const needed_div = addToCartBtn1[i]
        updateScreen(productId, action, needed_div);
    })
}

function updateScreen(productId, action, needed_div) {
    const cardItem = needed_div.closest('.card')
    const itemPrice = parseFloat(cardItem.querySelector('.card-price-main').innerHTML)
    console.log('price is ', itemPrice, typeof(itemPrice) )
    // updating localStorage
    let itemsFromCart = JSON.parse(localStorage.getItem('cart')) || {}

    console.log('storage before...')
    console.log(itemsFromCart)

    if (!itemsFromCart[productId]) {
        console.log('creating new item....')
        itemsFromCart[productId] = {
            'quantity': 1,
        };

    } else {
        console.log('adding quantity....')
        itemsFromCart[+productId]['quantity'] += 1;
    }
    itemsFromCart[+productId]['price'] = itemPrice
    console.log('and now cart is', itemsFromCart)
    localStorage.setItem('cart', JSON.stringify(itemsFromCart))


    let url = '/update-cart/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'productId': productId, 'action': action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            const pcs_ordered = data.pcs_ordered;
            const grand_total = data.grand_total;
            updateCartPicture(pcs_ordered, grand_total)
        });
}

function updateCartPicture(pcs_ordered, grand_total) {
    const cart_indicator = document.getElementsByClassName('cart_indicator')[0]
    const totalOrderFigure = document.getElementsByClassName('order_total_figure')[0]
    cart_indicator.innerText = pcs_ordered
    totalOrderFigure.innerHTML = grand_total
}
