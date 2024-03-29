// Translate to english
export default {
    // Translate in navbar component
    button: {
        submit: 'Submit',
        unsubmit: 'Cancel',
    },
    navbar: {
        languages: 'Languages',
        en: 'English',
        vi: 'Vietnamese',
        profile: 'Profile',
        logout: 'Logout',
        favorite: 'Favorite list',
        booking: 'Booking list',
        user: 'Manage user',
        hotel: 'Approve hotel',
        changePassword: 'Change password',
        reply: 'Replies from hotels',
        notification: 'Approval results'
    },
    payment: {
        success: 'Thanks for booking!',
        cancel: 'Your payment was cancelled.',
        back: 'Back to booking page'
    },
    // Translate for user object
    user: {
        login: {
            title: 'Login',
            email: 'Email:',
            emailPlaceholder: 'Enter email',
            password: 'Password:',
            passwordPlaceholder: 'Enter password',
            token: 'Token:',
            tokenPlaceholder: 'Enter token from email to reset password',
            oldPassword: 'Old password:',
            oldPasswordPlaceholder: 'Enter old password',
            newPassword: 'New password:',
            newPasswordPlaceholder: 'Enter new password',
            forgotPassword: 'Forgot password',
            resetPassword: 'Reset password',
            submit: 'Login',
            sendBtn: 'Submit',
            register: 'Create new account',
            showPassword: 'Show password',
            errors: {
                title: 'Login failed',
                invalidData: 'Incorrect email or password',
                missing: 'Missing email or password',
                exceptionOccurred: 'An exception occurred',
                lock: 'Your account has been locked'
            }
        },
        forgot: {
            errors: {
                title: 'Failed',
                invalidData: 'Invalid data',
                exceptionOccurred: 'An exception occurred',
                missing: 'You must fill all required information',
            }
        },
        register: {
            noInfo: 'No information',
            activateAccount: 'Activate account',
            tokenPlaceholder: 'Enter token from email to activate account',
            title: 'Register',
            email: 'Email:',
            emailPlaceholder: 'Enter email',
            password: 'Password:',
            passwordPlaceholder: 'Enter password',
            confirmPassword: 'Confirm password:',
            confirmPasswordPlaceholder: 'Enter confirm password',
            name: 'Name:',
            namePlaceholder: 'Enter name',
            tel: 'Telephone number:',
            telPlaceholder: 'Enter telephone number',
            avatar: 'Avatar:',
            imagePlaceholder: 'Choose a file',
            imageDropPlaceholder: 'Drop file here',
            birthday: 'Birthday:',
            birthdayPlaceholder: 'Select birthday',
            city: 'City:',
            district: 'District:',
            ward: 'Ward:',
            address: 'Address:',
            addressPlaceholder: 'Enter address (No and street)',
            role: 'Role:',
            user: 'User',
            hotelier: 'Hotelier',
            admin: 'Admin',
            submit: 'Register',
            loginText: 'Already have an account?',
            loginLink: 'Login',
            success: {
                title: 'Action success',
                message: 'Token has been sent to your email',
                registerMessage: 'You have activated your account'
            },
            errors: {
                title: 'Register failed',
                invalidData: 'Invalid email format',
                email: 'You have to fill email',
                name: 'You have to fill name',
                tel: 'You have to fill telephone number',
                password: 'You have to fill password',
                passwordConfirm: 'You have to fill password confirm',
                passwordLength: 'Password minimum length is 6',
                passwordSame: 'Password and password are not similar',
                missing: 'You must fill all required information',
                emailUsed: 'Email has been used',
                exceptionOccurred: 'An exception occurred'
            }
        },
        user: {
            noResult: 'No matching user found',
            noUser: 'User list is empty',
            title: 'List user',
            searchUser: 'Search user',
            search: 'Search',
            myProfile: 'My profile',
            submit: 'Update profile',
            no: 'No',
            created: 'Created:',
            name: 'Name',
            tel: 'Tel',
            birthday: 'Birthday',
            address: 'Address',
            role: 'Role',
            action: 'Action',
            user: 'User',
            hotelier: 'Hotelier',
            admin: 'Admin',
            lock: 'Lock',
            unlock: 'Unlock',
            lockTitle: 'Lock account',
            reason: 'Reason to lock this account',
            view: 'View',
            viewUser: 'User detail',
            changePassword: 'Change password',
            success: {
                title: 'Update profile success',
                message: 'You have changed your profile',
                lockTitle: 'Lock user success',
                unlockTitle: 'Unlock user success',
                lockMessage: 'You have locked user',
                unlockMessage: 'You have unlock user',
                passwordTitle: 'Change password success',
                passwordMessage: 'You have changed your password',
            },
            errors: {
                search: '',
                title: 'Update profile failed',
                missing: 'You must fill all required information',
                exceptionOccurred: 'An exception occurred',
                lockTitle: 'Cannot lock user',
                unlockTitle: 'Cannot unlock user'
            }
        }
    },
    // Translate for hotel object
    hotel: {
        hotel: {
            myHotel: 'My hotels',
            noResult: 'No matching hotel found',
            noHotel: 'You have no hotel',
            name: 'Hotel name',
            submit: 'Submit',
            ownerName: 'Owner: ',
            contact: 'Hotel contact: ',
            ownerTel: 'Tel: ',
            ownerEmail: 'Email: ',
            title: 'Hotel list',
            approveLabel: 'List of hotels to approve',
            approveChoice: 'Approve or reject this request',
            reason: 'Description (Reason if you reject this request)',
            searchHotel: 'Search hotel',
            advancedSearch: 'Advanced search',
            recommended: 'Recommended hotels for you',
            recommendedLabel: 'Similar hotels that you may like',
            status: 'Status',
            approveStatus: 'Approved',
            rejectStatus: 'Denied',
            reasonTitle: 'Reason',
            notificationTitle: 'Notifications about hotels creation request',
            rating: 'Rating',
            createTitle: 'Create new hotel',
            createBtn: 'Create new hotel',
            city: 'City: ',
            district: 'District: ',
            address: 'Address: ',
            room: 'room | rooms',
            review: 'review | reviews',
            complaint: 'complaint | complaints',
            new_bookings: 'new booking | new bookings',
            amenities: 'Amenities: ',
            updateBtn: 'Update',
            deleteBtn: 'Delete',
            approveBtn: 'Approve',
            rejectBtn: 'Reject',
            searchBtn: 'Search',
            favoriteBtn: 'Save to favorites',
            removeBtn: 'Remove from favorites',
            discardBtn: 'Discard',
            updateTitle: 'Update hotel',
            deleteTitle: 'Delete hotel',
            approveTitle: 'Approve hotel',
            rejectTitle: 'Reject hotel',
            confirmDelete: 'Are you sure to delete this hotel?',
            confirmApprove: 'Do you want to approve this form?',
            confirmReject: 'Do you want to reject this form?',
            success: {
                approveTitle: 'Approve success',
                approveMessage: 'You have approved this hotel',
                rejectTitle: 'Reject success',
                rejectMessage: 'You have reject this request'
            },
            errors: {
                search: '',
                title: 'Delete hotel failed',
                exceptionOccurred: 'An exception occurred',
                approveTitle: 'Approve hotel failed',
                rejectTitle: 'Reject hotel failed',
            }
        },
        hotelForm: {
            name: 'Hotel name:',
            namePlaceholder: 'Enter hotel name',
            star: 'Star:',
            city: 'City:',
            district: 'District:',
            ward: 'Ward:',
            address: 'Address:',
            addressPlaceholder: 'Enter address (No and street)',
            image: 'Hotel image:',
            imagePlaceholder: 'Choose a file',
            imageDropPlaceholder: 'Drop file here',
            amenities: 'Amenities:',
            amenitiesPlaceholder: 'Select amenities',
            email: 'Email:',
            emailPlaceholder: 'Enter email',
            tel: 'Tel number:',
            telPlaceholder: 'Enter telephone number',
            createBtn: 'Create',
            updateBtn: 'Update',
            success: {
                title: 'Request success',
                message: 'You have sent request to admin',
                updateTitle: 'Update success',
                updateMessage: 'You have updated hotel info'
            },
            errors: {
                title: 'Action failed',
                invalidData: 'Invalid data',
                createTitle: 'Create hotel failed',
                updateTitle: 'Update hotel failed',
                missing: 'You must fill all required information',
                exceptionOccurred: 'An exception occurred',
                reasonMissing: 'You must fill reject reason'
            }
        },
        hotelDetail: {
            title: 'Hotel detail',
            rooms: 'Rooms list',
            reviews: 'Reviews list',
            complaints: 'Complaints list',
            types: 'Room types',
            createComplaint: 'Create complaint',
            createReview: 'Create review',
            similarHotel: 'Similar hotels',
            booking: 'Booking',
            bookings: 'Bookings list'
        }
    },
    booking: {
        booking: {
            search: 'Search booking',
            customerName: 'Customer name: ',
            customerTel: 'Telephone number: ',
            customerEmail: 'Customer email: ',
            bookingCode: 'Booking code: ',
            customerNamePlaceholder: 'Enter customer name',
            customerTelPlaceholder: 'Enter customer telephone number',
            customerEmailPlaceholder: 'Enter customer email',
            bookingCodePlaceholder: 'Enter booking code',
            status: 'Booking status ',
            processed: 'Processed',
            notProcess: 'New',
            isArranged: 'You have assigned rooms for this booking',
            noResult: 'You have no booking',
            noBooking: 'Booking list is empty',
            noResultSearch: 'No matching booking found',
            title: 'Booking list',
            detail: 'Booking detail',
            newTitle: 'New bookings',
            oldTitle: 'Bookings that were arranged',
            cancelBtn: 'Cancel',
            hotelName: 'Hotel',
            roomNumber: 'Room number',
            checkIn: 'Check in date',
            checkOut: 'Check out date',
            address: 'Address',
            price: 'Price',
            code: 'Booking code',
            totalPrice: 'Total price',
            userName: 'Customer',
            userTel: 'Telephone',
            userEmail: 'Email',
            viewBtn: 'View',
            cancelTitle: 'Cancel booking',
            confirmDelete: 'Are you sure to cancel this booking?',
            description: 'Pay when check-in',
            success: {
                message: 'You have assigned for this booking',
                title: 'Action success',
                deleteMessage: 'You have canceled this booking',
                deleteTitle: 'Action success'
            },
            errors: {
                title: 'Action failed',
                exceptionOccurred: 'An exception occurred',
                search: ''
            }
        },
        bookingForm: {
            title: 'Select rooms for user booking',
            description: 'Number of rooms to select',
            checkIn: 'Check in date:',
            checkOut: 'Check out date:',
            roomType: 'Room type',
            bookingNumber: 'Number of rooms',
            submit: 'Submit',
            checkInPlaceholder: 'Select check in date',
            checkOutPlaceholder: 'Select check out date',
            capacity: 'Capacity',
            adult: 'Adult',
            children: 'Children',
            area: 'Area',
            price: 'Price (VND)',
            amenities: 'Amenities',
            available: 'Available',
            rooms: 'Booking amount',
            viewImage: 'View image',
            hotelierRooms: 'Booking amount',
            roomNumber: 'Arrange rooms for customer',
            room: 'Room',
            totalPrice: 'Total price',
            getAvailable: 'Get available',
            success: {
                title: 'Booking success',
                message: 'You have made booking for this hotel',
            },
            errors: {
                title: 'Action failed',
                invalidData: 'Invalid data',
                createTitle: 'Booking failed',
                timeAfter: 'Check out time must be after',
                missing: 'You must fill all required information',
                roomNumber: 'You have to choose number of rooms',
                exceptionOccurred: 'An exception occurred'
            }
        }
    },
    complaint: {
        complaint: {
            sendEmail: 'Send email',
            status: 'This complaint have been processed',
            noResult: 'No matching complaint found',
            noComplaint: 'Complaint list is empty',
        },
        complaintForm: {
            title: 'Title:',
            content: 'Content:',
            image: 'Image:',
            titlePlaceHolder: 'Enter title',
            contentPlaceHolder: 'Enter content',
            submit: 'Submit',
            success: {
                title: 'Create complaint success',
                message: 'You have sent complaint to this hotel',
            },
            errors: {
                title: 'Action failed',
                invalidData: 'Invalid data',
                createTitle: 'Create complaint failed',
                missing: 'You must fill all required information',
                exceptionOccurred: 'An exception occurred'
            }
        }
    },
    reply: {
        reply: {
            title: 'Replies from hotels that you have complainted',
            view: 'View reply',
            sendReply: 'Send reply',
            createTitle: 'Send reply'
        },
        replyDetail: {
            title: 'Reply from hotel ',
            contact: 'Contact'
        }
    },
    favorite: {
        favorite: {
            title: 'Favorite list',
            noResult: 'Favorite list is empty',
            success: {
                saveTitle: 'Save to favorite list success',
                saveMessage: 'You have saved this hotel to your favorite list',
                removeTitle: 'Remove from favorite list success',
                removeMessage: 'You have removed this hotel from your favorite list',
            },
            errors: {
                removeTitle: 'Remove from favorite list failed',
                exceptionOccurred: 'An exception occurred'
            }
        }
    },
    review: {
        review: {
            createBtn: 'Review',
            createTitle: 'Review this hotel',
            noResult: 'No matching review found',
            noReview: 'Review list is empty',
        },
        reviewForm: {
            title: 'Title:',
            content: 'Content:',
            titlePlaceholder: 'Enter title',
            contentPlaceholder: 'Enter content',
            rating: 'Rating:',
            submitBtn: 'Submit',
            success: {
                title: 'Create review success',
                message: 'You have created review for this hotel',
            },
            errors: {
                title: 'Action failed',
                invalidData: 'Invalid data',
                createTitle: 'Create review failed',
                missing: 'You must fill all required information',
                exceptionOccurred: 'An exception occurred'
            }
        }
    },
    type: {
        type: {
            noResult: 'No matching type found',
            noType: 'Type list is empty',
            createBtn: 'Create room type',
            updateBtn: 'Update',
            deleteBtn: 'Delete',
            roomType: 'Room type',
            capacity: 'Capacity',
            adultNumber: 'Number of adult',
            childrenNumber: 'Number of children',
            price: 'Price',
            area: 'Area',
            createTitle: 'Create new room type',
            confirmDelete: 'Are you sure to delete this room type?',
            deleteTitle: 'Delete room type',
            errors: {
                title: 'Delete failed',
                exceptionOccurred: 'An exception occurred'
            }
        },
        typeForm: {
            roomType: 'Room type:',
            roomTypePlaceholder: 'Enter room type',
            capacity: 'Capacity:',
            capacityPlaceholder: 'Enter room capacity',
            adult: 'Number of adult:',
            adultPlaceholder: 'Enter number of adult:',
            children: 'Number of children:',
            childrenPlaceholder: 'Enter number of children:',
            price: 'Price (VND):',
            pricePlaceholder: 'Enter room price',
            area: 'Area (㎡):',
            areaPlaceholder: 'Enter area',
            amenities: 'Amenities:',
            amenitiesPlaceholder: 'Select amenities',
            createBtn: 'Create',
            updateBtn: 'Update',
            success: {
                title: 'Create success',
                message: 'You have created new room type',
                updateTitle: 'Update success',
                updateMessage: 'You have updated this room type'
            },
            errors: {
                title: 'Action failed',
                invalidData: 'Wrong data type',
                createTitle: 'Create room type failed',
                updateTitle: 'Update room type failed',
                missing: 'You must fill all required information',
                exceptionOccurred: 'An exception occurred'
            }
        }
    },
    room: {
        room: {
            noResult: 'No matching room found',
            noRoom: 'Room list is empty',
            createBtn: 'Create new room',
            bookBtn: 'Booking',
            capacity: 'Capacity',
            adultNumber: 'Number of adults',
            childrenNumber: 'Number of children',
            area: 'Area',
            minCapacity: 'Minimum capacity:',
            capacityPlaceholder: 'Enter capacity',
            minPrice: 'Min price (VND):',
            maxPrice: 'Max price (VND):',
            roomType: 'Room type: ',
            searchBtn: 'Search',
            updateBtn: 'Update',
            deleteBtn: 'Delete',
            confirmDelete: 'Are you sure to delete this room?',
            roomDetail: 'Room detail',
            roomNumber: 'Room number',
            booked: 'Booked',
            price: 'Price',
            amenities: 'Amenities',
            bookings: 'Bookings',
            bookingRoom: 'Booking room',
            userName: 'Name',
            checkInTime: 'Check in date',
            checkOutTime: 'Check out date',
            updateTitle: 'Update room',
            deleteTitle: 'Delete room',
            errors: {
                title: 'Delete failed',
                exceptionOccurred: 'An exception occurred',
                search: ''
            }
        },
        roomForm: {
            roomType: 'Room type:',
            roomNumber: 'Room number:',
            roomNumberPlaceholder: 'Enter room number',
            roomNumbers: 'Add room numbers:',
            roomNumbersPlaceholder: 'Enter room number list',
            image: 'Image:',
            images: 'Image for room',
            createBtn: 'Create',
            updateBtn: 'Update',
            success: {
                title: 'Create success',
                message: 'You have created new rooms',
                updateTitle: 'Update success',
                updateMessage: 'You have updated this room'
            },
            errors: {
                title: 'Action failed',
                invalidData: 'Wrong data type for room number',
                createTitle: 'Create room failed',
                updateTitle: 'Update room failed',
                missing: 'You must fill all required information',
                image: 'Room image is missing',
                exceptionOccurred: 'An exception occurred',
                duplicate: 'Duplicate room numbers'
            }
        }
    }
}