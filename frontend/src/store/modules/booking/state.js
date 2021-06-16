export default {
    // Booking status and list
    status: '',
    bookings: [],
    // Show bookings which are not assigned
    new_bookings: [],
    message: '',
    // Show all room types of hotel, use in BookingDetailHotelier
    types: [],
    // Show bookings which are assigned
    booking_rooms: [],
    // Show current booking form
    booking: {},
    // Data for BookingForm
    check_in: null,
    check_out: null,
    save: null,
    available_types: [],
    available_numbers: [],
    hotel_id: '',
    // Show current booking, use in BookingHotelier and BookingHotelierDetail
    booking_id: '',
    page: 1,
    user_name: null,
    user_tel: null,
    user_email: null,
    code: null,
    is_processed: null,
    is_search: false,
    count: 0,
    uuids: []
}