export default {
    resetStatus: state => {
        state.status = ''
    },

    listTypes: (state, payload) => {
        state.types = payload.data.types
    },

    createType: (state, payload) => {
        if (payload.data.success) {
            state.types.push(payload.data.type)
        } else {
            state.status = 'FAILED'
        }
    },
    // Save updated type
    updateType: (state, payload) => {
        if (payload.data.success) {
            let type = payload.data.type
            let index = state.types.findIndex(item => item.uuid === type.uuid)
            state.types = [
                ...state.types.slice(0, index),
                type,
                ...state.types.slice(index + 1)
            ]
        } else {
            state.status = 'FAILED'
        }
    },

    deleteType: (state, payload) => {
        if (payload.data.success) {
            let type = payload.data.type
            state.types = state.types.filter(item => item.item !== type.uuid)
        } else {
            state.status = 'FAILED'
        }
    }
}
