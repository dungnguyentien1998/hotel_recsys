<template>
    <b-form>
        <b-form-group
            id="email-group"
            class="col-12"
            style="padding: 0"
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
            style="padding: 0"
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
            style="padding: 0"
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
            id="role-group"
            class="col-12"
            style="padding: 0"
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
        <b-form-group>
            <label class="required">{{ $t('user.user.reason') }}: </label>
            <b-form-textarea
                v-model="$v.form.deactivate_reason.$model"
                :state="validateState('deactivate_reason')"
                rows="3"
                max-rows="6"
                type="text"
            />
        </b-form-group>
        <button
            class="btn btn-sm btn-success"
            type="button"
            @click="onSubmit(user.uuid)"
        >
            {{ $t('hotel.hotel.submit') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required} from 'vuelidate/lib/validators';

export default {
    name: "DeactivateForm",
    mixins: [validationMixin, formMixin],
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
            form: {
                deactivate_reason: null,
            }
        }
    },
    validations: {
        form: {
            deactivate_reason: {
                required
            },
        }
    },
    methods: {
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
        onSubmit: function (uuid) {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast('', this.$t('user.register.errors.missing'))
            } else {
                this.$store.dispatch('user/resetStatus')
                this.form.is_active = false
                this.form.uuid = uuid
                this.$store.dispatch('user/updateUser', this.form).then(() => {
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
}
</script>

<style
    lang="scss"
    scoped
>
.required:after {
    content: " *";
    color: red;
}
</style>