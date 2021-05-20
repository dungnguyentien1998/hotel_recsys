<template>
    <layout>
        <template #content>
            <div>
                <div class="align-items-center d-flex">
                    <h2 class="flex-grow-1">
                        {{ $t('user.user.changePassword') }}
                    </h2>
                </div>
            </div>
            <hr>
            <b-form>
                <b-form-group
                    id="old-password-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-3 col-form-label">{{ $t('user.login.oldPassword') }}</label>
                        <b-form-input
                            id="old-password"
                            v-model="$v.form.old_password.$model"
                            class="form-control col-sm-9"
                            :placeholder="$t('user.login.oldPasswordPlaceholder')"
                            type="password"
                        />
                        <button
                            class="btn password"
                            type="button"
                            @click="showOldPassword"
                        >
                            <font-awesome-icon
                                :icon="['fas', 'eye']"
                            />
                        </button>
                    </div>
                </b-form-group>
                <b-form-group
                    id="password-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-3 col-form-label">{{ $t('user.login.newPassword') }}</label>
                        <b-form-input
                            id="password"
                            v-model="$v.form.password.$model"
                            class="form-control col-sm-9"
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
                        <label class="required col-sm-3 col-form-label">{{ $t('user.register.confirmPassword') }}</label>
                        <b-form-input
                            id="confirm-password"
                            v-model="$v.form.password_confirm.$model"
                            class="form-control col-sm-9"
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
                        size="sm"
                        @click="onSubmit"
                    >
                        {{ $t('user.login.sendBtn') }}
                    </b-button>
                </b-form-group>
            </b-form>
        </template>
    </layout>
</template>

<script>
import {validationMixin} from 'vuelidate'
import formMixin from '@/mixin/form-mixin'
import {required, minLength, sameAs} from 'vuelidate/lib/validators'
import snakecaseKeys from 'snakecase-keys'
import Layout from '@/components/layouts/Layout'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faEye} from '@fortawesome/free-solid-svg-icons'

library.add(faEye)

export default {
    name: "ChangePassword",
    components: {Layout},
    mixins: [formMixin],
    data: function () {
        return {
            // Form data
            form: {
                old_password: '',
                password: '',
                password_confirm: ''
            }
        }
    },
    validations: {
        form: {
            old_password: {
                required,
                minLength: minLength(6)
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
        resetForm: function () {
            this.form = {
                old_password: '',
                password: '',
                password_confirm: ''
            }
        },
        showOldPassword: function () {
            let x = document.getElementById("old-password")
            if (x.type === "password") {
                x.type = "text"
            } else {
                x.type = "password"
            }
        },
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
                this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.missing'));
            } else {
                this.$store.dispatch('user/changePassword', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
                        // this.resetForm()
                    } else {
                        this.$bvToast.toast(this.$t('user.user.success.passwordMessage'), {
                            title: this.$t('user.user.success.passwordTitle'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        this.resetForm()
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