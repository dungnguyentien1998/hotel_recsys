<template>
    <layout>
        <template #content>
            <div>
                <div class="align-items-center d-flex">
                    <h2 class="flex-grow-1">
                        {{ $t('user.user.myProfile') }}
                    </h2>
                </div>
                <hr>
                <b-form>
                    <b-form-group
                        id="email-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="required col-sm-3 col-form-label">{{ $t('user.register.email') }}</label>
                            <b-form-input
                                id="email"
                                :value="user.email"
                                class="form-control col-sm-9"
                                type="email"
                                disabled
                            />
                        </div>
                    </b-form-group>
                    <b-form-group
                        id="name-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="required col-sm-3 col-form-label">{{ $t('user.register.name') }}</label>
                            <b-form-input
                                id="name"
                                v-model="$v.form.name.$model"
                                class="form-control col-sm-9"
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
                            <label class="required col-sm-3 col-form-label">{{ $t('user.register.tel') }}</label>
                            <b-form-input
                                id="tel"
                                v-model="$v.form.tel.$model"
                                class="form-control col-sm-9"
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
                            <label class="required col-sm-3 col-form-label">{{ $t('user.register.role') }}</label>
                            <b-form-select
                                id="role"
                                :value="user.role"
                                class="form-control col-sm-9"
                                :options="roles"
                                disabled
                            />
                        </div>
                    </b-form-group>
                    <b-form-group
                        id="birthday-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="col-sm-3 col-form-label">{{ $t('user.register.birthday') }}</label>
                            <b-form-datepicker
                                id="birthday"
                                v-model="$v.form.birthday.$model"
                                class="form-control col-sm-9"
                                :state="validateState('birthday')"
                                :placeholder="$t('user.register.birthdayPlaceholder')"
                            />
                        </div>
                    </b-form-group>
                    <b-form-group
                        id="avatar-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="col-sm-3 col-form-label">{{ $t('user.register.avatar') }}</label>
                            <b-form-file
                                id="avatar"
                                v-model="$v.form.image.$model"
                                class="form-control col-sm-9"
                                :state="validateState('image')"
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
                            <label class="col-sm-3 col-form-label">{{ $t('user.register.city') }}</label>
                            <b-form-select
                                id="city"
                                v-model="$v.form.city.$model"
                                class="form-control col-sm-9"
                                :options="cities"
                                :state="validateState('city')"
                                @change="onChangeCity"
                            />
                        </div>
                    </b-form-group>
                    <b-form-group
                        id="district-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="col-sm-3 col-form-label">{{ $t('user.register.district') }}</label>
                            <b-form-select
                                id="district"
                                v-model="$v.form.district.$model"
                                class="form-control col-sm-9"
                                :options="districts"
                                :state="validateState('district')"
                                @change="onChangeDistrict"
                            />
                        </div>
                    </b-form-group>
                    <b-form-group
                        id="ward-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="col-sm-3 col-form-label">{{ $t('user.register.ward') }}</label>
                            <b-form-select
                                id="ward"
                                v-model="$v.form.ward.$model"
                                class="form-control col-sm-9"
                                :options="wards"
                                :state="validateState('ward')"
                            />
                        </div>
                    </b-form-group>
                    <b-form-group
                        id="address-group"
                        class="col-12"
                    >
                        <div class="form-row">
                            <label class="col-sm-3 col-form-label">{{ $t('user.register.address') }}</label>
                            <b-form-input
                                id="address"
                                v-model="$v.form.address.$model"
                                class="form-control col-sm-9"
                                :state="validateState('address')"
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
                            {{ $t('user.user.submit') }}
                        </b-button>
                    </b-form-group>
                </b-form>
            </div>
        </template>
    </layout>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin';
import addressMixin from '@/mixin/address-mixin';
import {minLength, required} from 'vuelidate/lib/validators';
import Layout from '@/components/layouts/Layout';
import {getDistrictsByProvinceCode, getWardsByDistrictCode, getProvinces} from 'sub-vn';

export default {
    name: "Profile",
    components: {Layout},
    mixins: [validationMixin, formMixin, addressMixin],
    data: function () {
        const user = this.$store.getters['user/user']
        let city_code = null
        if (user.city != null) {
            city_code = getProvinces().filter(option => option.name === user.city)[0].code
        }
        let district_code = null
        if (city_code != null && user.district != null) {
            district_code = getDistrictsByProvinceCode(city_code).filter(option => option.name === user.district)[0].code
        }
        let ward_code = null
        if (district_code != null && user.ward != null) {
            ward_code = getWardsByDistrictCode(district_code).filter(option => option.name === user.ward)[0].code
        }
        return {
            // User data
            user: user,
            // Form data
            form: {
                name: user.name,
                tel: user.tel,
                image: null,
                city: city_code,
                district: district_code,
                ward: ward_code,
                address: user.address,
                birthday: user.birthday,
                role: user.role
            },
            // Role options
            roles: [
                {value: null, text: '-----'},
                {value: 'user', text: this.$t('user.register.user')},
                {value: 'hotelier', text: this.$t('user.register.hotelier')},
                {value: 'admin', text: this.$t('user.register.admin')}
            ]
        }
    },
    computed: {
        // Get user image
        avatar: function () {
            return `${process.env.VUE_APP_PUBLIC_URL}${this.user.image}`
        },
    },
    beforeCreate() {
        this.$store.dispatch('user/account').then(() => {
            this.user = this.$store.getters['user/user']
        })
    },
    created() {
        // Get districts by city
        this.districts = [
            {value: null, text: '-----'},
            ...getDistrictsByProvinceCode(this.form.city).map(district => {
                return {value: district.code, text: district.name}
            })
        ]
        // Get wards by district
        this.wards = [
            {value: null, text: '-----'},
            ...getWardsByDistrictCode(this.form.district).map(ward => {
                return {value: ward.code, text: ward.name}
            })
        ]
    },
    // Form validate
    validations: {
        form: {
            name: {
                required,
            },
            tel: {
                required,
                minLength: minLength(10)
            },
            image: {

            },
            city: {

            },
            district: {

            },
            ward: {

            },
            address: {

            },
            birthday: {

            }
        }
    },
    methods: {
        // Get cities
        citiesOptions: function() {
            return getProvinces()
        },
        // Get districts by city
        districtsOptions: function(code) {
            return getDistrictsByProvinceCode(code)
        },
        // Get wards by district
        wardsOptions: function(code) {
            return getWardsByDistrictCode(code)
        },
        // Handle update profile
        onSubmit: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validate
                this.makeToast(this.$t('user.user.errors.title'), this.$t('user.user.errors.missing'))
            } else {
                const city_code = this.form.city
                const district_code = this.form.district
                if (this.form.city != null) {
                    this.form.city = this.citiesOptions().filter(option => option.code === this.form.city)[0].name
                }
                if (city_code != null && this.form.district != null) {
                    this.form.district = this.districtsOptions(city_code).filter(option => option.code === this.form.district)[0].name
                }
                if (district_code != null && this.form.ward != null) {
                    this.form.ward = this.wardsOptions(district_code).filter(option => option.code === this.form.ward)[0].name
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
                this.$store.dispatch('user/resetStatus')
                this.$store.dispatch('user/updateAccount', this.form).then(() => {
                    if (this.$store.getters['user/status'] === 'FAILED') {
                        // Alert for failed update profile
                        this.makeToast(this.$t('user.user.errors.title'), this.$t('user.user.errors.exceptionOccurred'))
                    } else {
                        // Alert for success update profile
                        this.$bvToast.toast(this.$t('user.user.success.message'), {
                            title: this.$t('user.user.success.title'),
                            autoHideDelay: 2000,
                            variant: 'success'
                        })
                        setTimeout(location.reload.bind(location), 2000)
                    }
                }).catch(() => {
                    this.makeToast(this.$t('user.user.errors.title'), this.$t('user.user.errors.exceptionOccurred'))
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