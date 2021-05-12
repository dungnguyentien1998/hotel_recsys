import state from "@/store/modules/room/state";
import getters from "@/store/modules/room/getters";
import mutations from "@/store/modules/room/mutations";
import actions from "@/store/modules/room/actions";


// Room module
export default {
    namespaced: true,
    state, getters, mutations, actions
}