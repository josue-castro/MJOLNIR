<template>
  <v-container>
    <v-row v-if="loading" justify="center">
      <v-progress-circular
        :active="loading"
        indeterminate
        :size="50"
        color="primary"
      ></v-progress-circular>
    </v-row>
    <ErrorCard
      v-if="init_error && !loading"
      :in_color="uprm_color"
      :error_header="error_header"
      :error_message="error_message"
    />
    <v-card fixed v-if="!init_error && !loading">
      <v-toolbar color="green darken-1" dark flat>
        <v-spacer />
        <v-toolbar-title class="title">{{ sportName }}</v-toolbar-title>
        <v-spacer />
      </v-toolbar>
      <v-container>
        <v-row align="center" justify="center">
          <SoccerScore
            :uprm_team="uprm_team_name"
            :opp_team="opponentName"
            :uprm_score="uprmScore"
            :opp_score="oppScore"
            :current_set="currentSet"
            :current_uprm_score="currentUPRMSet"
            :current_opp_score="currentOppSet"
            :event_id="event_id"
            v-if="$store.state.userAuth.userPermissions[5]['18']"
          />
          <VolleyballScoreDisplayOnly
            :uprm_team="uprm_team_name"
            :opp_team="opponentName"
            :uprm_score="uprmScore"
            :opp_score="oppScore"
            :current_set="currentSet"
            :current_uprm_score="currentUPRMSet"
            :current_opp_score="currentOppSet"
            :event_id="event_id"
            v-else
          />
        </v-row>
        <v-row>
          <v-col>
            <v-divider class="mx-4" horizontal></v-divider>
          </v-col>
        </v-row>
        <v-tabs align-with-title centered grow :color="uprm_color">
          <v-tabs-slider :color="uprm_color" />
          <v-tab>JUGADA A JUGADA</v-tab>

          <v-tab>ESTADÍSTICAS POR EQUIPO</v-tab>

          <v-tab>ESTADÍSTICAS POR ATLETAS</v-tab>

          <v-tab-item>
            <div v-if="$store.state.userAuth.userPermissions[5]['18']">
              <v-row justify="center">
                <v-card-title>Administrador de Jugadas</v-card-title>
              </v-row>
              <v-row>
                <SoccerPBPActionsAdder
                  :event_id="event_id"
                  :uprm_team_name="uprm_team_name"
                  :opp_team_name="opponentName"
                  :uprm_roster="uprmRoster"
                  :valid_uprm_roster="validUPRMRoster"
                  :opp_roster="oppRoster"
                  :opp_color="oppColor"
                />
              </v-row>
            </div>
            <v-row>
              <v-divider class="mx-4" horizontal></v-divider>
            </v-row>

            <div v-if="$store.state.userAuth.userPermissions[5]['18']">
              <v-row justify="center">
                <v-card-title>Acciones Generales</v-card-title>
              </v-row>

              <v-row justify="center">
                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      class="ma-6"
                      color="primary"
                      dark
                      v-on="on"
                      width="175"
                      @click.native="on_notification_pressed()"
                    >
                      <v-icon class="mx-1">mdi-android-messages</v-icon
                      >Notificación
                    </v-btn>
                  </template>
                  <span>Crear notificación de juego</span>
                </v-tooltip>

                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      class="ma-6"
                      color="primary"
                      dark
                      v-on="on"
                      width="225"
                      @click.native="startChooseColor()"
                    >
                      <v-icon class="mx-1">mdi-palette</v-icon>Color de Oponente
                    </v-btn>
                  </template>
                  <span>Seleccionar color de equipo oponente</span>
                </v-tooltip>

                <v-tooltip bottom>
                  <template v-slot:activator="{ on }">
                    <v-btn
                      class="ma-6"
                      color="primary"
                      dark
                      v-on="on"
                      width="175"
                      @click.native="end_pbp_dialog = true"
                    >
                      <v-icon class="mx-1">mdi-file-excel-box</v-icon>Finalizar
                    </v-btn>
                  </template>
                  <span>Finalizar secuencia de jugadas</span>
                </v-tooltip>
              </v-row>
            </div>

            <v-row justify="center">
              <v-card-title>Lista de Jugadas</v-card-title>
            </v-row>
            <v-container v-for="action in gameActions" :key="action.key + 500">
              <SoccerGameAction
                v-if="action.action_type === notification"
                align="center"
                justify="center"
                :action_type="action.action_type"
                :message="action.message"
                :athlete_number="action.athlete_number"
                :athlete_name="action.athlete_name"
                :athlete_img="action.athlete_img"
                in_color="gray"
                :id="action.key"
                :event_id="event_id"
              />
              <SoccerGameAction
                v-else-if="action.team === opp_keyword"
                align="center"
                justify="center"
                :action_type="action.action_type"
                :message="action.text"
                :athlete_number="
                  findAthleteNumber(action.athlete_id, oppRoster)
                "
                :athlete_name="findAthleteName(action.athlete_id, 'opponent')"
                :athlete_id="action.athlete_id"
                :athlete_img="action.athlete_img"
                :in_color="oppColor"
                :id="action.key"
                :event_id="event_id"
                :uprmAthletes="uprmRoster"
                :oppAthletes="oppRoster"
                team="Oponente"
              />
              <SoccerGameAction
                v-else
                align="center"
                justify="center"
                :action_type="action.action_type"
                :message="action.text"
                :athlete_number="
                  findAthleteNumber(action.athlete_id, uprmRoster)
                "
                :athlete_name="findAthleteName(action.athlete_id, 'uprm')"
                :athlete_img="findAthleteImg(action.athlete_id, uprmRoster)"
                :athlete_id="action.athlete_id"
                :in_color="uprm_color"
                :id="action.key"
                :event_id="event_id"
                :uprmAthletes="uprmRoster"
                :oppAthletes="oppRoster"
                team="UPRM"
              />
            </v-container>
          </v-tab-item>

          <v-tab-item>
            <v-spacer />
            <v-container>
              <v-tabs centered :color="uprm_color">
                <v-tabs-slider :color="uprm_color" />

                <v-tab>{{ uprm_team_name }}</v-tab>
                <v-tab>{{ opponentName }}</v-tab>
                <v-tab-item>
                  <SoccerStatistics :soccer_stats="uprmStatistics" />
                </v-tab-item>
                <v-tab-item>
                  <SoccerStatistics :soccer_stats="oppStatistics" />
                </v-tab-item>
              </v-tabs>
            </v-container>
          </v-tab-item>
          <v-tab-item>
            <v-spacer />
            <v-container>
              <v-tabs centered :color="uprm_color">
                <v-tabs-slider :color="uprm_color" />
                <v-tab>{{ uprm_team_name }}</v-tab>
                <v-tab>{{ opponentName }}</v-tab>
                <v-tab-item>
                  <v-data-table
                    dense
                    :headers="statistics_headers"
                    :items="uprmAthleteStatistics"
                    item-key="12344"
                    class="elevation-1"
                    :loading="loading"
                    loading-text="Cargando Estadísticas..."
                    no-data-text="No Se Encontraron Resultados"
                  />
                </v-tab-item>
                <v-tab-item>
                  <v-data-table
                    dense
                    :headers="statistics_headers"
                    :items="oppAthleteStatistics"
                    item-key="12345"
                    class="elevation-1"
                    :loading="loading"
                    loading-text="Cargando Estadísticas..."
                    no-data-text="No Se Encontraron Resultados"
                  />
                </v-tab-item>
              </v-tabs>
            </v-container>
          </v-tab-item>
        </v-tabs>
      </v-container>
      <v-dialog v-model="notification_dialog" persistent max-width="600px">
        <v-form ref="create_form">
          <v-card>
            <v-card-title>
              <span class="headline">Enviar Notificación</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-row allign="center">
                  <v-col>
                    <v-text-field
                      label="Texto de notificación *"
                      required
                      v-model="notification_text"
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
              <v-btn color="gray darken-3" text @click="reset_notification()"
                >Cerrar</v-btn
              >
              <v-btn
                color="primary darken-1"
                :loading="button_loading"
                text
                @click.native="send_notification()"
                >Enviar</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>
      <v-dialog v-model="end_pbp_dialog" persistent max-width="350">
        <v-card>
          <v-card-title class="text-center" style="word-break: normal;"
            >Terminar Secuencia de Jugadas</v-card-title
          >
          <v-card-text class="subtitle-1" style="word-break: normal;"
            >Terminar una secuencia de jugadas es irreversible. ¿Aún que desea
            terminar la secuencia de jugadas?</v-card-text
          >
          <v-row>
            <v-col>
              <v-checkbox
                v-model="terms"
                class="mx-2 text-center"
                style="word-break: normal;"
                label="He verificado el estado del juego.*"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="gray darken-3" text @click="clear_end_pbp()"
              >No</v-btn
            >
            <v-btn
              color="green darken-1"
              :disabled="!terms"
              text
              @click="startEndPBPSequence()"
              >Sí</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
      <v-dialog v-model="color_dialog" persistent max-width="300">
        <v-card>
          <v-card-title class="text-center" style="word-break: normal;"
            >Color del Equipo Oponente</v-card-title
          >
          <v-color-picker v-model="color" show-swatches></v-color-picker>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="gray darken-3" text @click="cancelColorUpdate()"
              >Cancelar</v-btn
            >
            <v-btn
              color="green darken-1"
              text
              :loading="button_loading"
              @click="updateColor()"
              >Guardar</v-btn
            >
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-card>
  </v-container>
</template>

<script>
import SoccerScore from "../../../components/SoccerScore";
import SoccerStatistics from "../../../components/SoccerStatistics";
import VolleyballScoreDisplayOnly from "../../../components/VolleyballScoreDisplayOnly";
import PBPRosterEntry from "../../../components/PBPRosterEntry";
import SoccerGameAction from "../../../components/SoccerGameAction";
import SoccerPBPActionsAdder from "../../../components/SoccerPBPActionsAdder";
import ErrorCard from "../../../components/PBP/ErrorCard";
import { mapGetters, mapActions } from "vuex";
export default {
  components: {
    SoccerScore,
    SoccerStatistics,
    VolleyballScoreDisplayOnly,
    PBPRosterEntry,
    SoccerGameAction,
    SoccerPBPActionsAdder,
    ErrorCard
  },
  data: () => ({
    loading: true,

    terms: false,

    invalid_event_dialog: false,
    no_pbp_dialog: false,
    invalid_sport_dialog: false,

    // Flag for controlling Error Card.
    init_error: false,
    // Strings for handling Error Card.
    error_header: "",
    error_message: "",

    // Header for statistics table (athletes).
    statistics_headers: [
      { text: "Número", value: "number", align: "center" },
      { text: "Nombre", value: "name", align: "center" },
      { text: "Goles", value: "Goal", align: "center" },
      { text: "Tiros a Portería", value: "GoalAttempt", align: "center" },
      { text: "Asistencias", value: "Assist", align: "center" },
      { text: "Atajadas", value: "Tackle", align: "center" },
      { text: "Faltas", value: "Foul", align: "center" },
      { text: "Tarjetas Amarillas", value: "YellowCard", align: "center" },
      { text: "Tarjetas Rojas", value: "RedCard", align: "center" }
    ],

    event_id: Number,
    end_pbp_dialog: false,
    color_dialog: false,
    prev_color: null,
    button_loading: false,
    notification_dialog: false,
    notification_text: "",
    notification_rules: [
      v =>
        (!!v && v.length > 0 && v.length <= 100) ||
        "Las notificaciones deben tener entre 1 y 100 caracteres."
    ],
    uprm_color: "primary",
    notification: "Notification",
    uprm_team_name: "uprm",
    opp_keyword: "opponent"
  }),
  methods: {
    sendAdjust(team_name, adjust_no) {
      payload = {
        team: team_name,
        action_type: "ScoreAdjust",
        adjust: adjust_no
      };
      console.log(payload);
    },
    // Functions for init/detach callbacks for maintaining data models based on Firebase updates.
    ...mapActions({
      getEvent: "soccerPBP/getEvent",
      getValidUPRMRoster: "soccerPBP/getValidUPRMRoster",
      handleSetScores: "soccerPBP/handleSetScores",
      handleCurrentSet: "soccerPBP/handleCurrentSet",
      handleUPRMRoster: "soccerPBP/handleUPRMRoster",
      handleOPPRoster: "soccerPBP/handleOPPRoster",
      handleGameOver: "soccerPBP/handleGameOver",
      handleOppColor: "soccerPBP/handleOppColor",
      handleGameActions: "soccerPBP/handleGameActions",
      detachSetScores: "soccerPBP/detachSetScores",
      detachCurrentSet: "soccerPBP/detachCurrentSet",
      detachUPRMRoster: "soccerPBP/detachUPRMRoster",
      detachOPPRoster: "soccerPBP/detachOPPRoster",
      detachGameOver: "soccerPBP/detachGameOver",
      detachOppColor: "soccerPBP/detachOppColor",
      detachGameActions: "soccerPBP/detachGameActions",
      sendGameAction: "soccerPBP/sendGameAction",
      endPBPSequence: "soccerPBP/endPBPSequence",
      clearPBPState: "soccerPBP/clearPBPState",
      updateOpponentColor: "soccerPBP/updateOpponentColor"
    }),
    startEndPBPSequence() {
      // Set payload format.
      const payload = {
        event_id: this.event_id
      };
      // Send request for ending a PBP sequence.
      this.endPBPSequence(payload);
      this.end_pbp_dialog = false;
    },
    findAthleteName(athlete_id, team) {
      let athlete_index = -1;
      let roster = [];
      // Set the right roster.
      if (team === "uprm") {
        roster = this.uprmRoster;
      } else if (team === "opponent") {
        roster = this.oppRoster;
      }
      // Iterate through each element in roster.
      for (let index in roster) {
        if (roster[index].key == "athlete-" + athlete_id) {
          athlete_index = index;
          continue;
        }
      }
      if (athlete_index === -1) {
        return "Atleta Desconocido";
      }
      // If athlete is opponent, just return its name.
      if (team === "opponent") {
        return roster[athlete_index].name;
      }
      // Otherwise, build its name using the structure established by Odin.
      let athlete_name = roster[athlete_index].first_name;
      if (roster[athlete_index].middle_name !== "") {
        athlete_name += " " + roster[athlete_index].middle_name;
      }
      athlete_name += " " + roster[athlete_index].last_names;
      return athlete_name;
    },
    on_notification_pressed() {
      this.notification_dialog = true;
    },

    clear_end_pbp() {
      this.terms = false;
      this.end_pbp_dialog = false;
    },

    async send_notification() {
      if (this.$refs.create_form.validate()) {
        const payload = {
          event_id: this.event_id,
          data: {
            message: this.notification_text,
            action_type: "Notification"
          }
        };
        this.button_loading = true;
        if (await this.sendGameAction(payload)) {
          this.$refs.create_form.reset();
          this.notification_dialog = false;
        }
        this.button_loading = false;
      }
    },
    reset_notification() {
      this.notification_dialog = false;
      this.$refs.create_form.reset();
    },
    findAthleteNumber(athlete_id, roster) {
      let athlete_index = -1;
      for (let index in roster) {
        if (roster[index].key == "athlete-" + athlete_id) {
          athlete_index = index;
          continue;
        }
      }
      if (athlete_index === -1) {
        return "?";
      }
      return roster[athlete_index].number;
    },
    findAthleteImg(athlete_id, roster) {
      let athlete_index = -1;
      for (let index in roster) {
        if (roster[index].key == "athlete-" + athlete_id) {
          athlete_index = index;
          continue;
        }
      }
      if (athlete_index === -1) {
        return "";
      }
      return roster[athlete_index].profile_image_link;
    },
    // Set up variables for color update dialog.
    startChooseColor() {
      this.prev_color = this.color;
      this.color_dialog = true;
    },
    // Rollback to previous color in case cancel was pressed.
    cancelColorUpdate() {
      this.color = this.prev_color;
      this.color_dialog = false;
    },
    // Send request to Odin.
    async updateColor() {
      const payload = {
        event_id: this.event_id,
        color: this.color.hexa
      };
      this.button_loading = true;
      if (await this.updateOpponentColor(payload)) {
        this.color_dialog = false;
      }
      this.button_loading = false;
    }
  },
  computed: {
    // Functions for getting values in the data models.
    ...mapGetters({
      uprmSets: "soccerPBP/uprmSets",
      oppSets: "soccerPBP/oppSets",
      currentUPRMSet: "soccerPBP/currentUPRMSet",
      currentOppSet: "soccerPBP/currentOppSet",
      currentSet: "soccerPBP/currentSet",
      uprmScore: "soccerPBP/uprmScore",
      oppScore: "soccerPBP/oppScore",
      uprmRoster: "soccerPBP/uprmRoster",
      oppRoster: "soccerPBP/oppRoster",
      gameOver: "soccerPBP/gameOver",
      oppColor: "soccerPBP/oppColor",
      gameActions: "soccerPBP/gameActions",
      uprmStatistics: "soccerPBP/uprmStatistics",
      oppStatistics: "soccerPBP/oppStatistics",
      uprmAthleteStatistics: "soccerPBP/uprmAthleteStatistics",
      oppAthleteStatistics: "soccerPBP/oppAthleteStatistics",
      sportName: "soccerPBP/sportName",
      hasPBP: "soccerPBP/hasPBP",
      teamId: "soccerPBP/teamId",
      validUPRMRoster: "soccerPBP/validUPRMRoster",
      branch: "soccerPBP/branch",
      opponentName: "soccerPBP/opponentName"
    })
  },
  async beforeMount() {
    this.loading = true;
    this.init_error = false;
    let event_id = this.$route.params.id;

    // Validate ID has been passed.
    if (!!!event_id) {
      this.error_header = "Error de Argumento";
      this.error_message = "No se envió un identificador de evento.";
      this.init_error = true;
      this.loading = false;
      return;
    }

    // Validate that the passed id is an unsigned integer.
    if (!!!event_id.match(/^-{0,1}\d+$/) || parseInt(event_id) < 0) {
      this.error_header = "Argumento Inválido";
      this.error_message =
        "El identificador del evento debe ser un entero sin signo.";
      this.init_error = true;
      this.loading = false;
      return;
    }

    this.event_id = parseInt(this.$route.params.id);
    // Validate a valid event_id was provided.
    if (await this.getEvent(this.event_id)) {
      this.getValidUPRMRoster(this.teamId);
      this.handleSetScores(this.event_id);
      this.handleCurrentSet(this.event_id);
      this.handleUPRMRoster(this.event_id);
      this.handleOPPRoster(this.event_id);
      this.handleGameOver(this.event_id);
      this.handleOppColor(this.event_id);
      this.handleGameActions(this.event_id);
      if (this.branch === "Masculino") {
        this.uprm_team_name = "Tarzanes";
      } else {
        this.uprm_team_name = "Juanas";
      }
      this.invalid_event_dialog = false;
    } else {
      this.error_header = "Error en la solicitud";
      this.error_message =
        "Esto puede ser debido a problemas de conexión o debido a que el evento provisto no se encuentre en el sistema.";
      this.init_error = true;
      this.loading = false;
      return;
    }
    // Validate the event has PBP functionality.
    if (this.hasPBP === false) {
      this.error_header = "Evento Inválido";
      this.error_message = "Este evento no tiene funcionalidad Play-by-Play.";
      this.init_error = true;
      this.loading = false;
    }

    // Validate the PBP sequence corresponds to Volleyball.
    if (this.sportName != "Futbol") {
      this.error_header = "Deporte Incorrecto";
      this.error_message =
        "Este deporte no está cubierto bajo la funcionalidad de Play-by-Play.";
      this.init_error = true;
      this.loading = false;
      return;
    }

    // All good at this point, so it is just needed to stop to loading animation.
    this.loading = false;
  },

  watch: {
    $route(to, from) {
      this.detachSetScores(this.event_id);
      this.detachCurrentSet(this.event_id);
      this.detachUPRMRoster(this.event_id);
      this.detachOPPRoster(this.event_id);
      this.detachGameOver(this.event_id);
      this.detachOppColor(this.event_id);
      this.detachGameActions(this.event_id);
      this.clearPBPState();
    }
  },
  beforeDestroy() {
    this.detachSetScores(this.event_id);
    this.detachCurrentSet(this.event_id);
    this.detachUPRMRoster(this.event_id);
    this.detachOPPRoster(this.event_id);
    this.detachGameOver(this.event_id);
    this.detachOppColor(this.event_id);
    this.detachGameActions(this.event_id);
    this.clearPBPState();
  }
};
</script>
