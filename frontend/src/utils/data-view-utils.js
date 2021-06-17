import {getDistrictsByProvinceCode, getProvinces, getWardsByDistrictCode} from "sub-vn";
import json from "../mixin/trans/db_en.json";

export default {
    methods: {
        getImgSrc: function (amenity) {
            let images = require.context('../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
        },
        getHotelImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        getFormatPrice(price) {
            if (!price) {
                return price
            }
            let temp = price.toString()
            let result = ''
            for (let i=temp.length - 1; i>=0; i--) {
                result = temp.charAt(i) + result
                if ((temp.length - i) % 3 === 0) {
                    result = "." + result
                }
            }
            if (result.charAt(0) === ".") {
                result = result.substring(1)
            }
            return result
        },
        getTransAddress: function (address, ward, district, city) {
            let city_en = city
            let district_en = district
            let ward_en = ward
            if (localStorage.getItem("language") === "en") {
                let city_code = getProvinces().filter(option => option.name === city)[0].code
                const provinces = json.province
                city_en = provinces.filter(option => option.idProvince === city_code)[0].name
                let district_code = getDistrictsByProvinceCode(city_code).filter(option => option.name === district)[0].code
                const dists = json.district
                district_en = dists.filter(option => option.idDistrict === district_code)[0].name
                let ward_code = getWardsByDistrictCode(district_code).filter(option => option.name === ward)[0].code
                const communes = json.commune
                ward_en = communes.filter(option => option.idCoummune === ward_code)[0].name
            }
            if (address == null || address === "") {
                return ward_en + ", " + district_en + ", " + city_en
            } else {
                return address + ", " + ward_en + ", " + district_en + ", " + city_en
            }
            // if (address == null || address === "") {
            //     return ward + ", " + district + ", " + city
            // } else {
            //     return address + ", " + ward + ", " + district + ", " + city
            // }
        },
    }
}