import {getDistrictsByProvinceCode, getProvinces, getWardsByDistrictCode} from 'sub-vn'
import json from './data/db_en.json'

// Handle address, city, district, ward in Vietnam
export default {
    data: function () {
        const provinces = json.province
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
                    let trans_text = city.name
                    if (localStorage.getItem("language") === "en") {
                        let province = provinces.filter(option => option.idProvince === city.code)[0]
                        trans_text = province.name
                    }
                    return {value: city.code, text: trans_text}
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
            const dists = json.district
            this.districts = [
                {value: null, text: '-----'},
                ...getDistrictsByProvinceCode(e).map(district => {
                    let trans_text = district.name
                    if (localStorage.getItem("language") === "en") {
                        let dist = dists.filter(option => option.idDistrict === district.code)[0]
                        trans_text = dist.name
                    }
                    return {value: district.code, text: trans_text}
                })
            ]

            this.form.district = null
            this.form.ward = null
            this.wards = [{value: null, text: '-----'}]
        },
        // Get wards by districts
        onChangeDistrict: function (e) {
            const communes = json.commune
            this.wards = [
                {value: null, text: '-----'},
                ...getWardsByDistrictCode(e).map(ward => {
                    let trans_text = ward.name
                    if (localStorage.getItem("language") === "en") {
                        let commune = communes.filter(option => option.idCoummune === ward.code)[0]
                        trans_text = commune.name
                    }
                    return {value: ward.code, text: trans_text}
                })
            ]
        },
    }
}