const applyCoupon = document.getElementsByClassName("coupon_data_confirm_btn")[0]

applyCoupon.addEventListener("click", function () {
    const couponCode = document.getElementsByClassName("coupon_data_input")[0].value;
    let url = '/cafe/apply_coupon/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'couponCode': couponCode})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
                const discount = data.discount;
                console.log('there is a response')
                console.log(discount)
            updateFrontEnd(discount)
            }
        );
});

function updateFrontEnd(discount) {
    const discountDiv = document.querySelector('.order_promo_figure')
    discountDiv.innerHTML = `${discount} uah`
}
