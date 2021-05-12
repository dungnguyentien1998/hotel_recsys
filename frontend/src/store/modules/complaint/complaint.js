import state from "@/store/modules/complaint/state";
import getters from "@/store/modules/complaint/getters";
import mutations from "@/store/modules/complaint/mutations";
import actions from "@/store/modules/complaint/actions";


// Complaint module
export default {
    namespaced: true,
    state, getters, mutations, actions
}