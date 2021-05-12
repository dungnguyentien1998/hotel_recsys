import {api} from "@/api"


export default {
    // Api list recommendations
    listRecommendations: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get(`hotels/${payload}/recommendations`).then(res => {
            context.commit('listRecommendations', res)
        })
    },
    // Api list recommendations
    listRecommendationsLogin: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('recommendations').then(res => {
            context.commit('listRecommendationsLogin', res)
        })
    }
}