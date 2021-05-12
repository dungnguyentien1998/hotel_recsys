import state from "@/store/modules/booking/state";
import getters from "@/store/modules/booking/getters";
import mutations from "@/store/modules/booking/mutations";
import actions from "@/store/modules/booking/actions";


// Booking module
export default {
    namespaced: true,
    state, getters, mutations, actions
}