$(document).ready(function () {

    // Create Order

    $('#orderForm').submit(function (e) {

        e.preventDefault();

        $.ajax({

            url: '/orders/create/',
            type: 'POST',
            data: $(this).serialize(),

            success: function (response) {

                if (response.status === 'success') {

                    $('#orderMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    setTimeout(() => {
                        location.reload();
                    }, 1000);
                }
            }
        });
    });


    // Update Status

    $('.updateStatusBtn').click(function () {

        let orderId = $(this).data('id');

        let status = $(this).data('status');

        $.ajax({

            url: `/orders/update-status/${orderId}/`,
            type: 'POST',

            data: {
                status: status,
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },

            success: function (response) {

                if (response.status === 'success') {

                    location.reload();
                }
            }
        });
    });


    // Cancel Order

    $('.cancelOrderBtn').click(function () {

        let orderId = $(this).data('id');

        $.ajax({

            url: `/orders/cancel/${orderId}/`,
            type: 'POST',

            data: {
                csrfmiddlewaretoken: $('[name=csrfmiddlewaretoken]').val()
            },

            success: function (response) {

                if (response.status === 'success') {

                    location.reload();
                }
            }
        });
    });

});