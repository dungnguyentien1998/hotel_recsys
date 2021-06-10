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
                        <label class="required col-sm-3 col-form-label">{{ $t('user.login.token') }}</label>
                        <b-form-input
                            id="token"
                            v-model="$v.form.token.$model"
                            class="form-control col-sm-9"
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
import {required} from 'vuelidate/lib/validators'
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
    created() {

    },
    methods: {
        onSubmit: function () {
            if (this.$v.form.$anyError) {
                this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.missing'));
            } else {
                this.form.email = this.$store.getters['user/email']
                this.$store.dispatch('user/activateAccount', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        this.makeToast(this.$t('user.forgot.errors.title'), this.$t('user.forgot.errors.invalidData'));
                    } else {
                        this.$bvToast.toast(this.$t('user.register.success.registerMessage'), {
                            title: this.$t('user.register.success.title'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        setTimeout(() => this.$router.push('/login'), 2000)
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