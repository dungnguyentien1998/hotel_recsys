export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
        state.message = ''
    },
    // Save booking list
    listBookings: (state, payload) => {
        state.bookings = payload.data.bookings
    },
    listNewBookings: (state, payload) => {
        state.new_bookings = payload.data.bookings
    },
    // Save new booking
    createBooking: (state, payload) => {
        let success = payload.data.success
        if (success) {
            state.bookings.push(payload.data.booking)
            state.booking = payload.data.booking
            state.status = ''
        } else {
            state.status = 'FAILED'
            state.message = payload.data.detail
        }
    },
    // Delete booking from list
    deleteBooking: (state, payload) => {
        if (payload.data.success) {
            let booking = payload.data.booking
            state.bookings = state.bookings.filter(item => item.item !== booking.uuid)
        } else {
            state.status = 'FAILED'
        }
    },
    listTypes: (state, payload) => {
        state.types = payload.data.types
    },
    listBookingRooms: (state, payload) => {
        state.booking_rooms = payload.data.bookingRooms
    },
    arrangeRoom: (state, payload) => {
        let success = payload.data.success
        if (success) {
            state.status = ''
        } else {
            state.status = 'FAILED'
        }
    }
}
