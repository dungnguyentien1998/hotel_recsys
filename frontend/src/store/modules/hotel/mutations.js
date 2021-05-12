export default {
    // Change status
    // submit: state => {
    //     state.status = 'SUBMIT'
    // },
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    // Save hotel list
    listHotels: (state, payload) => {
        state.hotels = payload.data.hotels
    },
    // Save new hotel
    createHotel: (state, payload) => {
        if (payload.data.success) {
            state.hotels.push(payload.data.hotel)
        } else {
            state.status = 'FAILED'
        }
    },
    // Save updated hotel
    updateHotel: (state, payload) => {
        if (payload.data.success) {
            let hotel = payload.data.hotel
            let index = state.hotels.findIndex(item => item.uuid === hotel.uuid)
            state.hotels = [
                ...state.hotels.slice(0, index),
                hotel,
                ...state.hotels.slice(index + 1)
            ]
        } else {
            state.status = 'FAILED'
        }
    },
    // Delete hotel from list
    deleteHotel: (state, payload) => {
        if (payload.data.success) {
            let hotel = payload.data.hotel
            state.hotels = state.hotels.filter(item => item.item !== hotel.uuid)
        } else {
            state.status = 'FAILED'
        }
    }
}
