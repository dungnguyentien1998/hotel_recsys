import axios from 'axios'
import camelcaseKeys from "camelcase-keys";

// Create api object for api calls
export const api = axios.create({
    // URL used for relative path
    baseURL: process.env.VUE_APP_BASE_URL,
    // Parse response from json string to object
    transformResponse: [data => {
        if (data) {
            // Object attribute can be written in camel case
            return (camelcaseKeys(JSON.parse(data), {deep: true}))
        }
    }]
});

// Create api objects for image
export const imageApi = axios.create({
    // URL used for relative path
    baseURL: process.env.VUE_APP_BASE_URL,
    // Return type of image
    responseType: "blob"
});
