export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    // Save review list
    listReviews: (state, payload) => {
        state.reviews = payload.data.reviews
        state.count = payload.data.count
    },
    // Save new review
    createReview: (state, payload) => {
        if (payload.data.success) {
            state.reviews.unshift(payload.data.review)
        } else {
            state.status = 'FAILED'
        }
    },
    saveReview: (state, payload) => {
        if (payload.success) {
            state.reviews.unshift(payload.review)
        } else {
            state.status = 'FAILED'
        }
    },
    saveNewReview: (state, payload) => {
        if (payload.success) {
            state.new_reviews.unshift(payload.review)
        } else {
            state.status = 'FAILED'
        }
    },
    setPage: (state, payload) => {
        state.page = payload
    },
    saveNewCount: state => {
        state.new_count = state.new_count + 1
    },
    resetNewCount: state => {
        state.new_count = 0
    },
}
