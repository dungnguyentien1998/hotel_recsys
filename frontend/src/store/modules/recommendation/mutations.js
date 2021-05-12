export default {
    // Save recommendation list
    listRecommendations: (state, payload) => {
        state.recommendations = payload.data.recommendations
    },
    // Save recommendation list
    listRecommendationsLogin: (state, payload) => {
        state.recommendationsLogin = payload.data.recommendationsLogin
    }
}
