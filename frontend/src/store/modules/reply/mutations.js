export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    listReplys: (state, payload) => {
        state.replys = payload.data.replys
    },
    createReply: (state, payload) => {
        if (payload.data.success) {
            state.replys.push(payload.data.reply)
        } else {
            state.status = 'FAILED'
        }
    },
}