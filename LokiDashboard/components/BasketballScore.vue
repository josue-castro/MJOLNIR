<template>
  <v-container>
    <v-row>
      <v-col>
        <v-row justify="center">
          <h1 class="text-lg-center">{{ uprm_team }}</h1>
        </v-row>
        <v-row justify="center">
          <v-layout row wrap align-center>
            <v-col class="text-right">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    @click.native="sendAdjust(uprm, -1)"
                    class="ma-2"
                    color="red"
                    fab
                    small
                    dark
                    v-on="on"
                  >
                    <v-icon>mdi-minus</v-icon>
                  </v-btn>
                </template>
                <span>Quitar un punto a UPRM</span>
              </v-tooltip>
            </v-col>
          </v-layout>
          <v-col>
            <v-card class="ma-3 pa-6" outlined tile>
              <h1 class="text-lg-center">{{ current_uprm_score[current_set-1] }}</h1>
            </v-card>
          </v-col>
          <v-layout row wrap align-center>
            <v-col class="text-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    @click.native="sendAdjust(uprm, 1)"
                    class="ma-2"
                    color="green"
                    fab
                    small
                    dark
                    v-on="on"
                  >
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <span>Añadir un punto a UPRM</span>
              </v-tooltip>
            </v-col>
          </v-layout>
        </v-row>
      </v-col>
      <v-col>
        <v-row justify="center">
          <h2 class="text-md-center">MARCADOR</h2>
        </v-row>
        <v-row justify="center">
          <v-card class="ma-3 pa-6" outlined tile>
            <h1 class="text-md-center">{{ current_uprm_score[0]+current_uprm_score[1]+current_uprm_score[2]+current_uprm_score[3] }} - {{ current_opp_score[0]+current_opp_score[1]+current_opp_score[2]+current_opp_score[3] }}</h1>
          </v-card>
        </v-row>
        <v-row justify="center">
          <h2 class="text-md-center">PARCIAL</h2>
        </v-row>
        <v-row justify="center">
          <v-layout row wrap align-center>
            <v-col class="text-right">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    @click.native="sendSetAdjust(-1)"
                    class="ma-2"
                    color="red"
                    fab
                    small
                    dark
                    v-on="on"
                  >
                    <v-icon>mdi-minus</v-icon>
                  </v-btn>
                </template>
                <span>Cambiar a parcial anterior</span>
              </v-tooltip>
            </v-col>
          </v-layout>
          <v-card class="ma-3 pa-6" outlined tile>
            <h1 class="text-md-center">{{ current_set }}</h1>
          </v-card>
          <v-layout row wrap align-center>
            <v-col class="text-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    @click.native="sendSetAdjust(1)"
                    class="ma-2"
                    color="green"
                    fab
                    small
                    dark
                    v-on="on"
                  >
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <span>Cambiar al próximo parcial</span>
              </v-tooltip>
            </v-col>
          </v-layout>
        </v-row>
      </v-col>
      <v-col>
        <v-row justify="center">
          <h1 class="text-lg-center">{{ opp_team }}</h1>
        </v-row>
        <v-row justify="center">
          <v-layout row wrap align-center>
            <v-col class="text-right">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    @click.native="sendAdjust(opp, -1)"
                    class="ma-2"
                    color="red"
                    fab
                    small
                    dark
                    v-on="on"
                  >
                    <v-icon>mdi-minus</v-icon>
                  </v-btn>
                </template>
                <span>Quitar un punto al oponente</span>
              </v-tooltip>
            </v-col>
          </v-layout>
          <v-col>
            <v-card class="ma-3 pa-6" outlined tile>
              <h1 class="text-lg-center">{{ current_opp_score[current_set-1] }}</h1>
            </v-card>
          </v-col>
          <v-layout row wrap align-center>
            <v-col class="text-left">
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    @click.native="sendAdjust(opp, 1)"
                    class="ma-2"
                    color="green"
                    fab
                    small
                    dark
                    v-on="on"
                  >
                    <v-icon>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <span>Añadir un punto al oponente</span>
              </v-tooltip>
            </v-col>
          </v-layout>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: {
    uprm_team: String,
    opp_team: String,
    uprm_score: Number,
    opp_score: Number,
    current_set: Number,
    current_uprm_score: Number, // Score of the current set for UPRM team.
    current_opp_score: Number, // Score of the current set for opponent team.
    event_id: String
  },
  data: () => ({
    uprm: "uprm",
    opp: "opponent"
  }),
  methods: {
    ...mapActions({
      sendSetAdjustAction: "BasketballPBP/sendSetAdjust",
      sendScoreAdjust: "BasketballPBP/sendGameAction"
    }),

    sendAdjust(team_name, adjust_no) {
      let payload = {
        data: {
          team: team_name,
          action_type: "ScoreAdjust",
          difference: adjust_no
        },
        event_id: this.event_id
      };
      this.sendScoreAdjust(payload);
    },

    sendSetAdjust(adjust_no) {
      let payload = {
        adjust: adjust_no,
        event_id: this.event_id
      };
      this.sendSetAdjustAction(payload);
    }
  }
};
</script>