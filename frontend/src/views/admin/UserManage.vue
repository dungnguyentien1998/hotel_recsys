<template>
    <layout>
        <template #content>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('user.user.searchUser') }}
                </h2>
            </div>
            <br>
            <!--   Search form    -->
            <b-form>
                <b-form-group
                    id="role-group"
                    :label="$t('user.register.role')"
                    label-for="role"
                    label-cols-sm="2"
                    label-cols-lg="2"
                    content-cols-sm="4"
                    content-cols-lg="4"
                >
                    <b-form-select
                        id="role"
                        v-model="$v.form.role.$model"
                        :options="roles"
                        :state="validateState('role')"
                    />
                </b-form-group>
            </b-form>
            <div>
                <b-button
                    v-b-toggle.collapse-1
                    variant="secondary"
                    class="btn-sm"
                >
                    {{ $t('hotel.hotel.advancedSearch') }}
                </b-button>
                <button
                    class="btn btn-sm btn-primary"
                    type="button"
                    style="float: right; margin-right: 550px"
                    @click="onSubmit"
                >
                    {{ $t('user.user.search') }}
                    <font-awesome-icon
                        :icon="['fas', 'search']"
                    />
                </button>
                <b-collapse
                    id="collapse-1"
                    class="mt-2"
                >
                    <b-card>
                        <b-form>
                            <b-form-group
                                id="name-group"
                                :label="$t('user.register.name')"
                                label-for="name"
                                label-cols-sm="2"
                                label-cols-lg="2"
                                content-cols-sm="4"
                                content-cols-lg="4"
                            >
                                <b-form-input
                                    id="name"
                                    v-model="$v.form.name.$model"
                                    :placeholder="$t('user.register.namePlaceholder')"
                                    type="search"
                                />
                            </b-form-group>
                            <b-form-group
                                id="email-group"
                                :label="$t('user.register.email')"
                                label-for="email"
                                label-cols-sm="2"
                                label-cols-lg="2"
                                content-cols-sm="4"
                                content-cols-lg="4"
                            >
                                <b-form-input
                                    id="email"
                                    v-model="$v.form.email.$model"
                                    :placeholder="$t('user.register.emailPlaceholder')"
                                    type="search"
                                />
                            </b-form-group>
                        </b-form>
                    </b-card>
                </b-collapse>
            </div>
            <br>
            <hr>
            <div class="align-items-center d-flex">
                <h2 class="flex-grow-1">
                    {{ $t('user.user.title') }}
                </h2>
            </div>
            <br>
            <div
                v-if="loading"
                class="loader"
            />
            <div
                id="users-table"
                :current-page="currentPage"
                :per-page="perPage"
            >
                <!--      Users table         -->
                <b-table
                    v-if="rows > 0"
                    :items="filterUsers"
                    :fields="columns"
                    :responsive="true"
                    hover
                    striped
                >
                    <template
                        #cell(index)="data"
                    >
                        {{ data.index + 1 + (currentPage - 1) * perPage }}
                    </template>
                    <template
                        #cell(role)="data"
                    >
                        {{ $t('user.user.' + data.item.role) }}
                    </template>
                    <template
                        #cell(action)="data"
                    >
                        <b-button
                            v-if="data.item.role !== 'admin'"
                            :disabled="data.item.isActive === true"
                            variant="success"
                            size="sm"
                            @click="onActivate(data.item.uuid)"
                        >
                            {{ $t('user.user.unlock') }}
                        </b-button>
                        <b-button
                            v-if="data.item.role !== 'admin'"
                            :disabled="data.item.isActive === false"
                            variant="danger"
                            href="#"
                            size="sm"
                            @click="$bvModal.show(`modal-${data.item.uuid}-lock`)"
                        >
                            {{ $t('user.user.lock') }}
                        </b-button>
                        <b-button
                            variant="primary"
                            href="#"
                            size="sm"
                            @click="$bvModal.show(`modal-${data.item.uuid}-view`)"
                        >
                            {{ $t('user.user.view') }}
                        </b-button>
                        <b-modal
                            :id="`modal-${data.item.uuid}-lock`"
                            :title="$t('user.user.lockTitle')"
                            size="lg"
                            hide-footer
                        >
                            <deactivate-form :user="data.item" />
                        </b-modal>
                        <b-modal
                            :id="`modal-${data.item.uuid}-view`"
                            :title="$t('user.user.viewUser')"
                            size="lg"
                            hide-footer
                        >
                            <user-detail :user="data.item" />
                        </b-modal>
                    </template>
                </b-table>
            </div>
            <span
                v-if="filterUsers.length === 0 && isSearch"
                style="font-style: italic"
            >
                {{ $t('user.user.noResult') }}
            </span>
            <b-pagination
                v-if="rows > perPage"
                v-model="currentPage"
                :per-page="perPage"
                :total-rows="rows"
                pills
                aria-controls="users-table"
                @change="handlePageChange"
            />
        </template>
    </layout>
</template>

<script>
import {validationMixin} from 'vuelidate';
import formMixin from '@/mixin/form-mixin'
import Layout from '@/components/layouts/Layout';
import UserDetail from "@/views/admin/UserDetail";
import {library} from '@fortawesome/fontawesome-svg-core'
import {faSearch} from '@fortawesome/free-solid-svg-icons'
import DeactivateForm from "@/views/admin/DeactivateForm";
import Pusher from "pusher-js";
import camelcaseKeys from "camelcase-keys";
import {getDistrictsByProvinceCode, getProvinces, getWardsByDistrictCode} from "sub-vn";
library.add(faSearch)


export default {
    name: "User",
    components: {UserDetail, Layout, DeactivateForm},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            // Search form data
            form: {
                role: this.$store.getters['user/role'],
                name: this.$store.getters['user/name'],
                email: this.$store.getters['user/email_search'],
            },
            updateForm: {
                is_active: null
            },
            // Pagination data
            currentPage: this.$store.getters['user/page'],
            perPage: 30,
            rows: 0,
            // User list
            users: [],
            // User list for search function
            filterUsers: [],
            isSearch: false,
            loading: false,
            uuids: []
        }
    },
    computed: {
        columns: function () {
            return [
                {
                    key: 'index',
                    label: this.$t('user.user.no'),
                },
                {
                    key: 'email',
                    label: this.$t('user.register.email'),
                    sortable: true
                },
                {
                    key: 'name',
                    label: this.$t('user.user.name'),
                },
                {
                    key: 'tel',
                    label: this.$t('user.user.tel'),
                },
                {
                    key: 'role',
                    label: this.$t('user.user.role'),
                },
                {
                    key: 'action',
                    label: this.$t('user.user.action'),
                },
            ]
        },
        roles: function() {
            return [
                {value: null, text: '-----'},
                {value: 'user', text: this.$t('user.user.user')},
                {value: 'hotelier', text: this.$t('user.user.hotelier')},
                {value: 'admin', text: this.$t('user.user.admin')}
            ]
        },
    },
    // Form validation
    validations: {
        form: {
            role: {

            },
            name: {

            },
            email: {

            }
        }
    },
    created() {
        this.$store.commit('hotel/setPage', 1)
        this.$store.commit('hotel/setName', null)
        this.$store.commit('hotel/setCity', null)
        this.$store.commit('hotel/setDistrict', null)
        this.$store.commit('hotel/setWard', null)
        this.$store.commit('hotel/setStar', null)
        this.$store.commit('hotel/setIsSearch', false)
        this.retrieveUsers()
        // Repeat code in Hotel Manage
        const params = this.getHotelRequestParams(1, 6)
        this.$store.dispatch('hotel/listHotels', params).then(() => {
            this.hotels = this.$store.getters['hotel/hotels']
            this.filterHotels = this.hotels
            this.$store.commit('hotel/setFullCount', this.$store.getters['hotel/count'])
            this.subscribe()
        })
        this.$store.dispatch('hotel/listUuids').then(() => {
            this.uuids = this.$store.getters['hotel/uuids']
        })
    },
    methods: {
        getRequestParams(currentPage, perPage, role, name, email) {
            let params = []
            if (currentPage) {
                params["page"] = currentPage
                this.$store.commit('user/setPage', currentPage)
            } else {
                if (this.isSearch || this.$store.getters['user/is_search']) {
                    params["page"] = this.$store.getters['user/page']
                }
            }
            if (perPage) {
                params["per_page"] = perPage
            }
            if (role) {
                params["role"] = role
                this.$store.commit('user/setRole', role)
            } else {
                this.$store.commit('user/setRole', role)
                if (this.isSearch || this.$store.getters['user/is_search']) {
                    params["role"] = null
                }
            }
            if (name) {
                params["name"] = name
                this.$store.commit('user/setName', name)
            } else {
                this.$store.commit('user/setName', name)
                if (this.isSearch || this.$store.getters['user/is_search']) {
                    params["name"] = null
                }
            }
            if (email) {
                params["email"] = email
                this.$store.commit('user/setEmailSearch', email)
            } else {
                this.$store.commit('user/setEmailSearch', email)
                if (this.isSearch || this.$store.getters['user/is_search']) {
                    params["email"] = null
                }
            }
            return params
        },
        retrieveUsers() {
            const params = this.getRequestParams(this.currentPage, this.perPage, this.form.role, this.form.name,
                this.form.email)
            this.loading = true
            this.$store.dispatch('user/users', params).then(() => {
                this.users = this.$store.getters['user/users']
                this.filterUsers = this.users
                this.rows = this.$store.getters['user/count']
                this.loading = false
            })
        },
        handlePageChange(value) {
            this.currentPage = value
            this.retrieveUsers()
        },
        getHotelRequestParams(currentPage, perPage) {
            let params = []
            if (currentPage) {
                params["page"] = currentPage
                this.$store.commit('hotel/setPage', currentPage)
            } else {
                if (this.isSearch || this.$store.getters['hotel/is_search']) {
                    params["page"] = this.$store.getters['hotel/page']
                }
            }
            if (perPage) {
                params["per_page"] = perPage
            }
            return params
        },
        // Convert to date string
        convertDate: function (date) {
            return new Date(date).toDateString()
        },
        // Search users by role
        onSubmit: function() {
            this.isSearch = true
            this.$store.commit('user/setIsSearch', true)
            this.currentPage = 1
            this.retrieveUsers()
        },
        compare: function (a,b) {
            if (a.name < b.name) {
                return -1;
            }
            if (a.name > b.name) {
                return  1;
            }
            return 0;
        },
        onActivate: function(uuid) {
            this.$store.dispatch('user/resetStatus')
            this.updateForm.is_active = true
            this.updateForm.uuid = uuid
            this.$store.dispatch('user/updateUser', this.updateForm).then(() => {
                if (this.$store.getters['user/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('user.user.errors.unlockTitle'), this.$t('user.user.errors.exceptionOccurred'))
                } else {
                    this.$bvToast.toast(this.$t('user.user.success.unlockMessage'), {
                        title: this.$t('user.user.success.unlockTitle'),
                        autoHideDelay: 2000,
                        variant: 'success'
                    })
                    setTimeout(location.reload.bind(location), 2000)
                }
            })
        },
        onDeactivate: function (uuid) {
            this.$store.dispatch('user/resetStatus')
            this.updateForm.is_active = false
            this.updateForm.uuid = uuid
            this.$store.dispatch('user/updateUser', this.updateForm).then(() => {
                if (this.$store.getters['user/status'] === 'FAILED') {
                    // Alert for failed api calls
                    this.makeToast(this.$t('user.user.errors.lockTitle'), this.$t('user.user.errors.exceptionOccurred'))
                } else {
                    this.$bvToast.toast(this.$t('user.user.success.lockMessage'), {
                        title: this.$t('user.user.success.lockTitle'),
                        autoHideDelay: 2000,
                        variant: 'success'
                    })
                    setTimeout(location.reload.bind(location), 2000)
                }
            })
        },
        subscribe() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event', data => {
                data = camelcaseKeys(data, {deep: true})
                let new_uuid = data.hotel.uuid
                let check = true
                for (let i=0; i<this.uuids.length; i++) {
                    if (this.uuids[i] === new_uuid) {
                        check = false
                        break
                    }
                }
                if (check === true) {
                    this.$store.commit('hotel/saveHotel', data)
                    this.$store.commit('hotel/saveNewCount')
                }
                // this.$store.commit('hotel/saveHotel', data)
                // this.$store.commit('hotel/saveNewCount')
            })
        }
    }
}
</script>

<style
    lang="scss"
    scoped
>
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