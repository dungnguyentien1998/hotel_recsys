import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"
import user from "@/store/modules/user/user"
import hotel from '@/store/modules/hotel/hotel'
import room from '@/store/modules/room/room'
import favorite from '@/store/modules/favorite/favorite'
import recommendation from '@/store/modules/recommendation/recommendation'
import booking from '@/store/modules/booking/booking'
import complaint from '@/store/modules/complaint/complaint'
import review from '@/store/modules/review/review'
import type from '@/store/modules/roomtype/type'
import reply from '@/store/modules/reply/reply'

Vue.use(Vuex);

// Create vuex store object
export const store = new Vuex.Store({
    modules: {
        user,
        hotel,
        room,
        favorite,
        recommendation,
        booking,
        complaint,
        review,
        type,
        reply
    },
    plugins: [createPersistedState({
        key: 'vuex',
        reducer(val) {
            if (localStorage.getItem('token') === null) {
                return null
            }
            return val
        }
    })],
});
