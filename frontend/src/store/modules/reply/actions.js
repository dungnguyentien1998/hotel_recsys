import formUtil from '@/utils/form-data-utils'
import {api} from "@/api"


export default {
    resetStatus: context => {
        context.commit('resetStatus');
    },

    listReplys: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('replys').then(res => {
            context.commit('listReplys', res)
        })
    },

    createReply: (context, payload) => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        let form = formUtil(payload)
        return api.post('replys', form).then(res => {
            context.commit('createReply', res)
        })
    },
}