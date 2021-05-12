export default {
    // Change status
    // submit: state => {
    //     state.status = 'SUBMIT'
    // },
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    // Save room list
    listRooms: (state, payload) => {
        state.rooms = payload.data.rooms
    },
    // Save new room
    createRoom: (state, payload) => {
        if (payload.data.success) {
            state.rooms.push(payload.data.room)
            state.status = ''
        } else {
            state.status = 'FAILED'
            state.message = payload.data.detail
        }
    },
    // Save updated room
    updateRoom: (state, payload) => {
        if (payload.data.success) {
            let room = payload.data.room
            let index = state.rooms.findIndex(item => item.uuid === room.uuid)
            state.rooms = [
                ...state.rooms.slice(0, index),
                room,
                ...state.rooms.slice(index + 1)
            ]
        } else {
            state.status = 'FAILED'
        }
    },
    // Delete room from list
    deleteRoom: (state, payload) => {
        if (payload.data.success) {
            let room = payload.data.room
            state.rooms = state.rooms.filter(item => item.item !== room.uuid)
        } else {
            state.status = 'FAILED'
        }
    }
}
