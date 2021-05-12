import {getProvinces, getDistrictsByProvinceCode, getWardsByDistrictCode} from 'sub-vn'

// Handle address, city, district, ward in Vietnam
export default {
    data: function () {
        return {
            // Address form
            form: {
                city: null,
                district: null,
                ward: null,
                address: '',
            },
            // get cities
            cities: [
                {value: null, text: '-----'},
                ...getProvinces().map(city => {
                    return {value: city.code, text: city.name}
                })
            ],
            // Districts
            districts: [{value: null, text: '-----'}],
            // Wards
            wards: [{value: null, text: '-----'}],
        }
    },
    methods: {
        // Get districts by city
        onChangeCity: function (e) {
            this.districts = [
                {value: null, text: '-----'},
                ...getDistrictsByProvinceCode(e).map(district => {
                    return {value: district.code, text: district.name}
                })
            ]

            this.form.district = null
            this.form.ward = null
            this.wards = [{value: null, text: '-----'}]
        },
        // Get wards by districts
        onChangeDistrict: function (e) {
            this.wards = [
                {value: null, text: '-----'},
                ...getWardsByDistrictCode(e).map(ward => {
                    return {value: ward.code, text: ward.name}
                })
            ]
        },
    }
}