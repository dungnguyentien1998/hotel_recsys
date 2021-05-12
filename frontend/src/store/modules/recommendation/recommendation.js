import state from "@/store/modules/recommendation/state";
import getters from "@/store/modules/recommendation/getters";
import mutations from "@/store/modules/recommendation/mutations";
import actions from "@/store/modules/recommendation/actions";


// Recommendation modules
export default {
    namespaced: true,
    state, getters, mutations, actions
}