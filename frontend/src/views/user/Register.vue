<template>
    <auth-layout>
        <template #title>
            {{ $t('user.register.title') }}
        </template>
        <template #form>
            <b-form>
                <b-form-group
                    id="email-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.register.email') }}</label>
                        <b-form-input
                            id="email"
                            v-model="$v.form.email.$model"
                            class="form-control col-sm-8"
                            :state="validateState('email')"
                            :placeholder="$t('user.register.emailPlaceholder')"
                            type="email"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="password-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.register.password') }}</label>
                        <b-form-input
                            id="password"
                            v-model="$v.form.password.$model"
                            class="form-control col-sm-8"
                            :state="validateState('password')"
                            :placeholder="$t('user.register.passwordPlaceholder')"
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
                <b-form-group
                    id="name-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.register.name') }}</label>
                        <b-form-input
                            id="name"
                            v-model="$v.form.name.$model"
                            class="form-control col-sm-8"
                            :state="validateState('name')"
                            :placeholder="$t('user.register.namePlaceholder')"
                            type="text"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="tel-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.register.tel') }}</label>
                        <b-form-input
                            id="tel"
                            v-model="$v.form.tel.$model"
                            class="form-control col-sm-8"
                            :state="validateState('tel')"
                            :placeholder="$t('user.register.telPlaceholder')"
                            type="text"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="role-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="required col-sm-4 col-form-label">{{ $t('user.register.role') }}</label>
                        <b-form-select
                            id="role"
                            v-model="$v.form.role.$model"
                            class="form-control col-sm-8"
                            :options="roles"
                            :state="validateState('role')"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="birthday-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="col-sm-4 col-form-label">{{ $t('user.register.birthday') }}</label>
                        <b-form-datepicker
                            id="birthday"
                            v-model="$v.form.birthday.$model"
                            class="form-control col-sm-8"
                            :placeholder="$t('user.register.birthdayPlaceholder')"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="avatar-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="col-sm-4 col-form-label">{{ $t('user.register.avatar') }}</label>
                        <b-form-file
                            id="avatar"
                            v-model="$v.form.image.$model"
                            class="form-control col-sm-8"
                            :placeholder="$t('user.register.imagePlaceholder')"
                            :drop-placeholder="$t('user.register.imageDropPlaceholder')"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="city-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="col-sm-4 col-form-label">{{ $t('user.register.city') }}</label>
                        <b-form-select
                            id="city"
                            v-model="$v.form.city.$model"
                            class="form-control col-sm-8"
                            :options="cities"
                            @change="onChangeCity"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="district-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="col-sm-4 col-form-label">{{ $t('user.register.district') }}</label>
                        <b-form-select
                            id="district"
                            v-model="$v.form.district.$model"
                            class="form-control col-sm-8"
                            :options="districts"
                            @change="onChangeDistrict"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="ward-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="col-sm-4 col-form-label">{{ $t('user.register.ward') }}</label>
                        <b-form-select
                            id="ward"
                            v-model="$v.form.ward.$model"
                            class="form-control col-sm-8"
                            :options="wards"
                        />
                    </div>
                </b-form-group>
                <b-form-group
                    id="address-group"
                    class="col-12"
                >
                    <div class="form-row">
                        <label class="col-sm-4 col-form-label">{{ $t('user.register.address') }}</label>
                        <b-form-input
                            id="address"
                            v-model="$v.form.address.$model"
                            class="form-control col-sm-8"
                            :placeholder="$t('user.register.addressPlaceholder')"
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
                        {{ $t('user.register.submit') }}
                    </b-button>
                </b-form-group>
            </b-form>
            <p class="text-center text-secondary d-block">
                {{ $t('user.register.loginText') }}
                <router-link
                    :to="{name: 'login'}"
                    class="text-secondary"
                >
                    {{ $t('user.register.loginLink') }}
                </router-link>
            </p>
        </template>
    </auth-layout>
</template>

<script>
import AuthLayout from '@/components/layouts/AuthLayout'
import {validationMixin} from 'vuelidate'
import formMixin from '@/mixin/form-mixin'
import addressMixin from '@/mixin/address-mixin'
import {required, email, minLength, sameAs} from 'vuelidate/lib/validators'
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';
import {library} from '@fortawesome/fontawesome-svg-core'
import {faEye} from '@fortawesome/free-solid-svg-icons'

library.add(faEye)


export default {
    name: 'Register',
    components: {AuthLayout},
    mixins: [validationMixin, formMixin, addressMixin],
    data: function () {
        return {
            // Form data
            form: {
                email: '',
                password: '',
                password_confirm: '',
                name: '',
                tel: '',
                image: null,
                birthday: null,
                role: null
            },
            // Role options
            roles: [
                {value: null, text: '-----'},
                {value: 'user', text: this.$t('user.register.user')},
                {value: 'hotelier', text: this.$t('user.register.hotelier')}
            ]
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
            },
            password_confirm: {
                required,
                sameAsPassword: sameAs('password')
            },
            name: {
                required,
            },
            tel: {
                required,
                minLength: minLength(10)
            },
            city: {

            },
            district: {

            },
            ward: {

            },
            address: {

            },
            image: {

            },
            birthday: {

            },
            role: {
                required,
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
        // Get cities
        // citiesOptions: function() {
        //     return getProvinces()
        // },
        // // Get districts by city
        // districtsOptions: function(code) {
        //     return getDistrictsByProvinceCode(code)
        // },
        // // Get wards by district
        // wardsOptions: function(code) {
        //     return getWardsByDistrictCode(code)
        // },
        // Clear form
        resetForm: function () {
            this.form = {
                email: this.form.email,
                password: '',
                password_confirm: '',
                name: this.form.name,
                tel: this.form.tel,
                city: null,
                district: null,
                ward: null,
                address: this.form.address,
                image: this.form.image,
                birthday: this.form.birthday,
                role: null
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
        validatePassword: function () {
            let x = document.getElementById("password")
            let invalid = false
            if (x.value === "") {
                invalid = true
            }
            return invalid
        },
        showPasswordConfirm: function () {
            let x = document.getElementById("confirm-password")
            if (x.type === "password") {
                x.type = "text"
            } else {
                x.type = "password"
            }
        },
        // Handle register
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate, need to add more message
                if (this.form.email === '' || this.form.email == null) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.email'))
                } else
                if (this.form.name === '' || this.form.name == null) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.name'))
                } else
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
                } else
                if (this.form.role == null) {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.missing'))
                } else
                {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.invalidData'))
                }
            } else {
                // Change city district ward code to name
                const city_code = this.form.city
                const district_code = this.form.district
                if (this.form.city != null) {
                    this.form.city = this.getProvinces().filter(option => option.code === this.form.city)[0].name
                }
                if (city_code != null && this.form.district != null) {
                    this.form.district = this.getDistrictsByProvinceCode(city_code).filter(option => option.code === this.form.district)[0].name
                }
                if (district_code != null && this.form.ward != null) {
                    this.form.ward = this.getWardsByDistrictCode(district_code).filter(option => option.code === this.form.ward)[0].name
                }
                if (this.form.birthday == null) {
                    delete this.form.birthday
                }
                if (this.form.image == null) {
                    delete this.form.image
                }
                if (this.form.city == null) {
                    delete this.form.city
                }
                if (this.form.district == null) {
                    delete this.form.district
                }
                if (this.form.ward == null) {
                    delete this.form.ward
                }
                this.$store.dispatch('user/register', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        // Alert for failed register api
                        this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.emailUsed'))
                        this.resetForm()
                    } else {
                        this.$store.commit('user/setEmail', this.form.email)
                        // localStorage.setItem("email", this.form.email)
                        this.$bvToast.toast(this.$t('user.register.success.message'), {
                            title: this.$t('user.register.success.title'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        setTimeout(() => this.$router.push('/activate'), 2000)
                    }
                }).catch(() => {
                    this.makeToast(this.$t('user.register.errors.title'), this.$t('user.register.errors.exceptionOccurred'))
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