<template>
  <div>
      <div class="content">
          <div class="row">
              <div class="col-sm-12">
                  <div class="card">
                      <div class="card-header">
                          <h4 class="card-title">Customers</h4>

                      </div>
                      <div class="card-body">
                          <table class="table table-striped walla">
                              <thead>
                              <tr>
                                  <th>id</th>
                                  <th>name</th>
                                  <th>email</th>
                              </tr>
                              </thead>
                              <tbody>
                              <tr v-for="customer in tableData" v-bind:key="_source">
                                  <td>{{customer.customers_id}}</td>
                                  <td>{{customer.customers_firstname}}</td>
                                  <td>{{customer.customers_email}}</td>
                              </tr>
                              </tbody>
                          </table>
                      </div>
                  </div>
              </div>
          </div>
      </div>
  </div>
</template>

 
                   
                
<script>

import axios from 'axios'

    export default {
        data() {
            return {
                tableData: [],
            }
        },
        created() {
          this.getCustomer();
        },

        methods: {
            getCustomer() {
            let query = {

            }  

            axios.get('http://localhost:9200/_search?pretty', {
            params:{
                source: JSON.stringify(query),
                source_content_type: 'application/json' ,}})
                    .then(res => {
                      this.tableData = res.data;
                    })
            }
            },
          }
 </script>