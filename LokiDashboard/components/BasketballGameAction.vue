<template>
  <v-container>
    <v-dialog v-model="notification_dialog" persistent max-width="600px">
      <v-card>
        <v-card-title>
          <span class="headline">Editar Notificación</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row allign="center">
              <v-col>
                <v-text-field
                  label="Texto de notificación *"
                  required
                  v-model="newMessage"
                  counter="100"
                  :rules="notification_rules"
                  outlined
                ></v-text-field>
                <small>* Indica que es un valor requerido</small>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="gray darken-3" text @click="notification_dialog = false"
            >Cerrar</v-btn
          >
          <v-btn
            color="primary darken-1"
            text
            :loading="button_loading"
            @click.native="editNotification()"
            >Guardar</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-dialog v-model="edit_play_dialog" persistent max-width="500px">
      <v-form v-model="valid" ref="edit_form">
        <v-card>
          <v-card-title>
            <span class="headline">Editar Jugada</span>
          </v-card-title>

          <v-row justify="center">
            <v-col cols="12" sm="4">
              <v-card-title class="body-1" style="word-break: normal;"
                >Tipo de Jugada</v-card-title
              >
            </v-col>
            <v-col cols="12" sm="6" allign="center">
              <v-select
                v-model="current_play"
                :items="plays"
                menu-props="auto"
                label="Jugada *"
                outlined
              ></v-select>
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-col cols="12" sm="4">
              <v-card-title class="body-1" style="word-break: normal;"
                >Equipo de Interés</v-card-title
              >
            </v-col>
            <v-col cols="12" sm="6">
              <v-select
                v-model="current_team"
                :items="teams"
                menu-props="auto"
                label="Equipo *"
                outlined
              ></v-select>
            </v-col>
          </v-row>
          <v-row justify="center">
            <v-col cols="12" sm="4">
              <v-card-title class="body-1" style="word-break: normal;"
                >Selccione Atleta</v-card-title
              >
            </v-col>
            <v-col cols="12" sm="6">
              <v-select
                v-if="current_team === 'UPRM'"
                v-model="current_athlete"
                :items="uprmAthletes"
                :item-text="get_uprm_item_text"
                item-value="athlete_id"
                label="Atleta *"
                :rules="[v => v != null || 'Debe seleccionar un atleta']"
                required
                outlined
              ></v-select>
              <v-select
                v-if="current_team === 'Oponente'"
                v-model="current_athlete"
                :items="oppAthletes"
                :item-text="get_opp_item_text"
                item-value="number"
                label="Atleta *"
                :rules="[v => v != null || 'Debe seleccionar un atleta']"
                required
                outlined
              ></v-select>
            </v-col>
          </v-row>
          <small class="mx-12">* Indica que es un valor requerido</small>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="gray darken-3" text @click="edit_play_dialog = false"
              >Cerrar</v-btn
            >
            <v-btn
              color="primary darken-1"
              text
              :disabled="!valid"
              :loading="button_loading"
              @click.native="editPlay()"
              >Guardar</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-form>
    </v-dialog>
    <v-dialog v-model="delete_dialog" persistent max-width="300">
      <v-card>
        <v-card-title class="text-center" style="word-break: normal;"
          >Eliminar Acción de Juego</v-card-title
        >
        <v-card-text
          >Por favor confirme si desea eliminar la acción de juego
          seleccionada.</v-card-text
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="gray darken-3" text @click="delete_dialog = false"
            >No</v-btn
          >
          <v-btn
            color="green darken-1"
            :loading="button_loading"
            text
            @click="deleteGameAction()"
            >Sí</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-hover v-slot:default="{ hover }" open-delay="25">
      <v-card
        v-if="action_type === notification"
        width="550px"
        :elevation="hover ? 16 : 2"
      >
        <v-toolbar :color="in_color" dark flat>
          <v-row justify="center" align="center">
            <v-card-title>{{ game_actions_map[action_type] }}</v-card-title>
          </v-row>
        </v-toolbar>
        <v-row align="center">
          <v-col :cols="4" justify="center">
            <v-avatar size="100" class="mx-10">
              <v-icon
                x-large
                :color="in_color"
                v-if="!athlete_img"
                height="100px"
                >mdi-bell-outline</v-icon
              >
            </v-avatar>
          </v-col>
          <v-col justify="center">
            <v-row allign="center">
              <v-col>
                <v-card-title class="text-center" style="word-break: normal;">{{
                  message
                }}</v-card-title>
              </v-col>
            </v-row>
          </v-col>
          <v-col :cols="2" allign="center" justify="right">
            <v-row>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    class="ma-2"
                    color="gray"
                    fab
                    small
                    dark
                    @click.native="startEditNotification()"
                    v-on="on"
                    v-if="$store.state.userAuth.userPermissions[5]['18']"
                  >
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                </template>
                <span>Editar notificación</span>
              </v-tooltip>
            </v-row>
            <v-row>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    class="ma-2"
                    color="red"
                    fab
                    small
                    dark
                    @click.native="delete_dialog = true"
                    v-on="on"
                    v-if="$store.state.userAuth.userPermissions[4]['17']"
                  >
                    <v-icon>mdi-trash-can</v-icon>
                  </v-btn>
                </template>
                <span>Eliminar notificación</span>
              </v-tooltip>
            </v-row>
          </v-col>
        </v-row>
      </v-card>
      <v-card v-else width="550px" :elevation="hover ? 16 : 2">
        <v-toolbar :color="in_color" dark flat>
          <v-row justify="center" align="center">
            <v-card-title>{{ game_actions_map[action_type] }}</v-card-title>
          </v-row>
        </v-toolbar>
        <v-row>
          <v-col :cols="3">
            <v-avatar size="100" class="mx-10">
              <v-icon
                x-large
                :color="in_color"
                v-if="!athlete_img"
                height="100px"
                >mdi-account</v-icon
              >
              <v-img v-else :src="athlete_img" alt="ATHLETE" height="100px">
                <template v-slot:placeholder>
                  <v-layout fill-height align-center justify-center ma-0>
                    <v-progress-circular
                      indeterminate
                      :color="in_color"
                    ></v-progress-circular>
                  </v-layout>
                </template>
              </v-img>
            </v-avatar>
          </v-col>
          <v-col allign="center">
            <v-row class="mx-10" justify="center">
              <v-card-title class="text-center" style="word-break: normal;"
                >#{{ athlete_number }}. {{ athlete_name }}</v-card-title
              >
            </v-row>
          </v-col>
          <v-col :cols="2" allign="center" justify="right">
            <v-row>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    class="ma-2"
                    color="gray"
                    fab
                    small
                    dark
                    @click.native="startEditPlay()"
                    v-on="on"
                    v-if="$store.state.userAuth.userPermissions[5]['18']"
                  >
                    <v-icon>mdi-pencil</v-icon>
                  </v-btn>
                </template>
                <span>Editar jugada</span>
              </v-tooltip>
            </v-row>
            <v-row>
              <v-tooltip bottom>
                <template v-slot:activator="{ on }">
                  <v-btn
                    class="ma-2"
                    color="red"
                    fab
                    small
                    dark
                    @click.native="delete_dialog = true"
                    v-on="on"
                    v-if="$store.state.userAuth.userPermissions[4]['17']"
                  >
                    <v-icon>mdi-trash-can</v-icon>
                  </v-btn>
                </template>
                <span>Eliminar jugada</span>
              </v-tooltip>
            </v-row>
          </v-col>
        </v-row>
      </v-card>
    </v-hover>
  </v-container>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: {
    action_type: String, // After this, the following props are optional depending on the action_type.
    message: String,
    athlete_name: String,
    athlete_number: Number,
    athlete_id: Number,
    athlete_img: String,
    in_color: String,
    id: String,
    event_id: Number,
    uprmAthletes: [],
    oppAthletes: [],
    team: String
  },
  data: () => ({
    // Notification keyword.
    notification: "Notification",

    // Dialog flags.
    notification_dialog: false,
    delete_dialog: false,
    edit_play_dialog: false,

    valid: false,
    button_loading: false,

    // Content to be displayed in the Edit Game Action dialog.
    teams: ["Oponente", "UPRM"],

    team_map: {
      Oponente: "opponent",
      UPRM: "uprm"
    },

    plays: [
      "Tiro Libre",
      "Tiro de Campo",
      "Tiro de tres",
      "Asistencia",
      "Robo de balon",
      "Tapón",
      "Rebote",
      "Perdida de balón",
      "Falta"
    ],

    current_team: null,
    current_play: "",
    current_athlete: null,

    game_actions_map: {
      Notification: "Notificación",
      Notificación: "Notification",
      Freethrow: "Tiro Libre",
      "Tiro Libre": "freethrow",
      "2Points": "Tiro de Campo Anotado",
      "Tiro de Campo": "2Points",
      "3Points": "Tiro de Tres",
      "Tiro de tres": "threepoints",
      Assist: "Asistencia",
      Asistencia: "Assist",
      Bloqueo: "Blocks",
      Blocks: "Tapón",
      Steals: "Robo",
      Rebound: "Rebote",
      Turnover: "Perdida de balón",
      "Perdida de balón": "Turnover",
      Foul: "Falta",
      Falta: "Foul"
    },

    // Rules and placeholders.
    newMessage: "",
    notification_rules: [
      v =>
        (v.length > 0 && v.length <= 100) ||
        "Las notificaciones deben tener entre 1 y 100 caracteres."
    ]
  }),
  methods: {
    ...mapActions({
      updateGameAction: "BasketballPBP/updateGameAction",
      removeGameAction: "BasketballPBP/removeGameAction"
    }),

    // Setup v-models for editting a notification.
    startEditNotification() {
      this.current_team = this.team;
      this.newMessage = this.message;
      this.notification_dialog = true;
    },

    // Edit a notification game action.
    async editNotification() {
      // Create payload with new message and notification info.
      if (this.newMessage.length >= 1 && this.newMessage.length <= 100) {
        const payload = {
          event_id: this.event_id,
          action_id: this.id,
          data: {
            action_type: this.notification,
            message: this.newMessage
          }
        };
        // Update notification.
        this.button_loading = true;
        if (await this.updateGameAction(payload)) {
          this.notification_dialog = false;
        }
        this.button_loading = false;
      }
    },

    async deleteGameAction() {
      const payload = {
        event_id: this.event_id,
        action_id: this.id
      };

      this.button_loading = true;
      if (await this.removeGameAction(payload)) {
        this.delete_dialog = false;
      }
      this.button_loading = false;
    },

    startEditPlay() {
      this.edit_play_dialog = true;
      this.current_team = this.team;
      this.current_play = this.game_actions_map[this.action_type];

      // Find current UPRM athlete.
      if (this.current_team === "UPRM") {
        let index = -1;
        for (let i = 0; i < this.uprmAthletes.length; i++) {
          if (this.uprmAthletes[i].athlete_id === this.athlete_id) {
            index = i;
            break;
          }
        }

        if (index === -1) {
          this.current_athlete = null;
        } else {
          this.current_athlete = this.uprmAthletes[index].athlete_id;
        }
      }

      // Find current opponent athlete.
      else {
        let index = -1;
        for (let i = 0; i < this.oppAthletes.length; i++) {
          if (this.oppAthletes[i].number === this.athlete_id) {
            index = i;
            break;
          }
        }

        if (index === -1) {
          this.current_athlete = null;
        } else {
          this.current_athlete = this.oppAthletes[index].number;
        }
      }
    },

    async editPlay() {
      // Verify the content in the form is valid.
      if (!this.$refs.edit_form.validate()) {
        return;
      }

      // Make sure an athlete was selected.
      if (this.current_athlete == null) {
        return;
      }

      // Determine if the athlete was selected.
      let index = -1;
      if (this.current_team === "UPRM") {
        for (let i = 0; i < this.uprmAthletes.length; i++) {
          if (this.uprmAthletes[i].athlete_id == this.current_athlete) {
            index = i;
            break;
          }
        }
      } else {
        for (let i = 0; i < this.oppAthletes.length; i++) {
          if (this.oppAthletes[i].number == this.current_athlete) {
            index = i;
            break;
          }
        }
      }

      if (index === -1) {
        this.current_athlete = null;
        !this.$refs.edit_form.validate();
        return;
      }

      const payload = {
        event_id: this.event_id,
        action_id: this.id,
        data: {
          action_type: this.game_actions_map[this.current_play],
          athlete_id: this.current_athlete,
          team: this.team_map[this.current_team]
        }
      };
      // Close edit play dialog if request is successful.
      this.button_loading = true;
      if (await this.updateGameAction(payload)) {
        this.edit_play_dialog = false;
      }
      this.button_loading = false;
    },

    map_action(action_name) {
      switch (action_name) {
        case "Notification":
          return "Notificación";

        case "Freethrow":
          return "Tiro Libre";

        case "twopoints":
          return "Tiro de Campo";

        case "threepoints":
          return "Tiro de Tres";

        case "Assist":
          return "Asistencia";

        case "Blocks":
          return "tapón";

        case "Steals":
          return "Robo";

        case "Rebounds":
          return "Rebote";

        case "Turnovers":
          return "Perdida de Balón";

        case "Foul":
          return "Falta";

        default:
          return "Acción Desconocida";
      }
    },

    // Given an item (UPRM ATHLETE), return its name.
    get_uprm_item_text(item) {
      let index = -1;

      for (let i = 0; i < this.uprmAthletes.length; i++) {
        if (item.athlete_id === this.uprmAthletes[i].athlete_id) {
          index = i;
          break;
        }
      }

      if (index === -1) {
        return null;
      }

      const athlete = this.uprmAthletes[index];

      if (item.middle_name === "") {
        return (
          "#" + athlete.number + " " + item.first_name + " " + item.last_names
        );
      }
      return (
        "#" +
        athlete.number +
        " " +
        item.first_name +
        " " +
        item.middle_name +
        " " +
        item.last_names
      );
    },
    get_opp_item_text(item) {
      let index = -1;

      for (let i = 0; i < this.oppAthletes.length; i++) {
        if (item.number === this.oppAthletes[i].number) {
          index = i;
          break;
        }
      }

      if (index === -1) {
        return null;
      }

      const athlete = this.oppAthletes[index];

      return "#" + athlete.number + " " + item.name;
    }
  },
  computed: {
    getRoster: function() {
      // UPRM selected.
      if (this.current_team === "UPRM") {
        console.log(this.uprmAthletes);
        return this.uprmAthletes;
      }
      // Opponent selected.
      if (this.current_team === "Oponente") {
        return this.oppAthletes;
      }

      // Otherwise, send an empty list.
      return [];
    }
  }
};
</script>
