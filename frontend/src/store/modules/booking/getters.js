export default {
    // Booking status and list
    status: state => state.status,
    bookings: state => state.bookings,
    new_bookings: state => state.new_bookings,
    message: state => state.message,
    types: state => state.types,
    booking_rooms: state => state.booking_rooms,
    booking: state => state.booking,
    check_in: state => state.check_in,
    check_out: state => state.check_out,
    save: state => state.save,
    available_types: state => state.available_types,
    available_numbers: state => state.available_numbers,
    booking_id: state => state.booking_id,
    hotel_id: state => state.hotel_id,
}