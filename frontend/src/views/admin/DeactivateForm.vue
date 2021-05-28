<template>
    <b-form>
        <b-form-group
            id="email-group"
            class="col-12"
            style="padding: 0"
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
            style="padding: 0"
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
            style="padding: 0"
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
            id="role-group"
            class="col-12"
            style="padding: 0"
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
            {{ $t('review.reviewForm.submitBtn') }}
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