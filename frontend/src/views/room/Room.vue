<template>
    <div>
        <div class="justify-content-center d-flex">
            <p class="flex-grow-1" />
            <b-button
                v-if="roleHotelier"
                class="mb-2 text-right"
                variant="success"
                size="sm"
                @click="$bvModal.show('modal-create')"
            >
                {{ $t('room.room.createBtn') }}
            </b-button>
        </div>
        <hr>
        <b-form>
            <!--            <b-form-group-->
            <!--                id="capacity-group"-->
            <!--                :label="$t('room.room.minCapacity')"-->
            <!--                label-for="capacity"-->
            <!--                label-cols-sm="2"-->
            <!--                label-cols-lg="2"-->
            <!--                content-cols-sm="7"-->
            <!--                content-cols-lg="7"-->
            <!--            >-->
            <!--                <b-form-input-->
            <!--                    id="capacity"-->
            <!--                    v-model="$v.form.capacity.$model"-->
            <!--                    :state="validateState('capacity')"-->
            <!--                    :placeholder="$t('room.room.capacityPlaceholder')"-->
            <!--                    type="text"-->
            <!--                />-->
            <!--            </b-form-group>-->
            <!--            <b-form-group-->
            <!--                id="min-price-group"-->
            <!--                :label="$t('room.room.minPrice')"-->
            <!--                label-for="min-price"-->
            <!--                label-cols-sm="2"-->
            <!--                label-cols-lg="2"-->
            <!--                content-cols-sm="7"-->
            <!--                content-cols-lg="7"-->
            <!--            >-->
            <!--                <b-form-input-->
            <!--                    id="min-price"-->
            <!--                    v-model="$v.form.min_price.$model"-->
            <!--                    :state="validateState('min_price')"-->
            <!--                    :placeholder="$t('room.room.minPrice')"-->
            <!--                    type="text"-->
            <!--                />-->
            <!--            </b-form-group>-->
            <!--            <b-form-group-->
            <!--                id="max-price-group"-->
            <!--                :label="$t('room.room.maxPrice')"-->
            <!--                label-for="max-price"-->
            <!--                label-cols-sm="2"-->
            <!--                label-cols-lg="2"-->
            <!--                content-cols-sm="7"-->
            <!--                content-cols-lg="7"-->
            <!--            >-->
            <!--                <b-form-input-->
            <!--                    id="max-price"-->
            <!--                    v-model="$v.form.max_price.$model"-->
            <!--                    :state="validateState('max_price')"-->
            <!--                    :placeholder="$t('room.room.maxPrice')"-->
            <!--                    type="text"-->
            <!--                />-->
            <!--            </b-form-group>-->
            <b-form-group
                id="type-group"
                :label="$t('room.room.roomType')"
                label-for="type"
                label-cols-sm="2"
                label-cols-lg="2"
                content-cols-sm="7"
                content-cols-lg="7"
            >
                <b-form-select
                    id="type"
                    v-model="$v.form.room_type.$model"
                    :options="typeOptions"
                />
            </b-form-group>
            <button
                class="btn btn-sm btn-primary"
                type="button"
                @click="onSubmit"
            >
                {{ $t('room.room.searchBtn') }}
                <font-awesome-icon
                    :icon="['fas', 'search']"
                />
            </button>
        </b-form>
        <br>
        <b-card
            v-for="room in filterRooms"
            :key="room.uuid"
            class="mb-2 p-1"
            tag="article"
        >
            <div class="d-flex">
                <div class="flex-column d-flex">
                    <b-card-img
                        :src="roomImage(room.image)"
                    />
                    <div class="pt-3 btn-sm btn-group">
                        <button
                            v-if="roleHotelier"
                            class="btn btn-sm btn-primary"
                            @click="$bvModal.show(`modal-${room.uuid}-update`)"
                        >
                            {{ $t('room.room.updateBtn') }}
                        </button>
                        <button
                            v-if="roleHotelier"
                            class="btn btn-sm btn-danger"
                            @click="$bvModal.show(`modal-${room.uuid}-delete`)"
                        >
                            {{ $t('room.room.deleteBtn') }}
                        </button>
                        <b-modal
                            :id="`modal-${room.uuid}-update`"
                            :title="$t('room.room.updateTitle')"
                            size="lg"
                            hide-footer
                        >
                            <room-form :room="room" />
                        </b-modal>
                        <b-modal
                            :id="`modal-${room.uuid}-delete`"
                            :title="$t('room.room.deleteTitle')"
                            size="lg"
                            button-size="sm"
                            :ok-title="$t('button.submit')"
                            :cancel-title="$t('button.unsubmit')"
                            @ok="deleteRoom(room.uuid)"
                        >
                            {{ $t('room.room.confirmDelete') }}
                        </b-modal>
                    </div>
                </div>
                <div class="flex-grow-1">
                    <scrollable>
                        <template #content>
                            <div class="rooms ml-3">
                                <div
                                    role="tablist"
                                    class="accordion"
                                >
                                    <b-card
                                        class="mb-1"
                                        no-body
                                    >
                                        <b-card-header
                                            header-tag="header"
                                            role="tab"
                                            class="p-1"
                                        >
                                            <b-button
                                                v-b-toggle="`accordion-detail-${room.uuid}`"
                                                variant="secondary"
                                                block
                                            >
                                                {{ $t('room.room.roomDetail') }}
                                            </b-button>
                                        </b-card-header>
                                        <!--      Room info                                  -->
                                        <b-collapse
                                            :id="`accordion-detail-${room.uuid}`"
                                            :accordion="`group-detail-${roomAccordion(room.uuid)}`"
                                            role="tabpanel"
                                            visible
                                        >
                                            <b-card-body>
                                                <p
                                                    v-if="roleHotelier"
                                                >
                                                    <span class="font-weight-bolder">
                                                        {{ $t('room.room.roomNumber') }}:
                                                    </span>
                                                    <span class="text-secondary">
                                                        {{ room.roomNumber }} 
                                                    </span>
                                                </p>
                                                <p>
                                                    <span class="font-weight-bolder">
                                                        {{ $t('room.room.roomType') }}
                                                    </span>
                                                    <span class="text-secondary">
                                                        {{ room.roomType }}
                                                    </span>
                                                </p>
                                                <p>
                                                    <span class="font-weight-bolder">
                                                        {{ $t('room.room.capacity') }}:
                                                    </span>
                                                    <span class="text-secondary">
                                                        {{ room.capacity }} 
                                                    </span>
                                                </p>
                                                <p>
                                                    <span class="font-weight-bolder">
                                                        {{ $t('room.room.price') }}:
                                                    </span>
                                                    <span class="text-secondary">
                                                        {{ room.price }} VND
                                                    </span>
                                                </p>
                                            </b-card-body>
                                        </b-collapse>
                                    </b-card>
                                </div>
                                <div
                                    role="tablist"
                                    class="accordion"
                                >
                                    <b-card
                                        class="mb-1"
                                        no-body
                                    >
                                        <b-card-header
                                            header-tag="header"
                                            role="tab"
                                            class="p-1"
                                        >
                                            <b-button
                                                v-b-toggle="`accordion-amenities-${room.uuid}`"
                                                variant="secondary"
                                                block
                                            >
                                                {{ $t('room.room.amenities') }}
                                            </b-button>
                                        </b-card-header>
                                        <!--      Room amenities                                  -->
                                        <b-collapse
                                            :id="`accordion-amenities-${room.uuid}`"
                                            role="tabpanel"
                                            :accordion="`group-amenities-${roomAccordion(room.uuid)}`"
                                            visible
                                        >
                                            <b-card-body>
                                                <b-list-group>
                                                    <b-list-group-item
                                                        v-for="(amenity, index) in room.amenities"
                                                        :key="`${room.uuid}-amenity-${index}`"
                                                        style="border: none"
                                                    >
                                                        <img
                                                            :src="getSrc(amenity)"
                                                            :alt="amenity"
                                                            class="icon"
                                                        >
                                                        {{ amenity }}
                                                    </b-list-group-item>
                                                </b-list-group>
                                            </b-card-body>
                                        </b-collapse>
                                    </b-card>
                                </div>
                            </div>
                        </template>
                    </scrollable>
                </div>
            </div>
        </b-card>
        <b-modal
            id="modal-create"
            :title="$t('room.room.createBtn')"
            size="lg"
            hide-footer
        >
            <room-form />
        </b-modal>
    </div>
</template>

<script>
import Scrollable from '@/components/Scrollable';
import RoomForm from '@/components/RoomForm';
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import {library} from '@fortawesome/fontawesome-svg-core'
import {faSearch} from '@fortawesome/free-solid-svg-icons'

library.add(faSearch)


export default {
    name: "Room",
    components: {Scrollable, RoomForm},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            options: ['clothes rack', 'coffee kit', 'tissue box', 'bathrobes', 'wifi', 'toiletries', 'bathtub',
                        'refrigerator', 'hair dryer', 'electric kettle'],
            rooms: [],
            filterRooms: [],
            form: {
                capacity: null,
                min_price: null,
                max_price: null,
                room_type: null,
                // amenities: []
            },
        }
    },
    computed: {
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
        roleHotelier: function () {
            return (this.$store.getters['user/user'].role === 'hotelier')
        },
        // Check role user
        roleUser: function () {
            return (this.$store.getters['user/user'].role === 'user')
        },
        typeOptions() {
            let opts = []
            const types = this.$store.getters['type/types']
            opts.push({value: null, text: '-----'})
            for (let option in this.$store.getters['type/types']) {
                const room_type = types[option].roomType
                opts.push({value: room_type, text: room_type})
            }
            return opts
        },
    },
    // Form validate
    validations: {
        form: {
            capacity: {

            },
            min_price: {

            },
            max_price: {

            },
            room_type: {

            },
            amenities: {

            }
        }
    },
    created() {
        // Get room data
        this.$store.dispatch('room/listRooms', this.$route.params.uuid)
            .then(() => {
                this.rooms = this.$store.getters['room/rooms']
                this.filterRooms = this.rooms
                this.filterRooms.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
                })
            })
    },
    methods: {
        getSrc: function (amenity) {
            let images = require.context('../../assets/', false, /\.png$/)
            return images('./' + amenity + ".png")
        },
        // Get room accordion
        roomAccordion: function (uuid) {
            return `accordion-${uuid}`
        },
        // Get room image
        roomImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },
        // Convert to date string
        convertDate: function (date) {
            return new Date(date).toDateString()
        },
        // Handle search room
        onSubmit: function () {
            this.filterRooms = this.rooms
            // Search by capacity price type and amenities
            if (!!this.form.capacity) {
                this.filterRooms = this.filterRooms.filter(room =>
                    room.capacity >= this.form.capacity
                )
            }
            if (!!this.form.min_price) {
                this.filterRooms = this.filterRooms.filter(room =>
                    room.price >= this.form.min_price
                )
            }
            if (!!this.form.max_price) {
                this.filterRooms = this.filterRooms.filter(room =>
                    room.price <= this.form.max_price
                )
            }
            if (!!this.form.room_type) {
                this.filterRooms = this.filterRooms.filter(room =>
                    room.roomType === this.form.room_type.toLowerCase()
                )
            }
            // if (!!this.form.amenities) {
            //     const amenities_list = this.form.amenities.map(amenity => amenity.toLowerCase())
            //     this.filterRooms = this.filterRooms.filter(room =>
            //         amenities_list.every(amenity => room.amenities.includes(amenity))
            //     )
            // }
        },
        // Handle delete room
        deleteRoom: function (uuid) {
            this.$store.dispatch('room/resetStatus')
            this.$store.dispatch('room/deleteRoom', {hotelId: this.$route.params.uuid, roomId: uuid})
                .then(() => {
                    if (this.$store.getters['room/status'] === 'FAILED') {
                        // Alert for failed delete api
                        this.makeToast(this.$t('room.room.errors.title'), this.$t('room.room.errors.exceptionOccurred'))
                    } else {
                        window.location.reload()
                    }
                })
        }
    }
}
</script>

<style scoped>
.card-img {
    object-fit: cover;
    height: 400px;
    width: 400px;
}

.rooms {
    height: 553px;
    overflow-y: auto;
}
.icon {
    height: 30px;
    width: 30px;
}
</style>