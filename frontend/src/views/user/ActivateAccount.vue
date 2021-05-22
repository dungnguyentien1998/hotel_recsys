<template>
    <auth-layout>
        <template #title>
            {{ $t('user.register.activateAccount') }}
        </template>
        <template #form>
            <b-form>
                <b-form-group
                    id="token-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-2 col-form-label">{{ $t('user.login.token') }}</label>
                        <b-form-input
                            id="token"
                            v-model="$v.form.token.$model"
                            class="form-control col-sm-10"
                            :state="validateState('token')"
                            :placeholder="$t('user.register.tokenPlaceholder')"
                            type="text"
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
import {required, email, minLength, sameAs} from 'vuelidate/lib/validators'
import snakecaseKeys from 'snakecase-keys'
import AuthLayout from '@/components/layouts/AuthLayout'


export default {
    name: "ActivateAccount",
    components: {AuthLayout},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            // Form data
            form: {
                token: '',
            }
        }
    },
    validations: {
        form: {
            token: {
                required,
            },
        }
    },
    methods: {
        onSubmit: function () {
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.missing'));
            } else {
                this.form.email = localStorage.getItem("email")
                this.$store.dispatch('user/activateAccount', this.form).then(() => {
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

<style scoped>

</style>