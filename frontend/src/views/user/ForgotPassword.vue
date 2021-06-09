<template>
    <auth-layout>
        <template #title>
            {{ $t('user.login.forgotPassword') }}
        </template>
        <template #form>
            <b-form>
                <b-form-group
                    id="email-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-3 col-form-label">{{ $t('user.login.email') }}</label>
                        <b-form-input
                            id="email"
                            v-model="$v.form.email.$model"
                            class="form-control col-sm-9"
                            :state="validateState('email')"
                            :placeholder="$t('user.login.emailPlaceholder')"
                            type="email"
                        />
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
import {required, email} from 'vuelidate/lib/validators'
import AuthLayout from '@/components/layouts/AuthLayout'

export default {
    name: "ForgotPassword",
    components: {AuthLayout},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            // Form data
            form: {
                email: '',
            }
        }
    },
    // Form validate
    validations: {
        form: {
            email: {
                required,
                email
            },
        }
    },
    methods: {
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.missing'));
            } else {
                this.$store.dispatch('user/forgotPassword', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
                    } else {
                        // Push to login if success, need to add success message
                        this.$bvToast.toast(this.$t('user.register.success.message'), {
                            title: this.$t('user.register.success.title'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        setTimeout(() => this.$router.push('/reset-password'), 2000)
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