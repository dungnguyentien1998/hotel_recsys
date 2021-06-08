<template>
    <auth-layout>
        <template #title>
            {{ $t('user.login.title') }}
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
                    <!--                    <div-->
                    <!--                        style="margin-top: 10px"-->
                    <!--                    >-->
                    <!--                        <b-form-checkbox-->
                    <!--                            style="display: inline-block"-->
                    <!--                            @change="showPassword"-->
                    <!--                        >-->
                    <!--                            {{ $t('user.login.showPassword') }}-->
                    <!--                        </b-form-checkbox>-->
                    <!--                        <router-link-->
                    <!--                            :to="{name: 'forgotPassword'}"-->
                    <!--                            style="display: inline-block; float: right"-->
                    <!--                            class="text-secondary text-right small"-->
                    <!--                        >-->
                    <!--                            {{ $t('user.login.forgotPassword') }}-->
                    <!--                        </router-link>-->
                    <!--                    </div>-->
                    <router-link
                        :to="{name: 'forgotPassword'}"
                        class="text-secondary text-right small d-block"
                    >
                        {{ $t('user.login.forgotPassword') }}
                    </router-link>
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
import {library} from '@fortawesome/fontawesome-svg-core'
import {faEye} from '@fortawesome/free-solid-svg-icons'

library.add(faEye)


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
        showPassword: function () {
            let x = document.getElementById("password")
            if (x.type === "password") {
                x.type = "text"
            } else {
                x.type = "password"
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
                        let code = this.$store.getters['user/code']
                        if (code === '600') {
                            this.makeToast(this.$t('user.login.errors.title'), this.$t('user.login.errors.invalidData'));
                        } else {
                            this.makeToast(this.$t('user.login.errors.title'), this.$t('user.login.errors.lock'));
                        }

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
.password {
    position: absolute;
    border-radius: 5px;
    right: 5px;
    z-index: 2;
    border: none;
    top: 2px;
}
</style>