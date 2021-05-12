import state from "@/store/modules/review/state";
import getters from "@/store/modules/review/getters";
import mutations from "@/store/modules/review/mutations";
import actions from "@/store/modules/review/actions";


// Review component
export default {
    namespaced: true,
    state, getters, mutations, actions
}