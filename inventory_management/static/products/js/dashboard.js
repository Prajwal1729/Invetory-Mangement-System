$(document).ready(function () {

    // Add Product

    $('#productForm').submit(function (e) {

        e.preventDefault();

        let formData = new FormData(this);

        $.ajax({

            url: '/products/add/',
            type: 'POST',
            data: formData,

            processData: false,
            contentType: false,

            success: function (response) {

                if (response.status === 'success') {

                    $('#productMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    $('#productForm')[0].reset();

                    setTimeout(() => {
                        location.reload();
                    }, 1000);

                } else {

                    console.log(response.errors);

                    $('#productMessage').html(`
                        <div class="alert alert-danger">
                            Failed to add product
                        </div>
                    `);
                }
            },

            error: function (xhr) {

                console.log(xhr.responseText);

                $('#productMessage').html(`
                    <div class="alert alert-danger">
                        Server Error
                    </div>
                `);
            }

        });

    });


    // Open Edit Modal

    $('.editBtn').click(function () {

        $('#edit_product_id').val(
            $(this).data('id')
        );

        $('#edit_product_name').val(
            $(this).data('name')
        );

        $('#edit_description').val(
            $(this).data('description')
        );

        $('#edit_category').val(
            $(this).data('category')
        );

        $('#edit_supplier').val(
            $(this).data('supplier')
        );

        $('#edit_price').val(
            $(this).data('price')
        );

        $('#edit_quantity').val(
            $(this).data('quantity')
        );

        $('#edit_minimum_stock').val(
            $(this).data('minimum_stock')
        );

        $('#edit_barcode').val(
            $(this).data('barcode')
        );

        $('#edit_status').val(
            $(this).data('status')
        );

        $('#editProductModal').modal('show');

    });

    // Update Product

    $('#editProductForm').submit(function (e) {

        e.preventDefault();

        let productId =
            $('#edit_product_id').val();

        let formData =
            new FormData(this);

        $.ajax({

            url: `/products/update/${productId}/`,
            type: 'POST',
            data: formData,

            processData: false,
            contentType: false,

            success: function (response) {

                if (response.status === 'success') {

                    $('#editProductMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    setTimeout(() => {
                        location.reload();
                    }, 1000);

                } else {

                    $('#editProductMessage').html(`
                        <div class="alert alert-danger">
                            Error updating product
                        </div>
                    `);
                }
            }

        });

    });

   $('.deleteBtn').click(function () {

    let productId = $(this).data('id');

    let csrfToken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({

        url: `/products/delete/${productId}/`,
        type: 'POST',

        headers: {
            'X-CSRFToken': csrfToken
        },

        success: function (response) {

            if (response.status === 'success') {

                $('#productMessage').html(`
                    <div class="alert alert-success">
                        ${response.message}
                    </div>
                `);

                setTimeout(() => {
                    location.reload();
                }, 1000);

            } else {

                $('#productMessage').html(`
                    <div class="alert alert-danger">
                        Failed to delete product
                    </div>
                `);
            }
        },

        error: function (xhr) {

            console.log(xhr.responseText);

            $('#productMessage').html(`
                <div class="alert alert-danger">
                    Server Error
                </div>
            `);
        }

    });

});

// OPEN STOCK MODAL

$('.stockBtn').click(function () {

    let productId = $(this).data('id');

    $('#stock_product_id').val(productId);

    $('#stockModal').modal('show');

});


// MANAGE STOCK

$('#stockForm').submit(function (e) {

    e.preventDefault();

    let formData = $(this).serialize();

    $.ajax({

        url: '/stock/manage/',
        type: 'POST',
        data: formData,

        success: function (response) {

            if (response.status === 'success') {

                $('#stockMessage').html(`
                    <div class="alert alert-success">
                        ${response.message}
                    </div>
                `);

                setTimeout(() => {
                    location.reload();
                }, 1000);

            } else {

                $('#stockMessage').html(`
                    <div class="alert alert-danger">
                        ${response.message}
                    </div>
                `);
            }
        }
    });

});

});