import state from "@/store/modules/hotel/state";
import getters from "@/store/modules/hotel/getters";
import mutations from "@/store/modules/hotel/mutations";
import actions from "@/store/modules/hotel/actions";


// Hotel module
export default {
    namespaced: true,
    state, getters, mutations, actions
}