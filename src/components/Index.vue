<template>
  <div>
    <nav class="navbar navbar-expand-lg navbar-dark bg-default">
    <div class="container">
        <a class="navbar-brand" href="#">Covid-19</a>
      <span class="text-white"> <i class="fas fa-viruses"></i></span>
        <div class="collapse navbar-collapse" id="navbar-default">
            <div class="navbar-collapse-header">
                <div class="row">
                    <div class="col-6 collapse-brand">
                        <a href="javascript:void(0)">
                            <img src="">
                        </a>
                    </div>
                  
                </div>
            </div>
        </div>
    </div>
</nav>

<div class="card  shadow-lg  m-3 bg-white rounded">
  <div class="card-body">
    <div class="progress-wrapper">
  <div class="progress-info">
    <div class="progress-label">
      <span>Covid-19 Real Time Data</span>
       <span class="pull-right ml-4">Uttar Pradesh</span>
    </div>
  </div>
  <div class="progress">
    <div class="progress-bar bg-success" role="progressbar" aria-valuenow="90" aria-valuemin="0" aria-valuemax="100" style="width: 99%;"></div>
  </div>
</div>
  </div>
</div>



<div class="shadow p-3 m-3 bg-white rounded">
  <div class="row">
    <div class="col-6">
  <p> <img src="@/assets/v.png" class="img-responsive img-fluid" style="height: 30px;">
  <span class="ml-1">
    Total Infected
  </span>
       </p>
  <p><i class="fas fa-thumbtack "></i> <span class="ml-1"> India</span> </p>
  <h3 v-if="active[0].confirmed"><i class="fas fa-arrow-up text-info"></i> {{active[0].confirmed}}</h3>
  <!-- <h3>Recovered <i class="far fa-smile-beam text-success"></i> 48</h3> -->
  </div>
  <div class="col-6 pl-1">
    <img src="@/assets/cough.png" class="img-responsive" style="height :110px" >
  </div>
  </div>
</div>

  <div class="container">
   <div class="row">
      <div class="col-6">
        <div class="shadow p-3 m-3 bg-white rounded text-center">
        <span>  <i class="fas fa-smile-beam text-success"></i></span>
          <p>Discharged</p>
          <h2 v-if="active[0].recovered"> {{active[0].recovered}}</h2>
        </div>
      </div>
        <div class="col-6">
        <div class="shadow p-3 m-3 bg-white rounded text-center">
           <span>  <i class="fas fa-sad-tear text-danger"></i></span>
          <p>Death</p>
          <h2 v-if="active[0].death"> {{active[0].death}}</h2>
        </div>
      </div>
   </div>
  </div>

  <div class="container">
      <div class="shadow p-3 m-3  bg-white rounded">
        <div class="row">
          <div class="col-6">
             <img src="@/assets/india.png" class="img-responsive p-2" style="height :90px" >
          </div>
          <div class="col-6">
            <h3>{{info[1]}} | {{info[0]}}</h3>
            <p class="h6 ml-3">You live here</p>
            <p class="h6">Infected <i class="fas fa-virus text-danger"></i> 745</p>
            <p class="h6">Discharge <i class="fas fa-arrow-up text-success"></i> 745</p>
          </div>
        </div>
      </div>
</div>

  <div class="container mb-4">
    <div class="shadow p-3  bg-white rounded">

      <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">State</th>
      <th scope="col">Confirm</th>
      <th scope="col">Discharge</th>
    </tr>
  </thead>
  <tbody>
    <tr v-for="state in states" v-bind:key="state.id">
      
      <td v-if="state.state">{{(state.state).substring(0,15)}}</td>
      <td v-if="state.confirmed">{{state.confirmed}}</td>
      <td v-if="state.discharged">{{state.discharged}}</td>
    </tr>
   
  </tbody>
</table>
    </div>
    </div>


     <div class="container mb-4">
      <div class="shadow p-3  bg-white rounded">
        <h2 class="text-center">What to Do?</h2>
        <div class="row container">
          <div class="col-7">
            <p id="info" class="h6 mt-4 justify-text">If you are a developer check get my API and use it.</p>
        <router-link to="/api"> 
         <span class="badge badge-success p-1">Check</span>
        </router-link>
          </div>
          <div class="col-3">
             <img src="@/assets/developer.png" class="img-responsive p-2" style="height :90px" >
          </div>
        </div>

  <hr>
         <div class="row m-2">
            <div class="col-7">
             <img src="@/assets/quarantine.png" class="img-responsive p-2" style="height :80px" >
          </div>
          <div class="col-5">
            <p id="info" class="h6 mt-4 justify-text">Just be at home.</p>
       
          </div>
         
        </div>
<hr>
         <div class="row m-2">
          <div class="col-7">
            <p id="info" class="h6 mt-4 justify-text">Wear mask when you are out.</p>
         
          </div>
          <div class="col-3">
             <img src="@/assets/coronavirus.png" class="img-responsive p-2" style="height :90px" >
          </div>
        </div>

  <hr>

    <div class="row m-2">
            <div class="col-7">
             <img src="@/assets/virus (2).png" class="img-responsive p-2" style="height :80px" >
          </div>
          <div class="col-5">
            <p id="info" class="h6 mt-4 justify-text">Keep washing your hands.</p>
          </div>
        </div>
      </div>
     </div>

     <div class="container text-center ml-5 mb-3 pl-5 mx-auto">
       <ul class="nav text-center">
  <li class="nav-item">
    <a class="nav-link active h5" href="https://github.com/boxabhi/CovidVue"><i class="fab fa-github"></i> View code</a>
  </li>
  <li class="nav-item">
   <router-link to="/api">
    <a class="nav-link h5 active"><i class="fab fa-firefox-browser"></i> Get API</a>
   </router-link>
  </li>
  <li class="nav-item">
    <a class="nav-link h5" href="https://www.linkedin.com/in/gupta-abhijeet/"><i class="fab fa-linkedin"></i>LinkedIn</a>
  </li>

</ul>
     </div>
   
  

  <div class="container-fluid bg-dark">
    <div class="container text-center p-3 text-white">
      #BeAtHome
      <p class="text-white h6">Created by Abhijeet Gupta <i class="fas fa-mug-hot"></i> </p>
    </div>
  </div>

  </div>
</template>


<script>
import axios from 'axios';
export default {
  data(){
    return {
      states : [],
      active : [],
      info : [],
    }
  },
  methods :{
    //E1BYpVwtm8LiUS3vgSUEETh5a
      callApi(){
        axios.get("https://cors-anywhere.herokuapp.com/https://whereiscovidapi.herokuapp.com/api/all")
        .then(response => {   
          this.states = response.data
        })
        .catch(error => console.log(error))
      },
      callCases(){
        axios.get("https://cors-anywhere.herokuapp.com/https://whereiscovidapi.herokuapp.com/api/active_Case/all")
        .then(response => {   
          this.active = response.data
        })
        .catch(error => console.log(error))
      },
      callLocation(){
          axios.get("https://api.ipify.org/?format=json")
          .then(response =>{
            axios.get(`https://ipapi.co/${response.data.ip}/json/`)
            .then(response => {
              //console.log(response.data)
              this.info.push(response.data.country)
               this.info.push(response.data.region)
               this.info.push(response.data.region_code)
              this.info.push(response.data.city)
             // console.log("Info",this.info)
            })
            
          })
      },
      getByState(){
        for(var i=0;i<this.state.length;i++){
          if(this.state[i].state == this.info[0]){
            console.log("Found")
          }else{
            console.log(this.state[i])
          }

      }
      }
  },
  created(){
    this.callApi();
    this.callCases();
    this.callLocation();
    this.getByState();
    console.log(this.info)
  }
}
</script>