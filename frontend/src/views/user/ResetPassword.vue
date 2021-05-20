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
                        <button
                            class="btn password"
                            type="button"
                            @click="showPassword"
                        >
                            <font-awesome-icon
                                :icon="['fas', 'eye']"
                            />
                        </button>
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
                        <button
                            class="btn password"
                            type="button"
                            @click="showPasswordConfirm"
                        >
                            <font-awesome-icon
                                :icon="['fas', 'eye']"
                            />
                        </button>
                    </div>
                </b-form-group>
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
import {required, email, minLength, sameAs} from 'vuelidate/lib/validators'
import snakecaseKeys from 'snakecase-keys'
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
        },
        showPasswordConfirm: function () {
            let x = document.getElementById("confirm-password")
            if (x.type === "password") {
                x.type = "text"
            } else {
                x.type = "password"
            }
        },
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
            } else {
                this.$store.dispatch('user/resetPassword', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
                        // this.resetForm()
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