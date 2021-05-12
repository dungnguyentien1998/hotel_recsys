import {api} from "@/api"


export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api list favorites
    listFavorites: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('favorites').then(res => {
            context.commit('listFavorites', res)
        })
    },
    // Api create favorite
    createFavorite: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.post(`hotels/${payload}/favorites`).then(res => {
            context.commit('createFavorite', res)
        })
    },
    // Api delete favorite
    deleteFavorite: (context, payload) => {
        let hotelId = payload.hotelId
        let favoriteId = payload.favoriteId
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.delete(`hotels/${hotelId}/favorites/${favoriteId}`).then(res => {
            context.commit('deleteFavorite', res)
        })
    },
    deleteFavoriteFromList: (context, payload) => {
        let favoriteId = payload.favoriteId
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.delete(`favorites/${favoriteId}`).then(res => {
            context.commit('deleteFavorite', res)
        })
    }
}
