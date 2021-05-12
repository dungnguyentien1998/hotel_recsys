import state from "@/store/modules/favorite/state";
import getters from "@/store/modules/favorite/getters";
import mutations from "@/store/modules/favorite/mutations";
import actions from "@/store/modules/favorite/actions";


// Favorite module
export default {
    namespaced: true,
    state, getters, mutations, actions
}