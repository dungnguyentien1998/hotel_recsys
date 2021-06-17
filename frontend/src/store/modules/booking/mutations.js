export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
        state.message = ''
    },

    listBookings: (state, payload) => {
        let success = payload.data.success
        if (success) {
            state.bookings = payload.data.bookings
            state.count = payload.data.count
        }
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
    saveNewBooking: (state, payload) => {
        if (payload.success) {
            state.new_bookings.push(payload.booking)
        } else {
            state.status = 'FAILED'
        }
    },
    saveBooking: (state, payload) => {
        if (payload.success) {
            state.bookings.push(payload.booking)
        } else {
            state.status = 'FAILED'
        }
    },

    deleteBooking: (state, payload) => {
        if (payload.data.success) {
            let booking = payload.data.booking
            state.bookings = state.bookings.filter(item => item.item !== booking.uuid)
        } else {
            state.status = 'FAILED'
        }
    },
    listTypes: (state, payload) => {
        let success = payload.data.success
        if (success) {
            state.types = payload.data.types
        } else {
            state.types = []
        }
    },
    listBookingRooms: (state, payload) => {
        let success = payload.data.success
        if (success) {
            state.booking_rooms = payload.data.bookingRooms
        }
    },
    arrangeRoom: (state, payload) => {
        let success = payload.data.success
        if (success) {
            state.status = ''
        } else {
            state.status = 'FAILED'
        }
    },
    setCheckIn: (state, payload) => {
        state.check_in = payload
    },
    setCheckOut: (state, payload) => {
        state.check_out = payload
    },
    setSave: (state, payload) => {
        state.save = payload
    },
    resetSave: state => {
        state.save = null
    },
    setAvailableTypes: (state, payload) => {
        state.available_types.push(payload)
    },
    setAvailableNumbers: (state, payload) => {
        state.available_numbers.push(payload)
    },
    clearAvailableTypes: state => {
        state.available_types = []
    },
    clearAvailableNumbers: state => {
        state.available_numbers = []
    },
    setBookingId: (state, payload) => {
        state.booking_id = payload
    },
    setHotelId: (state, payload) => {
        state.hotel_id = payload
    },
    setPage: (state, payload) => {
        state.page = payload
    },
    setIsSearch: (state, payload) => {
        state.is_search = payload
    },
    setUserName: (state, payload) => {
        state.user_name = payload
    },
    setUserTel: (state, payload) => {
        state.user_tel = payload
    },
    setUserEmail: (state, payload) => {
        state.user_email = payload
    },
    setCode: (state, payload) => {
        state.code = payload
    },
    setIsProcessed: (state, payload) => {
        state.is_processed = payload
    },
    listUuids: (state, payload) => {
        state.uuids = payload.data.uuids
    },
    saveUuid: (state, payload) => {
        state.uuids.unshift(payload)
    },
}
