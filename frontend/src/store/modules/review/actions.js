import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api list reviews
    listReviews: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload.hotelId}/reviews`, {
            params: {
                page: payload.page
            }
        }).then(res => {
            context.commit('listReviews', res)
        })
    },
    // Api create review
    createReview: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let hotelId = payload.hotelId
        delete payload.hotelId
        let form = formUtil(payload)
        return api.post(`hotels/${hotelId}/reviews`, form).then(res => {
            context.commit('createReview', res)
        })
    },
}
