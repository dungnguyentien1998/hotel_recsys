import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    // Reset state status
    resetStatus: context => {
        context.commit('resetStatus');
    },
    newListBookings: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('bookings').then(res => {
            context.commit('listBookings', res)
        })
    },
    newCreateBooking: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let form = formUtil(payload)
        return api.post('bookings', form)
            .then(res => {
                context.commit('createBooking', res)
            })
    },
    newDeleteBooking: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.delete(`bookings/${payload}`).then(res => {
            // context.commit('deleteBooking', res)
        })
    },
    newListBookingsHotelier: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload.hotelId}/bookings`, {
            params: {
                page: payload.page,
                user_name: payload.user_name,
                user_tel: payload.user_tel,
                user_email: payload.user_email,
                code: payload.code,
                is_processed: payload.is_processed
            }
        }).then(res => {
            context.commit('listBookings', res)
        })
    },
    listNewBookings: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}/new_bookings`).then(res => {
            context.commit('listNewBookings', res)
        })
    },
    newDeleteBookingHotelier: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        let bookingId = payload.bookingId
        // let form = formUtil(payload)
        return api.delete(`hotels/${hotelId}/bookings/${bookingId}`).then(res => {
            // context.commit('deleteBooking', res)
        })
    },
    listTypes: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        let bookingId = payload.bookingId
        return api.get(`hotels/${hotelId}/bookings/${bookingId}`).then(res => {
            context.commit('listTypes', res)
        })
    },
    listBookingRooms: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        // let bookingId = payload.bookingId
        return api.get(`hotels/${hotelId}/arrange_room`, {
            params: {
                bookingId: payload.bookingId
            }
        }).then(res => {
            context.commit('listBookingRooms', res)
        })
    },
    arrangeRoom: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        let form = formUtil(payload)
        return api.post(`hotels/${hotelId}/arrange_room`, form)
            .then(res => {
                context.commit('arrangeRoom', res)
            })
    },
}