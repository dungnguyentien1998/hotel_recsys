import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    // Reset state status
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api list bookings for user
    listBookings: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('bookings').then(res => {
            context.commit('listBookings', res)
        })
    },
    // Api create booking
    createBooking: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let form = formUtil(payload)
        return api.post('bookings', form)
            .then(res => {
                context.commit('createBooking', res)
            })
    },
    // Api delete booking
    // deleteBooking: (context, payload) => {
    //     api.defaults.headers.common.Authorization = localStorage.getItem('token');
    //     return api.delete(`bookings/${payload}`).then(res => {
    //         context.commit('deleteBooking', res)
    //     })
    // }
    // Api delete multiple bookings for user
    deleteBooking: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        // let form = formUtil(payload)
        return api.delete('bookings', {data: payload}).then(res => {
            // context.commit('deleteBooking', res)
        })
    },
    // Api list bookings for hotelier
    listBookingsHotelier: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}/bookings`).then(res => {
            context.commit('listBookings', res)
        })
    },
    deleteBookingHotelier: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        // let form = formUtil(payload)
        return api.delete(`hotels/${hotelId}/bookings`, {data: payload}).then(res => {
            // context.commit('deleteBooking', res)
        })
    },
}