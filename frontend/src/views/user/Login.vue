<template>
    <auth-layout>
        <template #title>
            {{ $t('user.login.title') }}
        </template>
        <template #form>
            <!--   Login form         -->
            <b-form>
                <!--   Email             -->
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

                <!--    Password            -->
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
                <b-form-group>
                    <b-button
                        variant="success"
                        type="button"
                        block
                        @click="onSubmit"
                    >
                        {{ $t('user.login.submit') }}
                    </b-button>
                </b-form-group>
            </b-form>
            <!--   Link to register         -->
            <router-link
                :to="{name: 'register'}"
                class="d-block text-secondary text-center"
            >
                {{ $t('user.login.register') }}
            </router-link>
        </template>
    </auth-layout>
</template>

<script>
import {validationMixin} from 'vuelidate'
import formMixin from '@/mixin/form-mixin'
import {required, email, minLength} from 'vuelidate/lib/validators'
import snakecaseKeys from 'snakecase-keys'
import AuthLayout from '@/components/layouts/AuthLayout'


export default {
    name: "Login",
    components: {AuthLayout},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            // Form data
            form: {
                email: '',
                password: ''
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
            password: {
                required,
                minLength: minLength(6)
            }
        }
    },
    computed: {
        // Get user status
        status: function () {
            return this.$store.getters['user/status']
        }
    },
    methods: {
        // Clear form fields
        resetForm: function () {
            this.form = {
                email: this.form.email,
                password: ''
            }
        },
        // Handle login
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('user.login.errors.title'), this.$t('user.login.errors.missing'));
            } else {
                this.$store.dispatch('user/login', snakecaseKeys(this.form)).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        // Alert for failed login api
                        this.makeToast(this.$t('user.login.errors.title'), this.$t('user.login.errors.invalidData'));
                        this.resetForm()
                    } else {
                        this.$store.dispatch('user/account').then(() => {
                            // Check role to push to right router
                            let role = this.$store.getters['user/user'].role
                            switch (role) {
                                case 'user':
                                    this.$router.push('/dashboard/hotels')
                                    break
                                case 'hotelier':
                                    this.$router.push('/hotels')
                                    break;
                                case 'admin':
                                    this.$router.push('/admin/users')
                            }
                        })
                    }
                }).catch(() => {
                    this.makeToast(this.$t('user.login.errors.title'), this.$t('user.login.errors.exceptionOccurred'));
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