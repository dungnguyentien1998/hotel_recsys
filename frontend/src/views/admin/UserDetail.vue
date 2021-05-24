<template>
    <div>
        <b-form>
            <b-form-group
                id="email-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.register.email') }}</label>-->
                    <!--                    <b-form-input-->
                    <!--                        id="email"-->
                    <!--                        :value="user.email"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        type="email"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.register.email') }}
                    </span>
                    <span class="text-secondary">
                        {{ user.email }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="name-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.register.name') }}</label>-->
                    <!--                    <b-form-input-->
                    <!--                        id="name"-->
                    <!--                        :value="user.name"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        type="text"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.register.name') }}
                    </span>
                    <span class="text-secondary">
                        {{ user.name }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="tel-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.register.tel') }}</label>-->
                    <!--                    <b-form-input-->
                    <!--                        id="tel"-->
                    <!--                        :value="user.tel"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        type="text"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.register.tel') }}
                    </span>
                    <span class="text-secondary">
                        {{ user.tel }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="birthday-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.register.birthday') }}</label>-->
                    <!--                    <b-form-datepicker-->
                    <!--                        id="birthday"-->
                    <!--                        :value="user.birthday"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.register.birthday') }}
                    </span>
                    <span class="text-secondary">
                        {{ convertDate(user.birthday) }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="address-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.register.address') }}</label>-->
                    <!--                    <b-form-input-->
                    <!--                        id="address"-->
                    <!--                        :value="userAddress"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        type="text"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.register.address') }}
                    </span>
                    <span class="text-secondary">
                        {{ userAddress }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="role-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.register.role') }}</label>-->
                    <!--                    <b-form-select-->
                    <!--                        id="role"-->
                    <!--                        :value="user.role"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        :options="roles"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.register.role') }}
                    </span>
                    <span class="text-secondary">
                        {{ user.role }}
                    </span>
                </div>
            </b-form-group>
            <b-form-group
                id="created-group"
                class="col-12"
            >
                <div>
                    <!--                <div class="form-row">-->
                    <!--                    <label class="required col-sm-3 col-form-label">{{ $t('user.user.created') }}</label>-->
                    <!--                    <b-form-datepicker-->
                    <!--                        id="created"-->
                    <!--                        :value="user.created"-->
                    <!--                        class="form-control col-sm-9"-->
                    <!--                        disabled-->
                    <!--                    />-->
                    <span class="font-weight-bolder">
                        {{ $t('user.user.created') }}
                    </span>
                    <span class="text-secondary">
                        {{ convertDate(user.created) }}
                    </span>
                </div>
            </b-form-group>
            <div>
                <b-button
                    :disabled="user.isActive === true"
                    variant="success"
                    size="sm"
                    @click="onActivate(user.uuid)"
                >
                    {{ $t('user.user.unlock') }}
                </b-button>
                <b-button
                    :disabled="user.isActive === false"
                    variant="danger"
                    size="sm"
                    @click="onDeactivate(user.uuid)"
                >
                    {{ $t('user.user.lock') }}
                </b-button>
            </div>
        </b-form>
    </div>
</template>

<script>
export default {
    name: "UserDetail",
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
        userAddress() {
            if (this.user.address == null || this.user.address === '') {
                return this.user.ward + ", " + this.user.district + ", " + this.user.city
            } else {
                return this.user.address + ", " + this.user.ward + ", " + this.user.district + ", " + this.user.city
            }
        }
    },
    methods: {
        convertDate: function (date) {
            return new Date(date).toDateString()
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