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
            <div>
                <!--      Users table         -->
                <b-table
                    v-if="filterUsers.length > 0"
                    id="users-table"
                    :items="filterUsers"
                    :fields="columns"
                    :current-page="currentPage"
                    :per-page="perPage"
                    :responsive="true"
                    hover
                    striped
                >
                    <template
                        #cell(index)="data"
                    >
                        {{ data.index + 1 }}
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
                <span
                    v-if="filterUsers.length === 0 && isSearch"
                    style="font-style: italic"
                >
                    {{ $t('user.user.noResult') }}
                </span>
                <b-pagination
                    v-if="filterUsers.length > perPage"
                    v-model="currentPage"
                    :per-page="perPage"
                    :total-rows="rows"
                    pills
                    aria-controls="users-table"
                />
            </div>
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
library.add(faSearch)


export default {
    name: "User",
    components: {UserDetail, Layout, DeactivateForm},
    mixins: [validationMixin, formMixin],
    data: function () {
        return {
            // Search form data
            form: {
                role: null,
                name: null,
                email: null
            },
            updateForm: {
                is_active: null
            },
            // Pagination data
            currentPage: 1,
            perPage: 30,
            rows: 0,
            // User list
            users: [],
            // User list for search function
            filterUsers: [],
            isSearch: false
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
        // Used for search function
        this.$store.dispatch('user/users')
            .then(() => {
                this.users = this.$store.getters['user/users']
                this.filterUsers = this.users
                this.rows = this.filterUsers.length
                this.filterUsers.sort(this.compare)
            })
        // Repeat code in Hotel Manage
        this.$store.dispatch('hotel/listHotels').then(() => {
            this.hotels = this.$store.getters['hotel/hotels']
            this.filterHotels = this.hotels
            this.filterHotels.sort(function (a,b) {
                return new Date(b.created) - new Date(a.created)
            })
            this.subcribe()
        })
    },
    methods: {
        // Convert to date string
        convertDate: function (date) {
            return new Date(date).toDateString()
        },
        // Search users by role
        onSubmit: function() {
            this.filterUsers = this.users
            if (!!this.form.role) {
                this.filterUsers = this.filterUsers.filter(user =>
                    user.role === this.form.role
                )
            }
            if (!!this.form.name) {
                this.filterUsers = this.filterUsers.filter(user =>
                    user.name.toLowerCase().indexOf(this.form.name.toLowerCase()) > -1
                )
            }
            if (!!this.form.email) {
                this.filterUsers = this.filterUsers.filter(user =>
                    user.email.toLowerCase().indexOf(this.form.email.toLowerCase()) > -1
                )
            }
            this.rows = this.filterUsers.length
            if (this.filterUsers.length === 0) {
                this.makeToast(this.$t('user.user.errors.search'), this.$t('user.user.noResult'))
                this.isSearch = true
            }
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
        subcribe() {
            let pusher = new Pusher('5d873d3e35474aa76004', {
                cluster: 'ap1'
            });
            pusher.subscribe('a_channel');
            pusher.bind('an_event', data => {
                data = camelcaseKeys(data, {deep: true})
                this.$store.commit('hotel/saveHotel', data)
            })
        }
    }
}
</script>

<style scoped>

</style>