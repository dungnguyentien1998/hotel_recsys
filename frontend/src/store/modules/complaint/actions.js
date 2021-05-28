import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api list complaints
    listComplaints: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}/complaints`).then(res => {
            context.commit('listComplaints', res)
        })
    },
    // Api create complaint
    createComplaint: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        let form = formUtil(payload)
        return api.post(`hotels/${hotelId}/complaints`, form).then(res => {
            context.commit('createComplaint', res)
        })
    },
    updateComplaint: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        let complaintId = payload.complaintId
        delete payload.hotelId
        delete payload.complaintId
        let form = formUtil(payload)
        return api.put(`hotels/${hotelId}/complaints/${complaintId}`, form).then(res => {
            context.commit('updateComplaint', res)
        })
    },
}
