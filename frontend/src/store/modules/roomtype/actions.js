import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },

    listTypes: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}/types`).then(res => {
            context.commit('listTypes', res)
        })
    },

    createType: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        let form = formUtil(payload)
        return api.post(`hotels/${hotelId}/types`, form).then(res => {
            context.commit('createType', res)
        })
    },

    updateType: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        let typeId = payload.typeId
        delete payload.hotelId
        delete payload.typeId
        let form = formUtil(payload)
        return api.put(`hotels/${hotelId}/types/${typeId}`, form).then(res => {
            context.commit('updateType', res)
        })
    },

    deleteType: (context, payload) => {
        let hotelId = payload.hotelId
        let typeId = payload.typeId
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.delete(`hotels/${hotelId}/types/${typeId}`).then(res => {
            context.commit('deleteType', res)
        })
    }
}
