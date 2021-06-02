export default {
    // Reset status
    resetStatus: state => {
        state.status = ''
    },
    // Save complaint list
    listComplaints: (state, payload) => {
        state.complaints = payload.data.complaints
    },
    // Save new complaint
    createComplaint: (state, payload) => {
        if (payload.data.success) {
            state.complaints.push(payload.data.complaint)
        } else {
            state.status = 'FAILED'
        }
    },
    saveComplaint: (state, payload) => {
        if (payload.success) {
            state.complaints.unshift(payload.complaint)
        } else {
            state.status = 'FAILED'
        }
    },
    saveNewComplaint: (state, payload) => {
        if (payload.success) {
            state.new_complaints.unshift(payload.complaint)
        } else {
            state.status = 'FAILED'
        }
    },
}
