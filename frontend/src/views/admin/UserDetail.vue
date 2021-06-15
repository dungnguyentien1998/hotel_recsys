<template>
    <div>
        <b-form>
            <b-form-group
                id="email-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.register.email') }}
                    </span>
                    <span>
                        {{ user.email }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="name-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.register.name') }}
                    </span>
                    <span>
                        {{ user.name }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="tel-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.register.tel') }}
                    </span>
                    <span>
                        {{ user.tel }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="birthday-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.register.birthday') }}
                    </span>
                    <span>
                        {{ convertDate(user.birthday) }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="address-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.register.address') }}
                    </span>
                    <span>
                        {{ getAddress(user.address, user.ward, user.district, user.city) }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="role-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.register.role') }}
                    </span>
                    <span>
                        {{ getRole(user.role) }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="created-group"
                class="col-12"
            >
                <div>
                    <span class="font-weight-bolder">
                        {{ $t('user.user.created') }}
                    </span>
                    <span>
                        {{ convertDate(user.created) }}
                    </span>
                </div>
            </b-form-group>
            <div>
                <b-button
                    v-if="user.role !== 'admin'"
                    :disabled="user.isActive === true"
                    variant="success"
                    size="sm"
                    @click="onActivate(user.uuid)"
                >
                    {{ $t('user.user.unlock') }}
                </b-button>
            </div>
        </b-form>
    </div>
</template>

<script>
import json from '../../mixin/data/db_en.json'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import dataUtil from "@/utils/data-view-utils"
import {validationMixin} from "vuelidate";

export default {
    name: "UserDetail",
    mixins: [validationMixin, dataUtil],
    props: {
        // Hotel data
        user: {
            type: Object,
            default: () => {
                return null
            }
        }
    },
    data: function () {
        return {
            roles: [
                {value: null, text: '-----'},
                {value: 'user', text: this.$t('user.register.user')},
                {value: 'hotelier', text: this.$t('user.register.hotelier')},
                {value: 'admin', text: this.$t('user.register.admin')}
            ],
            updateForm: {
                is_active: null
            },
        }
    },
    computed: {

    },
    methods: {
        getAddress: function (address, ward, district, city) {
            return this.getTransAddress(address, ward, district, city)
        },
        convertDate: function(date_string) {
            let date = new Date(date_string)
            let format_date = date.getDate() + "-" + (date.getMonth() + 1) + "-" + date.getFullYear();
            return format_date;
        },
        getRole: function(role) {
            if (localStorage.getItem("language") === "vi") {
                if (role === 'user') {
                    return "người dùng"
                } else if (role === 'hotelier') {
                    return "chủ khách sạn"
                } else {
                    return "quản trị viên"
                }
            } else {
                return role
            }
        },
        onActivate: function(uuid) {
            this.$store.dispatch('user/resetStatus')
            this.updateForm.is_active = true
            this.updateForm.uuid = uuid
            this.$store.dispatch('user/updateUser', this.updateForm).then(() => {
                if (this.$store.getters['user/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('user.user.errors.unlockTitle'), this.$t('user.user.errors.exceptionOccurred'))
                } else {
                    this.$bvToast.toast(this.$t('user.user.success.unlockMessage'), {
                        title: this.$t('user.user.success.unlockTitle'),
                        autoHideDelay: 2000,
                        variant: 'success'
                    })
                    setTimeout(location.reload.bind(location), 2000)
                }
            })
        },
        onDeactivate: function (uuid) {
            this.$store.dispatch('user/resetStatus')
            this.updateForm.is_active = false
            this.updateForm.uuid = uuid
            this.$store.dispatch('user/updateUser', this.updateForm).then(() => {
                if (this.$store.getters['user/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('user.user.errors.lockTitle'), this.$t('user.user.errors.exceptionOccurred'))
                } else {
                    this.$bvToast.toast(this.$t('user.user.success.lockMessage'), {
                        title: this.$t('user.user.success.lockTitle'),
                        autoHideDelay: 2000,
                        variant: 'success'
                    })
                    setTimeout(location.reload.bind(location), 2000)
                }
            })
        }
    }
}
</script>

<style scoped>

</style>