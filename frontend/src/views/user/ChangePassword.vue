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
                            :state="validateState('old_password')"
                            :placeholder="$t('user.login.oldPasswordPlaceholder')"
                            type="password"
                        />
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
                        <label class="required col-sm-3 col-form-label">{{ $t('user.register.confirmPassword') }}</label>
                        <b-form-input
                            id="confirm-password"
                            v-model="$v.form.password_confirm.$model"
                            class="form-control col-sm-9"
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
    created() {
        this.$store.commit('hotel/setPage', 1)
        this.$store.commit('hotel/setName', null)
        this.$store.commit('hotel/setCity', null)
        this.$store.commit('hotel/setDistrict', null)
        this.$store.commit('hotel/setWard', null)
        this.$store.commit('hotel/setStar', null)
        this.$store.commit('hotel/setIsSearch', false)
    },
    methods: {
        resetForm: function () {
            this.form = {
                old_password: '',
                password: '',
                password_confirm: ''
            }
        },
        showPassword: function () {
            let x = document.getElementById("password")
            if (x.type === "password") {
                x.type = "text"
            } else {
                x.type = "password"
            }

            let y = document.getElementById("old-password")
            if (y.type === "password") {
                y.type = "text"
            } else {
                y.type = "password"
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
                this.$store.dispatch('user/changePassword', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
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