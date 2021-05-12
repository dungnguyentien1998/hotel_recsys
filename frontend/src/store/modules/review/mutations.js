export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    // Save review list
    listReviews: (state, payload) => {
        state.reviews = payload.data.reviews
    },
    // Save new review
    createReview: (state, payload) => {
        if (payload.data.success) {
            state.reviews.push(payload.data.review)
        } else {
            state.status = 'FAILED'
        }
    },
}
