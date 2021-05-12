export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    // Save favorite list
    listFavorites: (state, payload) => {
        state.favorites = payload.data.favorites
    },
    // Save new favorite
    createFavorite: (state, payload) => {
        if (payload.data.success) {
            state.favorites.push(payload.data.favorite)
        } else {
            state.status = 'FAILED'
        }
    },
    // Delete favorite from list
    deleteFavorite: (state, payload) => {
        if (payload.data.success) {
            let favorite = payload.data.favorite
            state.favorites = state.favorites.filter(item => item.uuid !== favorite.uuid)
        } else {
            state.status = 'FAILED'
        }
    }
}
