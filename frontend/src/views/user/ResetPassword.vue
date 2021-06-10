<template>
    <auth-layout>
        <template #title>
            {{ $t('user.login.resetPassword') }}
        </template>
        <template #form>
            <b-form>
                <b-form-group
                    id="token-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.login.token') }}</label>
                        <b-form-input
                            id="token"
                            v-model="$v.form.token.$model"
                            class="form-control col-sm-8"
                            :state="validateState('token')"
                            :placeholder="$t('user.login.tokenPlaceholder')"
                            type="text"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="password-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.login.newPassword') }}</label>
                        <b-form-input
                            id="password"
                            v-model="$v.form.password.$model"
                            class="form-control col-sm-8"
                            :state="validateState('password')"
                            :placeholder="$t('user.login.newPasswordPlaceholder')"
                            type="password"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="confirm-password-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.register.confirmPassword') }}</label>
                        <b-form-input
                            id="confirm-password"
                            v-model="$v.form.password_confirm.$model"
                            class="form-control col-sm-8"
                            :state="validateState('password_confirm')"
                            :placeholder="$t('user.register.confirmPasswordPlaceholder')"
                            type="password"
                        />
                    </div>
                </b-form-group>
                <b-form-checkbox
                    style="float: right"
                    @change="showPassword"
                >
                    {{ $t('user.login.showPassword') }}
                </b-form-checkbox>
                <br>
                <b-form-group>
                    <b-button
                        variant="success"
                        type="button"
                        block
                        @click="onSubmit"
                    >
                        {{ $t('user.login.sendBtn') }}
                    </b-button>
                </b-form-group>
            </b-form>
        </template>
    </auth-layout>
</template>

<script>
import {validationMixin} from 'vuelidate'
import formMixin from '@/mixin/form-mixin'
import {required, minLength, sameAs} from 'vuelidate/lib/validators'
import AuthLayout from '@/components/layouts/AuthLayout'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faEye} from '@fortawesome/free-solid-svg-icons'

library.add(faEye)

export default {
    name: "ResetPassword",
    components: {AuthLayout},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            // Form data
            form: {
                token: '',
                password: '',
                password_confirm: ''
            }
        }
    },
    validations: {
        form: {
            token: {
                required,
            },
            password: {
                required,
                minLength: minLength(6)
            },
            password_confirm: {
                required,
                sameAsPassword: sameAs('password')
            },
        }
    },
    methods: {
        showPassword: function () {
            let x = document.getElementById("password")
            if (x.type === "password") {
                x.type = "text"
            } else {
                x.type = "password"
            }

            let z = document.getElementById("confirm-password")
            if (z.type === "password") {
                z.type = "text"
            } else {
                z.type = "password"
            }
        },
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                if (this.form.password === '' || this.form.password == null) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.password'))
                } else
                if (this.form.password_confirm === '' || this.form.password_confirm == null) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.passwordConfirm'))
                } else
                if (this.form.password.length < 6) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.passwordLength'))
                } else
                if (this.form.password !== this.form.password_confirm) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.passwordSame'))
                } else {
                    this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.missing'));
                }
            } else {
                this.$store.dispatch('user/resetPassword', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
                    } else {
                        // Push to login if success, need to add success message
                        this.$router.push('/login')
                    }
                }).catch(() => {
                    this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.exceptionOccurred'))
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
.password {
    position: absolute;
    border-radius: 5px;
    right: 5px;
    z-index: 2;
    border: none;
    top: 2px;
}
</style>