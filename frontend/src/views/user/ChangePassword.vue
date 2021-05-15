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
                        <label class="required col-sm-3 col-form-label">{{ $t('user.login.password') }}</label>
                        <b-form-input
                            id="password"
                            v-model="$v.form.password.$model"
                            class="form-control col-sm-9"
                            :state="validateState('password')"
                            :placeholder="$t('user.login.passwordPlaceholder')"
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
import {required, email, minLength, sameAs} from 'vuelidate/lib/validators'
import snakecaseKeys from 'snakecase-keys'
import Layout from '@/components/layouts/Layout'

export default {
    name: "ChangePassword",
    components: {Layout},
    mixins: [validationMixin, formMixin],
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
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
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
</style>