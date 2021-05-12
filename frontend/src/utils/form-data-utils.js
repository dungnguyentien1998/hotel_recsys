import FormData from 'form-data';

// Handle form data
export default function (obj) {
    let form = new FormData()
    for (const [key, val] of Object.entries(obj)) {
        // Extract elements in value if value is array
        if (val instanceof Array) {
            for (const item in val) {
                form.append(key, val[item])
            }
        } else {
            form.append(key, val)
        }
    }
    // Create standard form, value is primitive data
    return form
}