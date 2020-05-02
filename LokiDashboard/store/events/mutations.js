export default {
    
    SET_EVENT(state,event){
        state.event = event
    },

    SET_EVENTS(state, events) {
        
        state.events = events
    },

    SET_EVENT_TEAMS(state,event_teams){
        state.event_teams = event_teams
    },

    DELETE_EVENT(state,id){
        state.events = state.events.filter(events => events.id !== id)
    },

    ADD_USER(state,event){
        state.events.push(user)
    },


    UPDATE_EVENT(state,event){
        const index = state.users.findIndex(arrevent => arrevent.id === event.id)
        if(index !== -1){
            state.events.splice(index,1,event)
        }
    }
    
}