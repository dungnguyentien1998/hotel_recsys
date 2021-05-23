import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api list rooms
    listRooms: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}/rooms`).then(res => {
            context.commit('listRooms', res)
        })
    },
    // Api create room
    createRoom: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        delete payload.room_number
        delete payload.image
        let form = formUtil(payload)
        return api.post(`hotels/${hotelId}/rooms`, form).then(res => {
            context.commit('createRoom', res)
        })
    },
    // Api update room
    updateRoom: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        let roomId = payload.roomId
        delete payload.hotelId
        delete payload.roomId
        delete payload.room_numbers
        delete payload.images
        if (payload.image == null){
            delete payload.image
        }
        let form = formUtil(payload)
        return api.put(`hotels/${hotelId}/rooms/${roomId}`, form).then(res => {
            context.commit('updateRoom', res)
        })
    },
    // Api delete room
    deleteRoom: (context, payload) => {
        let hotelId = payload.hotelId
        let roomId = payload.roomId
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.delete(`hotels/${hotelId}/rooms/${roomId}`).then(res => {
            context.commit('deleteRoom', res)
        })
    }
}
