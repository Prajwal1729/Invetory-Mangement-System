$(document).ready(function () {

    // Add Category

    // Add Category

$('#categoryForm').submit(function (e) {

    e.preventDefault();

    $('.text-danger').text('');
    $('#categoryMessage').html('');

    let name =
        $('[name="name"]').val().trim();

    let description =
        $('[name="description"]').val().trim();

   let status =
    $('#categoryForm select[name="status"]').val();

    let isValid = true;

    // Name Validation

    if (name === '') {

        $('#nameError').text(
            'Category name is required'
        );

        isValid = false;
    }

    // Description Validation

    if (description === '') {

        $('#descriptionError').text(
            'Description is required'
        );

        isValid = false;
    }

    // Status Validation

  $('#statusError').text('');

    if (status === '') {

        $('#statusError').text(
            'Please select status'
        );

        isValid = false;
    }

    if (!isValid) {
        return;
    }

    $.ajax({

        url: '/categories/add/',
        type: 'POST',

        data: $(this).serialize(),

        success: function (response) {

            if (response.status === 'success') {

                $('#categoryMessage').html(`
                    <div class="alert alert-success">
                        ${response.message}
                    </div>
                `);

                $('#categoryForm')[0].reset();

                setTimeout(() => {
                    location.reload();
                }, 1000);

            } else {

                $('#categoryMessage').html(`
                    <div class="alert alert-danger">
                        Failed to add category
                    </div>
                `);
            }
        },

        error: function () {

            $('#categoryMessage').html(`
                <div class="alert alert-danger">
                    Server Error
                </div>
            `);
        }
    });
});


    // Open Edit Modal

    $('.editCategoryBtn').click(function () {

        $('#edit_category_id').val(
            $(this).data('id')
        );

        $('#edit_name').val(
            $(this).data('name')
        );

        $('#edit_description').val(
            $(this).data('description')
        );

        $('#edit_status').val(
            $(this).data('status')
        );

        $('#editCategoryModal').modal('show');
    });


    // Update Category

    $('#editCategoryForm').submit(function (e) {

        e.preventDefault();

        let categoryId =
            $('#edit_category_id').val();

        $.ajax({

            url: `/categories/update/${categoryId}/`,
            type: 'POST',
            data: $(this).serialize(),

            success: function (response) {

                if (response.status === 'success') {

                    $('#editCategoryMessage').html(`
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


    // Delete Category

    $('.deleteCategoryBtn').click(function () {

        let categoryId =
            $(this).data('id');

        $.ajax({

            url: `/categories/delete/${categoryId}/`,
            type: 'POST',

            data: {
                csrfmiddlewaretoken:
                    $('[name=csrfmiddlewaretoken]').val()
            },

            success: function (response) {

                if (response.status === 'success') {

                    location.reload();
                }
            }
        });
    });

});