import formUtil from '@/utils/form-data-utils';
import {api} from "@/api";


export default {
    // Reset status
    resetStatus: context => {
        context.commit('resetStatus');
    },
    // Api login
    login: (context, payload) => {
        context.commit('submit')
        return api.post('login', payload)
            .then(res => {
                context.commit('login', res)
            })
    },
    // Api register
    register: (context, payload) => {
        context.commit('submit')
        let form = formUtil(payload)
        return api.post('register', form)
            .then(res => {
                context.commit('register', res)
            })
    },
    // Api logout
    logout: (context) => {
        context.commit('logout')
    },
    // Api profile
    account: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        return api.get('users/account')
            .then(res => {
                context.commit('account', res)
            })
    },
    // Api update profile
    updateAccount: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        let form = formUtil(payload)
        return api.put('users/account', form)
            .then(res => {
                context.commit('account', res)
            })
    },
    // Api list users
    users: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        return api.get('admin/users')
            .then(res => {
                context.commit('users', res)
            })
    },
    updateUser: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        let uuid = payload.uuid
        delete payload.uuid
        let form = formUtil(payload)
        return api.put(`users/${uuid}`, form).then(res => {
            context.commit('updateUser', res)
        })
    },
    forgotPassword: (context, payload) => {
        context.commit('submit')
        return api.post('forgot-password', payload)
            .then(res => {
                context.commit('forgotPassword', res)
            })
    },
    resetPassword: (context, payload) => {
        context.commit('submit')
        return api.put('forgot-password', payload)
            .then(res => {
                context.commit('forgotPassword', res)
            })
    },
    changePassword: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token')
        return api.put('users/change-password', payload)
            .then(res => {
                context.commit('forgotPassword', res)
            })
    },
}
