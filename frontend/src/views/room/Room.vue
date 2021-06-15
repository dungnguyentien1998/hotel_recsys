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
        <div
            v-if="loading"
            class="loader"
        />
        <div
            id="rooms-list"
            :current-page="currentPage"
            :per-page="perPage"
        >
            <b-card
                v-for="room in filterRooms.slice((currentPage-1)*perPage, (currentPage-1)*perPage+perPage)"
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
                                                            {{ $t('room.room.adultNumber') }}:
                                                        </span>
                                                        <span class="text-secondary">
                                                            {{ room.adultNumber }}
                                                        </span>
                                                    </p>
                                                    <p>
                                                        <span class="font-weight-bolder">
                                                            {{ $t('room.room.childrenNumber') }}:
                                                        </span>
                                                        <span class="text-secondary">
                                                            {{ room.childrenNumber }}
                                                        </span>
                                                    </p>
                                                    <p>
                                                        <span class="font-weight-bolder">
                                                            {{ $t('room.room.area') }}:
                                                        </span>
                                                        <span class="text-secondary">
                                                            {{ room.area }} m2
                                                        </span>
                                                    </p>
                                                    <p>
                                                        <span class="font-weight-bolder">
                                                            {{ $t('room.room.price') }}:
                                                        </span>
                                                        <span class="text-secondary">
                                                            {{ formatPrice(room.price) }} VND
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
        </div>
        <span
            v-if="filterRooms.length === 0 && isSearch"
            style="font-style: italic"
        >
            {{ $t('room.room.noResult') }}
        </span>
        <span
            v-if="rooms.length === 0"
            style="font-style: italic"
        >
            {{ $t('room.room.noRoom') }}
        </span>
        <b-pagination
            v-if="filterRooms.length > perPage"
            v-model="currentPage"
            :per-page="perPage"
            :total-rows="rows"
            pills
            aria-controls="rooms-list"
        />
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
import roleUtil from "@/utils/role-utils"
import dataUtil from "@/utils/data-view-utils"

library.add(faSearch)


export default {
    name: "Room",
    components: {Scrollable, RoomForm},
    mixins: [validationMixin, formMixin, roleUtil, dataUtil],
    data: function () {
        return {
            options: ['clothes rack', 'coffee kit', 'tissue box', 'bathrobes', 'wifi', 'toiletries', 'bathtub',
                        'refrigerator', 'hair dryer', 'electric kettle'],
            rooms: [],
            filterRooms: [],
            currentPage: 1,
            perPage: 6,
            rows: 0,
            form: {
                min_price: null,
                max_price: null,
                room_type: null,
            },
            isSearch: false,
            loading: false
        }
    },
    computed: {
        availableOptions() {
            return this.options.filter(opt => this.form.amenities.indexOf(opt) === -1)
        },
        roleHotelier: function () {
            return this.getRoleHotelier()
        },
        roleUser: function () {
            return this.getRoleUser()
        },
        typeOptions() {
            let opts = []
            const types = this.$store.getters['type/types']
            opts.push({value: null, text: '-----'})

            for (let i=0; i<types.length; i++) {
                const room_type = types[i].name
                opts.push({value: room_type, text: room_type})
            }
            return opts
        }
    },
    // Form validate
    validations: {
        form: {
            min_price: {

            },
            max_price: {

            },
            room_type: {

            },
        }
    },
    created() {
        // Get room data
        this.loading = true
        this.$store.dispatch('room/listRooms', this.$route.params.uuid)
            .then(() => {
                this.rooms = this.$store.getters['room/rooms']
                this.filterRooms = this.rooms
                this.rows = this.filterRooms.length
                this.filterRooms.sort(function (a,b) {
                    return new Date(a.created) - new Date(b.created)
                })
                this.loading = false
            })
    },
    methods: {
        getSrc: function (amenity) {
            return this.getImgSrc(amenity)
        },

        roomAccordion: function (uuid) {
            return `accordion-${uuid}`
        },

        roomImage: function (uri) {
            return `${process.env.VUE_APP_PUBLIC_URL}${uri}`
        },

        convertDate: function (date) {
            return new Date(date).toDateString()
        },
        formatPrice(price) {
            return this.getFormatPrice(price)
        },
        // Handle search room
        onSubmit: function () {
            this.filterRooms = this.rooms
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
            this.rows = this.filterRooms.length
            if (this.filterRooms.length === 0) {
                this.makeToast(this.$t('room.room.errors.search'), this.$t('room.room.noResult'))
                this.isSearch = true
            }
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

<style
    lang="scss"
    scoped
>
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
.loader{
    position: absolute;
    top:0;
    right:0;
    width:100%;
    height:100%;
    background-color:#eceaea;
    background-image: url('../../assets/Spinner-3.gif');
    background-size: 50px;
    background-repeat:no-repeat;
    background-position:center;
    z-index:10000000;
    opacity: 0.4;
    filter: alpha(opacity=40);
}
</style>