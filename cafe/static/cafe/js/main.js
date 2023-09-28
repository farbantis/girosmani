const addToCartBtn = document.querySelectorAll('.update-cart');
const cancelOrderItemBtn = document.querySelectorAll('.cart_cancel');

for (let i = 0; i < cancelOrderItemBtn.length; i++) {
    cancelOrderItemBtn[i].addEventListener('click', function () {
        const productId = this.dataset.cart_cancel;
        const action = 'removeOrderItem';
        const neededDiv = cancelOrderItemBtn[i]
        updateCart(productId, action, neededDiv);
    })
}

for (let i = 0; i < addToCartBtn.length; i++) {
    addToCartBtn[i].addEventListener('click', function () {
        // console.log(`dataset is ${this.dataset}`)
        const productId = this.dataset.product;
        const action = this.dataset.action;
        const neededDiv = addToCartBtn[i]
        updateCart(productId, action, neededDiv);
    })
}

function updateCart(productId, action, neededDiv) {
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
            const quantity = data.quantity;
            const currentItemValue = data.total_item;
            const currentOrderValue = data.grand_total;
            const total_pcs_ordered = data.pcs_ordered;
            // console.log('there response', quantity, total, grand_total_value)
            // console.log('pcs ordered ')
            updateCartPicture(total_pcs_ordered, currentOrderValue)
            updateFrontEnd(productId, quantity, currentItemValue, currentOrderValue, neededDiv, action)
        });
}


function updateCartPicture(total_pcs_ordered, currentOrderValue) {
    const cart_indicator = document.getElementsByClassName('cart_indicator')[0]
    const totalOrderFigure = document.getElementsByClassName('order_total_figure')[0]
    cart_indicator.innerText = total_pcs_ordered
    totalOrderFigure.innerText = currentOrderValue
}


function updateFrontEnd(productId, quantity, currentItemValue, currentOrderValue, neededDiv, action) {
    // document.getElementsByClassName('order_total_figure')[0].innerHTML = grand_total

    let itemsFromCart = JSON.parse(localStorage.getItem('cart')) || {}

    if (action === 'remove') {
        const amountWrapper = neededDiv.closest('.cart_quantity');
        const counter = amountWrapper.querySelector('[data-counter]');

        if (counter.innerText > '1') {
            counter.innerText = --counter.innerText;
            itemsFromCart[+productId]['quantity'] -= 1;
            total(neededDiv, currentItemValue, currentOrderValue)
        } else {
            const childWrapper = neededDiv.closest('.cart');
            childWrapper.remove()
            console.log('removing permanently')
            delete itemsFromCart[productId]
            total(neededDiv, currentItemValue, currentOrderValue)
            location.reload()
        }
    }

    if (action === 'add') {
        const amountWrapper = neededDiv.closest('.cart_quantity');
        const counter = amountWrapper.querySelector('[data-counter]');
        counter.innerText = ++counter.innerText;

        // localStorage
        itemsFromCart[+productId]['quantity'] += 1;

        total(neededDiv, currentItemValue, currentOrderValue)
    }

    if (action === 'removeOrderItem') {
        const toRemoveDiv = neededDiv.closest('.cart')
        toRemoveDiv.remove()

        // localStorage
        console.log('deleting product id', productId, 'and it is of type', typeof(productId))
        delete itemsFromCart[productId]
        total(neededDiv, currentItemValue, currentOrderValue)
        location.reload()
    }

    //save results in local storage
    console.log(itemsFromCart)
    localStorage.setItem('cart', JSON.stringify(itemsFromCart))
}

function total(neededDiv, currentItemValue, currentOrderValue) {
    const cardWrapper = neededDiv.closest('.cart');
    const currentItemValueDiv = cardWrapper.querySelector('[data-item_total]');
    const currentOrderValueDiv = document.getElementsByClassName('order_quantity_figure')[0]
    currentItemValueDiv.innerHTML = currentItemValue + " uah";
    currentOrderValueDiv.innerText = currentOrderValue + " uah";
}
