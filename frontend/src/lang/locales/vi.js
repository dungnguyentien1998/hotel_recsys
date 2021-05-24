// Translate to vietnamese
export default {
    // Translate in navbar component
    button: {
        submit: 'Đồng ý',
        unsubmit: 'Hủy bỏ',
    },
    navbar: {
        languages: 'Ngôn ngữ',
        en: 'Tiếng Anh',
        vi: 'Tiếng Việt',
        profile: 'Tài khoản',
        logout: 'Đăng xuất',
        favorite: 'Danh sách ưa thích',
        booking: 'Danh sách đặt phòng',
        user: 'Quản lý tài khoản',
        hotel: 'Phê duyệt khách sạn',
        changePassword: 'Đổi mật khẩu'
    },
    // Translate for user object
    user: {
        login: {
            title: 'Đăng nhập',
            email: 'Email:',
            emailPlaceholder: 'Nhập email',
            password: 'Mật khẩu:',
            passwordPlaceholder: 'Nhập mật khẩu',
            token: 'Mã xác thực:',
            tokenPlaceholder: 'Nhập mã xác thực nhận từ email để đặt lại mật khẩu',
            oldPassword: 'Mật khẩu cũ:',
            oldPasswordPlaceholder: 'Nhập mật khẩu cũ',
            newPassword: 'Mật khẩu mới:',
            newPasswordPlaceholder: 'Nhập mật khẩu mới',
            forgotPassword: 'Quên mật khẩu',
            resetPassword: 'Đặt lại mật khẩu',
            submit: 'Đăng nhập',
            sendBtn: 'Xác nhận',
            register: 'Tạo tài khoản mới',
            showPassword: 'Hiện mật khẩu',
            errors: {
                title: 'Lỗi đăng nhập',
                invalidData: 'Email hoặc mật khẩu không chính xác',
                missing: 'Thiếu tài khoản hoặc mật khẩu',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình đăng nhập'
            }
        },
        forgot: {
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Dữ liệu không chính xác',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
            }
        },
        register: {
            activateAccount: 'Kích hoạt tài khoản',
            tokenPlaceholder: 'Nhập mã xác thực nhận từ email để kích hoạt tài khoản',
            title: 'Đăng ký',
            email: 'Email:',
            emailPlaceholder: 'Nhập email',
            password: 'Mật khẩu:',
            passwordPlaceholder: 'Nhập mật khẩu',
            confirmPassword: 'Xác nhận mật khẩu:',
            confirmPasswordPlaceholder: 'Xác nhận mật khẩu',
            name: 'Tên:',
            namePlaceholder: 'Nhập tên',
            tel: 'Số điện thoại:',
            telPlaceholder: 'Nhập số điện thoại',
            avatar: 'Ảnh đại diện:',
            imagePlaceholder: 'Chọn ảnh',
            imageDropPlaceholder: 'Kéo tệp vào đây',
            birthday: 'Ngày sinh:',
            birthdayPlaceholder: 'Chọn ngày sinh',
            city: 'Tỉnh/thành phố:',
            district: 'Quận/huyện:',
            ward: 'Xã/phường:',
            address: 'Địa chỉ:',
            addressPlaceholder: 'Nhập địa chỉ',
            role: 'Vai trò:',
            user: 'Người dùng',
            hotelier: 'Chủ khách sạn',
            admin: 'Quản trị viên',
            submit: 'Đăng ký',
            loginText: 'Đã có tài khoản?',
            loginLink: 'Đăng nhập',
            errors: {
                title: 'Lỗi đăng ký',
                invalidData: 'Sai định dạng email',
                email: 'Bạn phải điền email',
                name: 'Bạn phải điền tên',
                password: 'Bạn phải điền mật khẩu',
                passwordConfirm: 'Bạn phải xác nhận mật khẩu',
                passwordLength: 'Độ dài mật khẩu tối thiểu là 6',
                passwordSame: 'Mật khẩu và mật khẩu xác nhận khác nhau',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                emailUsed: 'Email đã được sử dụng',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình đăng ký'
            }
        },
        user: {
            title: 'Danh sách tài khoản',
            searchUser: 'Tìm tài khoản',
            search: 'Tìm',
            myProfile: 'Thông tin cá nhân',
            submit: 'Cập nhật thông tin',
            no: 'STT',
            created: 'Ngày tạo:',
            name: 'Họ tên',
            tel: 'SĐT',
            birthday: 'Ngày sinh',
            address: 'Địa chỉ',
            role: 'Vai trò',
            action: 'Khóa/Mở khóa',
            user: 'Người dùng',
            hotelier: 'Chủ khách sạn',
            admin: 'Quản trị viên',
            lock: 'Khóa',
            unlock: 'Mở khóa',
            view: 'Chi tiết',
            viewUser: 'Chi tiết người dùng',
            changePassword: 'Thay đổi mật khẩu',
            success: {
                title: 'Cập nhật thành công',
                message: 'Bạn đã cập nhật thông tin cá nhân',
                lockTitle: 'Khóa tài khoản thành công',
                unlockTitle: 'Mở khóa tài khoản thành công',
                lockMessage: 'Bạn đã khóa tài khoản thành công',
                unlockMessage: 'Bạn đã mở khóa tài khoản thành công',
                passwordTitle: 'Thành công',
                passwordMessage: 'Bạn đã đổi mật khẩu',
            },
            errors: {
                title: 'Cập nhật không thành công',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện',
                lockTitle: 'Không thể khóa tài khoản',
                unlockTitle: 'Không thể mở khóa tài khoản'
            }
        }
    },
    // Translate for hotel object
    hotel: {
        hotel: {
            ownerName: 'Chủ khách sạn: ',
            ownerTel: 'Điện thoại: ',
            ownerEmail: 'Email: ',
            title: 'Danh sách khách sạn',
            approveLabel: 'Danh sách khách sạn cần phê duyệt',
            searchHotel: 'Tìm khách sạn',
            advancedSearch: 'Tìm kiếm nâng cao',
            recommended: 'Gợi ý khách sạn cho bạn',
            recommendedLabel: 'Những khách sạn tương tự mà bạn có thể thích',
            rating: 'Đánh giá',
            createTitle: 'Tạo khách sạn',
            createBtn: 'Tạo khách sạn',
            city: 'Tỉnh/thành phố: ',
            district: 'Quận/huyện: ',
            address: 'Địa chỉ: ',
            room: 'phòng | phòng',
            review: 'đánh giá | đánh giá',
            complaint: 'khiếu nại | khiếu nại',
            amenities: 'Tiện nghi: ',
            updateBtn: 'Cập nhật',
            deleteBtn: 'Xóa',
            approveBtn: 'Phê duyệt',
            rejectBtn: 'Từ chối',
            searchBtn: 'Tìm',
            favoriteBtn: 'Lưu vào danh sách ưa thích',
            removeBtn: 'Loại khỏi danh sách ưa thích',
            discardBtn: 'Gỡ',
            updateTitle: 'Cập nhật khách sạn',
            deleteTitle: 'Xóa khách sạn',
            approveTitle: 'Phê duyệt khách sạn',
            rejectTitle: 'Từ chối yêu cầu',
            confirmDelete: 'Bạn có chắc chắn xóa khách sạn này?',
            confirmApprove: 'Bạn có muốn phê duyệt khách sạn này?',
            confirmReject: 'Bạn có muốn từ chối?',
            success: {
                approveTitle: 'Phê duyệt thành công',
                approveMessage: 'Bạn đã phê duyệt khách sạn này',
                rejectTitle: 'Từ chối thành công',
                rejectMessage: 'Bạn đã từ chối yêu cầu tạo khách sạn'
            },
            errors: {
                title: 'Xóa khách sạn không thành công',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện',
                approveTitle: 'Phê duyệt khách sạn không thành công',
                rejectTitle: 'Từ chối không thành công',
            }
        },
        hotelForm: {
            name: 'Tên:',
            namePlaceholder: 'Nhập tên khách sạn',
            star: 'Số sao:',
            city: 'Tỉnh/thành phố:',
            district: 'Quận/huyện:',
            ward: 'Xã/phường:',
            address: 'Địa chỉ:',
            addressPlaceholder: 'Nhập địa chỉ (Số ..., đường ...)',
            image: 'Ảnh:',
            imagePlaceholder: 'Chọn ảnh',
            imageDropPlaceholder: 'Kéo tệp vào đây',
            amenities: 'Tiện ích:',
            amenitiesPlaceholder: 'Chọn tiện ích',
            createBtn: 'Tạo',
            updateBtn: 'Cập nhật',
            success: {
                title: 'Gửi yêu cầu thành công',
                message: 'Bạn đã gửi yêu cầu tới quản trị viên',
                updateTitle: 'Cập nhật thành công',
                updateMessage: 'Bạn đã cập nhật thông tin khách sạn'
            },
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Thông tin không chính xác',
                createTitle: 'Lỗi tạo khách sạn',
                updateTitle: 'Lỗi cập nhật khách sạn',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện'
            }
        },
        hotelDetail: {
            title: 'Chi tiết khách sạn',
            rooms: 'Danh sách phòng',
            reviews: 'Các đánh giá',
            complaints: 'Khiếu nại',
            types: 'Kiểu phòng',
            createComplaint: 'Tạo khiếu nại',
            createReview: 'Tạo đánh giá',
            similarHotel: 'Khách sạn tương đồng',
            booking: 'Đặt phòng',
            bookings: 'Danh sách đặt phòng'
        }
    },
    booking: {
        booking: {
            title: 'Danh sách đặt phòng',
            detail: 'Chi tiết đặt phòng',
            newTitle: 'Danh sách đặt phòng mới',
            oldTitle: 'Những yêu cầu đặt phòng đã được xử lý',
            cancelBtn: 'Hủy',
            hotelName: 'Khách sạn',
            roomNumber: 'Số phòng',
            checkIn: 'Ngày nhận phòng',
            checkOut: 'Ngày trả phòng',
            address: 'Địa chỉ',
            price: 'Giá',
            code: 'Mã đặt phòng',
            totalPrice: 'Tổng tiền',
            userName: 'Khách hàng',
            userTel: 'Điện thoại',
            userEmail: 'Email',
            viewBtn: 'Chi tiết',
            cancelTitle: 'Huỷ đặt phòng',
            confirmDelete: 'Bạn có muốn hủy đặt phòng này?',
            description: 'Thanh toán khi nhận phòng',
            errors: {
                title: 'Thao tác không thành công',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện'
            }
        },
        bookingForm: {
            title: 'Sắp xếp phòng cho khách hàng',
            description: 'Số phòng khách hàng đặt',
            checkIn: 'Ngày nhận phòng:',
            checkOut: 'Ngày trả phòng:',
            roomType: 'Kiểu phòng',
            bookingNumber: 'Số lượng',
            submit: 'Gửi yêu cầu',
            checkInPlaceholder: 'Chọn ngày nhận',
            checkOutPlaceholder: 'Chọn ngày trả',
            capacity: 'Sức chứa',
            price: 'Giá phòng (VND)',
            amenities: 'Tiện nghi',
            available: 'Có thể đặt',
            rooms: 'Số lượng khách đặt',
            roomNumber: 'Lựa chọn phòng cho khách hàng',
            totalPrice: 'Tổng tiền',
            getAvailable: 'Xem phòng trống',
            success: {
                title: 'Đặt phòng thành công',
                message: 'Bạn đã đặt phòng cho khách sạn này',
            },
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Thông tin không chính xác',
                createTitle: 'Đặt phòng không thành công',
                timeAfter: 'Ngày trả phòng phải sau ngày nhận phòng',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                roomNumber: 'Bạn chưa chọn số lượng phòng',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình đặt phòng'
            }
        }
    },
    complaint: {
        complaint: {
            sendEmail: 'Gửi phản hồi',
        },
        complaintForm: {
            title: 'Tiêu đề:',
            content: 'Nội dung:',
            image: 'Ảnh:',
            titlePlaceHolder: 'Nhập tiêu đề',
            contentPlaceHolder: 'Nhập nội dung',
            submit: 'Gửi khiếu nại',
            success: {
                title: 'Gửi khiếu nại thành công',
                message: 'Bạn đã gửi khiếu nại đến khách sạn này',
            },
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Thông tin không chính xác',
                createTitle: 'Tạo khiếu nại không thành công',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình tạo khiếu nại'
            }
        }
    },
    favorite: {
        favorite: {
            title: 'Danh sách ưa thích',
            success: {
                saveTitle: 'Lưu thành công',
                saveMessage: 'Bạn đã lưu khách sạn vào danh sách ưa thích',
                removeTitle: 'Gỡ thành công',
                removeMessage: 'Bạn đã gỡ khách sạn khỏi danh sách ưa thích',
            },
            errors: {
                removeTitle: 'Gỡ không thành công',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện'
            }
        }
    },
    review: {
        review: {
            createBtn: 'Đánh giá',
            createTitle: 'Đánh giá khách sạn',
        },
        reviewForm: {
            title: 'Tiêu đề:',
            content: 'Nội dung:',
            titlePlaceholder: 'Nhập tiêu đề',
            contentPlaceholder: 'Nhập nội dung',
            rating: 'Đánh giá:',
            submitBtn: 'Gửi đánh giá',
            success: {
                title: 'Gửi đánh giá thành công',
                message: 'Bạn đã gửi đánh giá đến khách sạn này',
            },
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Thông tin không chính xác',
                createTitle: 'Tạo đánh giá không thành công',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình tạo đánh giá'
            }
        }
    },
    type: {
        type: {
            createBtn: 'Thêm kiểu phòng',
            updateBtn: 'Cập nhật',
            deleteBtn: 'Xóa',
            roomType: 'Kiểu phòng',
            capacity: 'Sức chứa',
            price: 'Giá phòng',
            createTitle: 'Tạo kiểu phòng',
            confirmDelete: 'Bạn có muốn xóa kiểu phòng này?',
            deleteTitle: 'Xóa kiểu phòng',
            errors: {
                title: 'Xóa kiểu phòng không thành công',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện'
            }
        },
        typeForm: {
            roomType: 'Kiểu phòng:',
            roomTypePlaceholder: 'Nhập kiểu phòng',
            capacity: 'Sức chứa:',
            capacityPlaceholder: 'Nhập sức chứa',
            price: 'Giá phòng (VND):',
            pricePlaceholder: 'Nhập giá phòng',
            amenities: 'Tiện nghi:',
            amenitiesPlaceholder: 'Nhập tiện nghi',
            createBtn: 'Tạo',
            updateBtn: 'Cập nhật',
            success: {
                title: 'Tạo kiểu phòng thành công',
                message: 'Bạn đã tạo kiểu phòng mới',
                updateTitle: 'Cập nhật thành công',
                updateMessage: 'Bạn đã cập nhật kiểu phòng thành công'
            },
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Thông tin không chính xác',
                createTitle: 'Tạo kiểu phòng không thành công',
                updateTitle: 'Cập nhật không thành công',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình cập nhật'
            }
        }
    },
    room: {
        room: {
            createBtn: 'Tạo phòng',
            bookBtn: 'Đặt phòng',
            capacity: 'Sức chứa',
            minCapacity: 'Sức chứa tối thiểu:',
            capacityPlaceholder: 'Nhập sức chứa',
            minPrice: 'Giá tối thiểu (VND):',
            maxPrice: 'Giá tối đa (VND):',
            roomType: 'Kiểu phòng:',
            searchBtn: 'Tìm',
            updateBtn: 'Cập nhật',
            deleteBtn: 'Xóa',
            confirmDelete: 'Bạn có muốn xóa phòng này?',
            roomDetail: 'Chi tiết phòng',
            roomNumber: 'Số phòng',
            booked: 'Số lượng đã đặt',
            price: 'Giá phòng',
            amenities: 'Tiện nghi',
            bookings: 'Danh sách đặt phòng',
            bookingRoom: 'Đặt phòng',
            userName: 'Tên',
            checkInTime: 'Ngày nhận',
            checkOutTime: 'Ngày trả',
            updateTitle: 'Cập nhật phòng',
            deleteTitle: 'Xóa phòng',
            errors: {
                title: 'Xóa phòng không thành công',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện'
            }
        },
        roomForm: {
            roomType: 'Kiểu phòng:',
            roomNumber: 'Số phòng:',
            roomNumberPlaceholder: 'Nhập số phòng',
            roomNumbers: 'Danh sách số phòng:',
            roomNumbersPlaceholder: 'Nhập danh sách số phòng',
            image: 'Ảnh:',
            images: 'Ảnh phòng',
            createBtn: 'Tạo',
            updateBtn: 'Cập nhật',
            success: {
                title: 'Tạo phòng thành công',
                message: 'Bạn đã tạo phòng mới',
                updateTitle: 'Cập nhật thành công',
                updateMessage: 'Bạn đã cập nhật phòng thành công'
            },
            errors: {
                title: 'Thao tác không thành công',
                invalidData: 'Thông tin không chính xác',
                createTitle: 'Tạo phòng không thành công',
                updateTitle: 'Cập nhật không thành công',
                missing: 'Bạn phải điền đủ các thông tin bắt buộc',
                exceptionOccurred: 'Có lỗi xảy ra trong quá trình thực hiện'
            }
        }
    }
}