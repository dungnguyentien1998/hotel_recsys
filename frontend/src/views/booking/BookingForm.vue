<template>
    <b-form>
        <!--  Booking check in date      -->
        <b-form-group
            id="checkin-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('booking.bookingForm.checkIn') }}</label>
                <b-form-datepicker
                    id="check_in"
                    v-model="$v.form.check_in_time.$model"
                    class="form-control col-sm-9"
                    :state="validateState('check_in_time')"
                    :min="first"
                    :placeholder="$t('booking.bookingForm.checkInPlaceholder')"
                />
            </div>
        </b-form-group>
        <!--  Booking check out date      -->
        <b-form-group
            id="checkout-group"
            class="col-12"
        >
            <div class="form-row">
                <label class="required col-sm-3 col-form-label">{{ $t('booking.bookingForm.checkOut') }}</label>
                <b-form-datepicker
                    id="check_out"
                    v-model="$v.form.check_out_time.$model"
                    class="form-control col-sm-9"
                    :state="validateState('check_out_time')"
                    :min="last"
                    :placeholder="$t('booking.bookingForm.checkOutPlaceholder')"
                />
            </div>
        </b-form-group>
        <br>
        <br>
        <div>
            <!--      Users table         -->
            <b-table
                id="users-table"
                :items="types"
                :fields="fields"
                :responsive="true"
                hover
                striped
            >
                <template
                    #cell(roomType)="data"
                >
                    <span class="font-weight-bolder">
                        {{ data.item.name }}
                    </span>
                    <div>{{ $t('booking.bookingForm.area') }}: {{ data.item.area }} ㎡</div>
                    <div>
                        <b-link
                            :href="hotelImage(data.item.images[0])"
                            target="_blank"
                        >
                            {{ $t('booking.bookingForm.viewImage') }}
                        </b-link>
                    </div>
                </template>
                <template
                    #cell(capacity)="data"
                >
                    <div>{{ $t('booking.bookingForm.adult') }}: {{ data.item.adultNumber }}</div>
                    <div>{{ $t('booking.bookingForm.children') }}: {{ data.item.childrenNumber }} </div>
                </template>
                <template
                    #cell(amenities)="data"
                >
                    <div class="test">
                        <ul
                            style="padding: 0; list-style-type: none"
                        >
                            <li
                                v-for="(amenity, index) in data.item.amenities"
                                :key="`${data.item.uuid}-amenity-${index}`"
                            >
                                <img
                                    :src="getSrc(amenity)"
                                    :alt="amenity"
                                    class="icon"
                                >
                                <span>{{ amenity }}</span>
                            </li>
                        </ul>
                    </div>
                </template>
                <template
                    #cell(available)="data"
                >
                    {{ getAvailable(data.item.name) }}
                    {{
                        (getAvailable(data.item.name) === ' ') ? '' : $tc('hotel.hotel.room', getAvailable(data.item.name))
                    }}
                </template>
                <template
                    #cell(rooms)="data"
                >
                    <div
                        v-if="showAvailable(data.item.name)"
                    >
                        <span style="color: #cd0505">
                            {{ message(data.item.name) }}
                        </span>
                    </div>
                    <b-form-select
                        v-model="form.booking_counts[getIndex(data.item.name)]"
                        :options="numberOpts(data.item.name, data.item.price)"
                    />
                </template>
            </b-table>
            <p>
                <span class="font-weight-bolder">
                    {{ $t('booking.bookingForm.totalPrice') }}:
                </span>
                <span>
                    {{ totalPrice }} VND ({{ $t('booking.booking.description') }})
                </span>
            </p>
        </div>
        <button
            class="btn btn-primary"
            type="button"
            @click="onSubmit"
        >
            {{ $t('booking.bookingForm.submit') }}
        </button>
    </b-form>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {required} from 'vuelidate/lib/validators';
import dataUtil from "@/utils/data-view-utils"

export default {
    name: "BookingForm",
    mixins: [validationMixin, formMixin, dataUtil],
    data: function () {
        const now = new Date()
        const today = new Date(now.getFullYear(), now.getMonth(), now.getDate())
        const minDate = new Date(today)
        minDate.setDate(minDate.getDate() + 1)
        const types = this.$store.getters['type/types']
        const types_length = types.length
        let booking_counts = []
        let room_types = []
        let availables = []
        for (let i = 0; i < types_length; i++) {
            booking_counts.push(0)
            room_types.push(types[i].name)
            availables.push(0)
        }
        let check_in_time = null
        let check_out_time = null
        if (this.$store.getters['booking/save'] != null) {
            check_in_time = this.$store.getters['booking/check_in']
            check_out_time = this.$store.getters['booking/check_out']
        }
        return {
            // Form data
            form : {
                check_in_time: check_in_time,
                check_out_time: check_out_time,
                hotel_id: null,
                booking_counts: booking_counts
            },
            first: minDate,
            last: minDate,
            numberOptions: [
                {value: 0, text: '-----'},
                {value: 1, text: '1'},
                {value: 2, text: '2'},
                {value: 3, text: '3'},
                {value: 4, text: '4'},
                {value: 5, text: '5'},
            ],
            types: types,
            room_types: room_types,
            // available rooms for each type
            availables: availables,
        }
    },
    computed: {
        totalPrice() {
            let sum = 0
            if (this.form.check_in_time === null || this.form.check_out_time === null) {
                return sum
            }
            const types = this.$store.getters['type/types']
            const types_length = types.length
            for (let i = 0; i < types_length; i++) {
                sum = sum + this.form.booking_counts[i]*types[i].price
            }
            let date_in = new Date(this.form.check_in_time)
            let date_out = new Date(this.form.check_out_time)
            let delta = (date_out.getTime() - date_in.getTime())/ (1000*3600*24)
            sum = sum * delta
            return this.formatPrice(sum)
        },
        fields: function() {
            return [
                {
                    key: 'roomType',
                    label: this.$t('booking.bookingForm.roomType'),
                    thStyle: {width: '200px'}
                },
                {
                    key: 'capacity',
                    label: this.$t('booking.bookingForm.capacity'),
                    thStyle: {width: '150px'}
                },
                {
                    key: 'amenities',
                    label: this.$t('booking.bookingForm.amenities'),
                    thStyle: {width: '450px'}
                },
                {
                    key: 'rooms',
                    label: this.$t('booking.bookingForm.rooms'),
                    // thStyle: {width: '250px'}
                },
            ]
        }
    },
    created() {
        // this.getStripePublishableKey();
        this.$store.dispatch('type/listTypes', this.$route.params.uuid).then(() => {
            this.types = this.$store.getters['type/types']
        })
    },
    // Form validation
    validations: {
        form: {
            check_in_time: {
                required
            },
            check_out_time: {
                required
            },
        }
    },
    methods: {
        hotelImage: function (uri) {
            return this.getHotelImage(uri)
        },
        message(roomType) {
            let n = this.getAvailable(roomType)
            let result = ''
            if (n < 0) {
                return result
            } else {
                if (localStorage.getItem("language") === "en") {
                    result = 'Only ' + n + ' rooms available'
                } else {
                    result = 'Chỉ còn ' + n + ' phòng trống'
                }
                return result
            }
        },
        numberOpts(roomType, price) {
            let opts = []
            opts.push({value: 0, text: '-----'})
            let n = 5
            if (this.$store.getters['booking/save'] != null) {
                n = this.getAvailable(roomType)
                if (n < 0) {
                    n = 5
                }
            }
            for (let i = 1; i <= n; i++) {
                opts.push({value: i, text: i.toString() + " (" + this.formatPrice(price*i) + " VND)"})
            }
            return opts
        },
        formatPrice(price) {
            return this.getFormatPrice(price)
        },
        // getStripePublishableKey() {
        //     fetch('http://localhost:8000/api/config')
        //         .then((result) => result.json())
        //         .then((data) => {
        //
        //             this.stripe = Stripe(data.publicKey);
        //         });
        // },
        // purchase(bookingId) {
        //
        //     fetch('http://localhost:8000/api/create-checkout-session', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json',
        //         },
        //         body: JSON.stringify({ booking_id: bookingId }),
        //     })
        //         .then((result) => result.json())
        //         .then((data) => {
        //             console.log(data);
        //
        //             return this.stripe.redirectToCheckout({ sessionId: data.sessionId });
        //         })
        //         .then((res) => {
        //             console.log(res);
        //         });
        // },
        getIndex: function(room_type) {
            let index = 0
            const types = this.$store.getters['type/types']

            for (let i=0; i<types.length; i++) {
                const roomType = types[i].name
                if (roomType === room_type) {
                    return index
                }
                index = index + 1
            }
            return index
        },
        getAvailable: function (roomType) {
            const available_types = this.$store.getters['booking/available_types']
            const available_numbers = this.$store.getters['booking/available_numbers']
            let index = available_types.length;
            for (let i=0; i<available_types.length; i++) {
                if (available_types[i] === roomType) {
                    index = i;
                    break;
                }
            }
            if (index === available_types.length) {
                return -1
            } else {
                return available_numbers[index]
            }
        },
        getSrc: function (amenity) {
            return this.getImgSrc(amenity)
        },
        // Parse date string to right format
        convertDate: function(date_string) {
            let date = new Date(date_string)
            let format_date = date.getFullYear() + "-" + (date.getMonth() + 1) + "-" + date.getDate() + " " +
                date.getHours() + ":" + date.getMinutes() + ":" + date.getSeconds();
            return format_date;
        },
        showAvailable: function (roomType) {
            return this.$store.getters['booking/save'] != null && this.message(roomType) !== '';
        },
        // Get available rooms with each types
        onGetAvailable: function () {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), this.$t('booking.bookingForm.errors.missing'))
            } else if (Date.parse(this.form.check_in_time) >= Date.parse(this.form.check_out_time)) {
                // Alert if check in greater than check out
                this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), this.$t('booking.bookingForm.errors.timeAfter'))
            } else {
                this.form.hotel_id = this.$route.params.uuid
                this.form.room_types = this.room_types
                this.form.check_in_time = this.convertDate(this.form.check_in_time)
                this.form.check_out_time = this.convertDate(this.form.check_out_time)
                this.$store.commit('booking/setCheckIn', this.form.check_in_time)
                this.$store.commit('booking/setCheckOut', this.form.check_out_time)
                this.$store.commit('booking/setHotelId', this.form.hotel_id)
                this.$store.dispatch('booking/resetStatus')
                this.$store.dispatch('booking/newCreateBooking', this.form).then(() => {
                    if (this.$store.getters['booking/status'] === 'FAILED') {
                        this.$store.commit('booking/setSave', "0")
                        // Alert for failed api calls
                        const message = this.$store.getters['booking/message']
                        let data = JSON.parse(message)
                        for (const [key, value] of Object.entries(data)) {
                            this.availables[this.getIndex(key)] = value
                            this.$store.commit('booking/setAvailableTypes', key)
                            this.$store.commit('booking/setAvailableNumbers', value)
                        }
                        window.location.reload()
                    }
                })
            }
        },
        // Handle booking
        onSubmit: function() {
            this.$v.form.$touch();
            if (this.$v.form.$anyError) {
                // Alert for form validation
                this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), this.$t('booking.bookingForm.errors.missing'))
            } else if (Date.parse(this.form.check_in_time) >= Date.parse(this.form.check_out_time)) {
                // Alert if check in greater than check out
                this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), this.$t('booking.bookingForm.errors.timeAfter'))
            } else {
                // Check if user select amount of rooms
                let check = false
                const len = this.form.booking_counts.length
                for (let i=0; i<len; i++) {
                    if (this.form.booking_counts[i] > 0) {
                        check = true
                        break
                    }
                }
                if (check === false) {
                    this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), this.$t('booking.bookingForm.errors.roomNumber'))
                } else {
                    this.form.hotel_id = this.$route.params.uuid
                    this.form.room_types = this.room_types
                    this.form.check_in_time = this.convertDate(this.form.check_in_time)
                    this.form.check_out_time = this.convertDate(this.form.check_out_time)
                    this.$store.commit('booking/setCheckIn', this.form.check_in_time)
                    this.$store.commit('booking/setCheckOut', this.form.check_out_time)
                    this.$store.commit('booking/setHotelId', this.form.hotel_id)

                    this.$store.dispatch('booking/resetStatus')
                    this.$store.dispatch('booking/newCreateBooking', this.form).then(() => {
                        if (this.$store.getters['booking/status'] === 'FAILED') {
                            this.$store.commit('booking/setSave', "0")
                            // Alert for failed api calls
                            const message = this.$store.getters['booking/message']
                            let data = JSON.parse(message)
                            let failed_message = ""
                            this.$store.commit('booking/clearAvailableTypes')
                            this.$store.commit('booking/clearAvailableNumbers')
                            if (localStorage.getItem("language") === "en") {
                                for (const [key, value] of Object.entries(data)) {
                                    this.availables[this.getIndex(key)] = value
                                    this.$store.commit('booking/setAvailableTypes', key)
                                    this.$store.commit('booking/setAvailableNumbers', value)
                                    failed_message += value.toString() + " " + key + " rooms, "
                                }
                                const n = failed_message.length
                                failed_message = failed_message.slice(0, n-2)
                                failed_message = "Only " + failed_message + " available right now"
                            } else {
                                for (const [key, value] of Object.entries(data)) {
                                    this.availables[this.getIndex(key)] = value
                                    this.$store.commit('booking/setAvailableTypes', key)
                                    this.$store.commit('booking/setAvailableNumbers', value)
                                    failed_message += value.toString() + " phòng " + key + ", "
                                }
                                const n = failed_message.length
                                failed_message = failed_message.slice(0, n-2)
                                failed_message = "Chỉ còn " + failed_message + " có thể đặt"
                            }
                            const types = this.$store.getters['type/types']
                            const types_length = types.length
                            for (let i = 0; i < types_length; i++) {
                                this.form.booking_counts[i] = 0
                            }
                            this.makeToast(this.$t('booking.bookingForm.errors.createTitle'), failed_message)
                            // window.location.reload()
                        } else {
                            // Alert for success
                            this.$store.commit('booking/resetSave')
                            this.$bvToast.toast(this.$t('booking.bookingForm.success.message'), {
                                title: this.$t('booking.bookingForm.success.title'),
                                autoHideDelay: 2000,
                                variant: 'success'
                            })
                            setTimeout(location.reload.bind(location), 2000)
                        }
                    })
                }
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
.icon {
    height: 15px;
    width: 15px;
}
.th-class {
    max-width: 50px;
}
li.list-order {
    list-style: none;
    float: left;
    padding: 0 10px;
    margin-bottom: 5px;
    display: inline-block;
}
li.list-order:nth-child(odd) {clear: left}

.test ul {
    display: flex;
    flex-wrap: wrap;
    padding-left: 0;
}
.test ul li {
    list-style: none;
    flex: 0 0 33.333333%;
}


</style>