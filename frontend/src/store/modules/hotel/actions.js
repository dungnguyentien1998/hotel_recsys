import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    // Reset state status
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api list hotels
    listHotels: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('hotels', {
            params : {
                page: payload.page,
                name: payload.name,
                city: payload.city,
                district: payload.district,
                ward: payload.ward,
                star: payload.star
            }
        }).then(res => {
            context.commit('listHotels', res)
        })
    },
    getHotel: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}`).then(res => {
            context.commit('getHotel', res)
        })
    },
    // Api create hotel
    createHotel: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let form = formUtil(payload)
        return api.post('hotels', form).then(res => {
            context.commit('createHotel', res)
        })
    },
    // Api update booking
    updateHotel: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let uuid = payload.uuid
        delete payload.uuid
        if (payload.image == null){
            delete payload.image
        }
        let form = formUtil(payload)
        return api.put(`hotels/${uuid}`, form).then(res => {
            context.commit('updateHotel', res)
        })
    },
    // Api delete booking
    deleteHotel: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.delete(`hotels/${payload}`).then(res => {
            context.commit('deleteHotel', res)
        })
    },
    approveHotel: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        let uuid = payload.uuid
        delete payload.uuid
        let form = formUtil(payload)
        return api.put(`admin/hotels/${uuid}`, form).then(res => {
            context.commit('updateHotel', res)
        })
    },
    rejectHotel: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        let uuid = payload.uuid
        delete payload.uuid
        let form = formUtil(payload)
        return api.put(`admin/hotels/${uuid}`, form).then(res => {
            context.commit('updateHotel', res)
        })
    },
    notifyHotels: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('notifications/hotels').then(res => {
            context.commit('notifyHotels', res)
        })
    },
    listNames: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('hotels/name').then(res => {
            context.commit('listNames', res)
        })
    },
    listUuids: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('hotels/uuid').then(res => {
            context.commit('listUuids', res)
        })
    },
}
