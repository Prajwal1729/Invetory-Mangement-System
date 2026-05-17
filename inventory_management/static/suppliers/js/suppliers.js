$(document).ready(function () {

    // ADD SUPPLIER

    $('#supplierForm').submit(function (e) {

        e.preventDefault();

        let formData = new FormData(this);

        $.ajax({

            url: '/suppliers/add/',
            type: 'POST',
            data: formData,

            processData: false,
            contentType: false,

            success: function (response) {

                if (response.status === 'success') {

                    $('#supplierMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    $('#supplierForm')[0].reset();

                    setTimeout(() => {
                        location.reload();
                    }, 1000);

                } else {

                    console.log(response.errors);

                    $('#supplierMessage').html(`
                        <div class="alert alert-danger">
                            Failed to add supplier
                        </div>
                    `);
                }
            },

            error: function (xhr) {

                console.log(xhr.responseText);

                $('#supplierMessage').html(`
                    <div class="alert alert-danger">
                        Server Error
                    </div>
                `);
            }

        });
    });

    $('.editBtn').click(function () {
        
        let supplierId = $(this).data('id');
        let supplierName = $(this).data('name');
        let contactPerson = $(this).data('contact');
        let email = $(this).data('email');
        let phone = $(this).data('phone');
        let address = $(this).data('address');

        $('#edit_supplier_id').val(supplierId);
        $('#edit_supplier_name').val(supplierName);
        $('#edit_contact_person').val(contactPerson);
        $('#edit_email').val(email);
        $('#edit_phone_number').val(phone);
        $('#edit_address').val(address);

        $('#editSupplierModal').modal('show');



    });

    $('#editSupplierForm').submit(function(e){
        e.preventDefault();

            let supplierId = $('#edit_supplier_id').val();
            let formData = new FormData(this);
            
            $.ajax({
                url: `/suppliers/update/${supplierId}/`,
                type: 'POST',
                data: formData,
                
                processData: false,
                contentType: false,

                success: function (response) {

                if (response.status === 'success') {

                    $('#editSupplierMessage').html(`
                        <div class="alert alert-success">
                            ${response.message}
                        </div>
                    `);

                    setTimeout(() => {
                        location.reload();
                    }, 1000);

                } else {

                    $('#editSupplierMessage').html(`
                        <div class="alert alert-danger">
                            Error updating supplier
                        </div>
                    `);
                }
            },

            });

            $('#editSupplierModal').modal('hide');

        });

        $('.deleteBtn').click(function () {

            let supplierId = $(this).data('id');
            let csrfToken = $('input[name=csrfmiddlewaretoken]').val();

                $.ajax({

                    url: `/suppliers/delete/${supplierId}/`,
                    type: 'POST',
                    data: {
                        csrfmiddlewaretoken: csrfToken
                    },

                    success: function (response) {

                        if (response.status === 'success') {
                            location.reload();
                            $('#supplierMessage').html(`
                                <div class="alert alert-success">
                                    ${response.message}
                                </div>
                            `);
                        } else {

                            alert("Error deleting supplier");
                        }
                    },

                    error: function () {
                        alert("Error deleting supplier");
                    }
            });

        });

});