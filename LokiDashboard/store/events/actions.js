export default {
    async getEvents({commit,dispatch}) {
        try {
            const response = await this.$axios.get('events/')
            commit("SET_EVENTS", response.data.Events)
            commit("SET_EVENT",null)

        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.Error, color: 'error'}, {root: true})
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }

        }
    },

    async getEventByID({commit,dispatch},eid) {
        try{
            const response = await this.$axios.get('events/'+eid+'/')
            commit("SET_EVENT",response.data.Event)            

        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.Error, color: 'error'}, {root: true})
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }
        }
    },

    async getEventTeams({commit,dispatch}) {
        try{
            const response = await this.$axios.get('teams/all/')
            commit("SET_EVENT_TEAMS",response.data.Teams)            

        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.Error, color: 'error'}, {root: true})
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }
        }
    },

    async addEvent({commit,dispatch},eventJSON){
        try{
            commit("SET_EVENTS",[])
            
            const response = await this.$axios.post('events/team/'+eventJSON.team_id+'/',eventJSON)
            dispatch('notifications/setSnackbar', {text: response.data.Event, color: 'success'}, {root: true})
            //this.$router.push('/eventos/')
        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.Error, color: 'error'}, {root: true})
                return 'error'
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }
        }
    },

    async editEvent({commit,dispatch},eventJSON){
        try{
            commit("SET_EVENTS",[])      
            const response = await this.$axios.put('events/'+eventJSON.event_id+'/',eventJSON)
            dispatch('notifications/setSnackbar', {text: response.data.Event, color: 'success'}, {root: true})
            //this.$router.go()
        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.Error, color: 'error'}, {root: true})
                return 'error'
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }
        }
    },

    async removeEvent({commit,dispatch},eventID){
        try{          
            const response = await this.$axios.delete('events/'+eventID+'/')
            commit("DELETE_EVENT",eventID)
            dispatch('notifications/setSnackbar', {text: `El evento con identificador:${eventID} ha sido removido.`, color: 'success'}, {root: true})
            
        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.Error, color: 'error'}, {root: true})
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }
        }
    },

    async startPBPSequence({commit,dispatch},eventJSON){
        try{
            
            commit("SET_EVENTS",[])
            
            const response = await this.$axios.post('pbp/'+eventJSON.sport_name,{event_id:eventJSON.event_id})
            
            dispatch('notifications/setSnackbar', {text: response.data.MSG, color: 'success'}, {root: true})
            this.$router.push('/jugadas-voleibol/'+eventJSON.event_id)
        }catch(error){
            if(!!error.response.data){
                dispatch('notifications/setSnackbar', {text: error.response.data.ERROR, color: 'error'}, {root: true})
            }else{
                dispatch('notifications/setSnackbar', {text: error.message, color: 'error'}, {root: true})
            }
        }
        
    }
    
    
     
}