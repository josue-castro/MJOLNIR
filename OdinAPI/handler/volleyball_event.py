from flask import jsonify
from .dao.volleyball_event_dao import VolleyballEventDAO
from .dao.final_score_dao import FinalScoreDAO
#from .dao.event import EventDAO
#from .dao.team import TeamDAO
#from .dao.athlete import AthleteDAO
from .event_result import EventResultHandler
# TODO: REMOVE FOR FULL VERSIONS
# MOCK IMPLEMENTATIONS OF DAO
from .dao.event_dao import EventDAO
from .dao.team_dao import TeamDAO
from .dao.athlete_dao import AthleteDAO

# CONSTANTS:
VOLLEYBALL_IDM = 2
VOLLEYBALL_IDF = 12


class VolleyballEventHandler(EventResultHandler):

    # getAllStatisticsByVolleyballEventID(eID)//Instantiates a Volleyball Event DAO in order to complete the desired get request and it returns a JSON with the desired information or with an error message.
    # getAllAthleteStatisticsByVolleyballEventId(eID,aID)//Instantiates a Volleyball Event DAO in order to complete the desired get request and it returns a JSON with the desired information or with an error message
    # addStatistics(eID, aID, attributes)//Instantiates a Volleyball Event DAO in order to complete the desired post request and it returns a JSON with either a confirmation or error message.
    # editStatistics(eID, aID,attributes)//Instantiates a Volleyball Event DAO in order to complete the desired put request and it returns a JSON with either a confirmation or error message.
    # removesStatistics(eID, aID)//Instantiates a Volleyball Event DAO in order to complete the desired put request and it returns a JSON with either a confirmation or error message.
    # mapEventToDict(record)//Maps a Volleyball Event record to a dictionary and returns it.

    # ===========================//DICTIONARY MAPPERS//==================================
    # TODO: need to label somehow the jsonify/request in the route so that it has the sport?
    def mapEventToDict(self, record):
        athlete_info = {}
        stat_info = {}
        event_info = {}

        athlete_info['athlete_id'] = record[0]
        athlete_info['first_name'] = record[1]
        athlete_info['middle_name'] = record[2]
        athlete_info['last_names'] = record[3]
        athlete_info['number'] = record[4]
        athlete_info['profile_image_link'] = record[5]

        event_info['event_id'] = record[16]
        event_info['volleyball_event_id'] = record[17]

        stat_info['kill_points'] = record[6]
        stat_info['attack_errors'] = record[7]
        stat_info['assists'] = record[8]
        stat_info['aces'] = record[9]
        stat_info['service_errors'] = record[10]
        stat_info['digs'] = record[11]
        stat_info['blocks'] = record[12]
        stat_info['blocking_errors'] = record[13]
        stat_info['reception_errors'] = record[14]
        stat_info['blocking_points'] = record[15]

        result = dict(athlete=athlete_info, event_info=event_info,
                      event_statistics=stat_info)
        return result

    # For Specific Athlete Event Info
    def mapEventAthleteStatsToDict(self, record):
        stat_info = {}
        event_info = {}

        stat_info['kill_points'] = record[0]
        stat_info['attack_errors'] = record[1]
        stat_info['assists'] = record[2]
        stat_info['aces'] = record[3]
        stat_info['service_errors'] = record[4]
        stat_info['digs'] = record[5]
        stat_info['blocks'] = record[6]
        stat_info['blocking_errors'] = record[7]
        stat_info['reception_errors'] = record[8]
        stat_info['blocking_points'] = record[9]

        event_info['event_id'] = record[10]
        event_info['volleyball_event_id'] = record[11]
        event_info['athlete_id'] = record[12]

        #result = dict(Event_Statistics = stat_info)
        return dict(event_info=event_info, event_statistics=stat_info)

    # for team statistics
    def mapEventTeamStatsToDict(self, record):
        stat_info = {}
        event_info = {}

        stat_info['kill_points'] = record[0]
        stat_info['attack_errors'] = record[1]
        stat_info['assists'] = record[2]
        stat_info['aces'] = record[3]
        stat_info['service_errors'] = record[4]
        stat_info['digs'] = record[5]
        stat_info['blocks'] = record[6]
        stat_info['blocking_errors'] = record[7]
        stat_info['reception_errors'] = record[8]
        stat_info['blocking_points'] = record[9]

        event_info['event_id'] = record[10]
        event_info['volleyball_event_id'] = record[11]

        #result = dict(Event_Statistics = stat_info)
        return dict(event_info=event_info, event_statistics=stat_info)
        # UPRM_Score = final_record[0], Opponent_Score = final_record[1]

    def mapEventSeasonCollectionToDict(self, record):
        event_info = {}
        stat_info = {}

        event_info['event_id'] = record[0]
        event_info['event_date'] = record[1]
        event_info['volleyball_event_id'] = record[11]
        event_info['athlete_id'] = record[12]

        stat_info['kill_points'] = record[2]
        stat_info['attack_errors'] = record[3]
        stat_info['assists'] = record[4]
        stat_info['aces'] = record[5]
        stat_info['service_errors'] = record[6]
        stat_info['digs'] = record[7]
        stat_info['blocks'] = record[8]
        stat_info['blocking_errors'] = record[9]
        stat_info['reception_errors'] = record[10]
        stat_info['blocking_points'] = record[11]

        result = dict(Event=event_info, Event_Statistics=stat_info)
        return result

    def mapAthleteSeasonAggregate(self, record):
        athlete_info = {}
        stat_info = {}

        athlete_info['athlete_id'] = record[10]
        athlete_info['first_name'] = record[11]
        athlete_info['middle_name'] = record[12]
        athlete_info['last_names'] = record[13]
        athlete_info['number'] = record[14]
        athlete_info['profile_image_link'] = record[15]

        stat_info['kill_points'] = record[0]
        stat_info['attack_errors'] = record[1]
        stat_info['assists'] = record[2]
        stat_info['aces'] = record[3]
        stat_info['service_errors'] = record[4]
        stat_info['digs'] = record[5]
        stat_info['blocks'] = record[6]
        stat_info['blocking_errors'] = record[7]
        stat_info['reception_errors'] = record[8]
        stat_info['blocking_points'] = record[9]

        result = dict(Athlete=athlete_info, Event_Statistics=stat_info)
        return result

    def mapTeamSeasonAggregate(self, record):
        stat_info = {}

        stat_info['kill_points'] = record[0]
        stat_info['attack_errors'] = record[1]
        stat_info['assists'] = record[2]
        stat_info['aces'] = record[3]
        stat_info['service_errors'] = record[4]
        stat_info['digs'] = record[5]
        stat_info['blocks'] = record[6]
        stat_info['blocking_errors'] = record[7]
        stat_info['reception_errors'] = record[8]
        stat_info['blocking_points'] = record[9]
        

        result = dict(team_id=record[10], Event_Statistics=stat_info)
        return result


# { "event_id": 5,
#   "team_statistics":
#    { "volleyball_statistics":
#         {
#         "kill_points": 1,
#         "attack_errors":1,
#         "assists":1,
#         "aces":1,
#         "service_errors":1,
#         "digs":1,
#         "blocks":1,
#         "blocking_errors":1,
#         "reception_errors":1,
#         "blocking_points":1
#         }
#    },
#   "athlete_statistics":
#   [
#   	{"athlete_id":4,
#   	"statistics":
# 	  	{"volleyball_statistics":
# 		  	{
#             "kill_points": 1,
#             "attack_errors":1,
#             "assists":1,
#             "aces":1,
#             "service_errors":1,
#             "digs":1,
#             "blocks":1,
#             "blocking_errors":1,
#             "reception_errors":1,
#             "blocking_points":1
# 		  	}
# 	  	}
#   	},


    def mapEventAllStatsToDict(self, team_record, athlete_records, final_record):
        if team_record:
            event_info = dict(
                event_id=team_record[10],
                volleyball_event_team_stats_id=team_record[11]
                # event_date = team_record[17]
            )
            volleyball_statistics = dict(
                kill_points=team_record[0],
                attack_errors=team_record[1],
                assists=team_record[2],
                aces=team_record[3],
                service_errors=team_record[4],
                digs=team_record[5],
                blocks=team_record[6],
                blocking_errors=team_record[7],
                reception_errors=team_record[8],
                blocking_points=team_record[9]
            )
            team_statistics = dict(volleyball_statistics=volleyball_statistics)
        else:
            event_info = dict(event_id=None,volleyball_event_team_stats_id=None)
            team_statistics = None
    
        # mappedResult = []
        # for athlete_statistics in result:
        #     mappedResult.append(self.mapEventToDict(athlete_statistics))
        # return jsonify(Volleyball_Event = mappedResult), 200

        athlete_statistics = []
        for athlete_record in athlete_records:
            athlete_info = dict(
                athlete_id=athlete_record[0],
                first_name=athlete_record[1],
                middle_name=athlete_record[2],
                last_names=athlete_record[3],
                number=athlete_record[4],
                profile_image_link=athlete_record[5],
                volleyball_event_id=athlete_record[17]
            )
            statistics = dict(
                kill_points=athlete_record[6],
                attack_errors=athlete_record[7],
                assists=athlete_record[8],
                aces=athlete_record[9],
                service_errors=athlete_record[10],
                digs=athlete_record[11],
                blocks=athlete_record[12],
                blocking_errors=athlete_record[13],
                reception_errors=athlete_record[14],
                blocking_points=athlete_record[15]
            )

            athlete_statistics.append(
                dict(athlete_info=athlete_info, statistics=statistics))

        result = dict(event_info=event_info, team_statistics=team_statistics,
                      athlete_statistic=athlete_statistics, uprm_score=final_record[0],
                      opponent_score=final_record[1])
        return result

# ===========================//HANDLERS//==================================


# ===========================//I.GETS//====================================

    # TODO: Validation - For add/updates, validate the len(attributes), same as previous len(form)

    def getAllAthleteStatisticsByEventId(self, eID, aID):
        """
        Gets all the statistics for a given event and athlete. 

        Calls the VolleyballEventDAO to get event statistics and maps the result to
        to a JSON that contains all the statistics for that athlete and event in the system. That
        JSON object is then returned.

        Args:
            eID: The ID of the event of which statistics need to be fetched.
            aID: The ID of the athlete of which statistics need to be fetched

        Returns:
            A JSON containing all the statistics in the system for the specified event and athlete.
        """

        # validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # validate existing athlete

        try:
            a_dao = AthleteDAO()
            athlete = a_dao.athleteExists(aID)
            if not athlete:
                return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

        # validate existing volleyball_event entry and format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.getAllAthleteStatisticsByEventID(eID, aID)
            if not result:
                return jsonify(Error="Estadisticas de Evento de Voleibol no se encontro para el evento con ID:{} y atleta con ID:{}.".format(eID, aID)), 404
            mappedResult = self.mapEventAthleteStatsToDict(result)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500
        return jsonify(Volleyball_Event_Athlete_Statistics=mappedResult), 200

    def getAllTeamStatisticsByEventId(self, eID):
        """
        Gets all the statistics for a given event. 

        Calls the VolleyballEventDAO to get event team statistics and maps the result to
        to a JSON that contains all the team statistics for that event in the system. That
        JSON object is then returned.

        Args:
            eID: The ID of the event of which team statistics need to be fetched.

        Returns:
            A JSON containing all the team statistics in the system for the specified event.
        """

        # validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # validate existing volleyball_event entry and format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.getAllTeamStatisticsByEventID(eID)
            if not result:
                return jsonify(Error="Estadisticas de Equipo para Evento de Voleibol  no se encontraron para el Evento con ID:{}.".format(eID)), 404
            mappedResult = self.mapEventTeamStatsToDict(result)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

        return jsonify(Volleyball_Event_Team_Stats=mappedResult), 200

    def getAllAthleteStatisticsPerSeason(self, aID, seasonYear):
        """
        Gets all the statistics for a given athlete during a given season. 

        Calls the VolleyballEventDAO to get event statistics and maps the result to
        to a JSON that contains all the statistics for that athlete during the given season
        in the system. That JSON object is then returned.

        Args:
            seasonYear: the season year of which statistics need to be fetched
            aID: The ID of the athlete of which statistics need to be fetched

        Returns:
            A JSON containing all the statistics in the system for the specified athlete and season year.
        """

        # validate existing athlete

        try:
            a_dao = AthleteDAO()
            athlete = a_dao.athleteExists(aID)
            if not athlete:
                return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

        # validate existing volleyball_event entries and format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.getAllAthleteStatisticsPerSeason(aID, seasonYear)
            if not result:
                return jsonify(Error="No se encontraron Estadisticas de Evento de Voleibol para atleta con ID:{} con año de temproada:{}.".format(aID, seasonYear)), 404
            mappedResult = []
            for athlete_statistics in result:
                mappedResult.append(
                    self.mapEventSeasonCollectionToDict(athlete_statistics))
            # print(mappedResult)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        return jsonify(Volleyball_Event_Season_Athlete_Statistics=mappedResult), 200

    # NEW
    def getAggregatedAthleteStatisticsPerSeason(self, aID, seasonYear):
        """
        Gets aggregated statistics for a given athlete during a given season. 

        Calls the VolleyballEventDAO to get aggregated event statistics and maps the result to
        to a JSON that contains all the statistics for that athlete during the given season
        in the system. That JSON object is then returned.

        Args:
            seasonYear: the season year of which statistics need to be fetched
            aID: The ID of the athlete of which statistics need to be fetched

        Returns:
            A JSON containing aggregated  statistics in the system for the specified athlete and season year.
        """

        # validate existing athlete

        try:
            a_dao = AthleteDAO()
            athlete = a_dao.athleteExists(aID)
            if not athlete:
                return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

        # validate existing volleyball_event entries and format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.getAggregatedAthleteStatisticsPerSeason(
                aID, seasonYear)
            if not result:
                return jsonify(Error="No se encontraron Estadisticas de Evento de Voleibol para atleta con ID:{} con año de temproada:{}.".format(aID, seasonYear)), 404
            mappedResult = self.mapAthleteSeasonAggregate(result)
            # print(mappedResult)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        return jsonify(Volleyball_Event_Season_Athlete_Statistics=mappedResult), 200

    # NEW
    def getAllAggregatedAthleteStatisticsPerSeason(self, sID, seasonYear):
        """
        Gets all aggregated statistics for athletes during a given season. 

        Calls the VolleyballEventDAO to get  all aggregated event statistics and maps the result to
        to a JSON that contains all the aggregated statistics  during the given season
        in the system. That JSON object is then returned.

        Args:
            seasonYear: the season year of which statistics need to be fetched
            sID: The ID of the sport of which statistics need to be fetched

        Returns:
            A JSON containing all the aggregated statistics in the system for the specified sport and season year.
        """

        # validate existing volleyball_event entries and format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.getAllAggregatedAthleteStatisticsPerSeason(
                sID, seasonYear)
            if not result:
                return jsonify(Error="No se encontraron Estadisticas de Evento de Voleibol para deporte con ID:{} con año de temproada:{}.".format(sID, seasonYear)), 404
            mappedResult = []
            for athlete_statistics in result:
                mappedResult.append(
                    self.mapAthleteSeasonAggregate(athlete_statistics))
            # print(mappedResult)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        return jsonify(Volleyball_Event_Season_Athlete_Statistics=mappedResult), 200

    # NEW
    def getAggregatedTeamStatisticsPerSeason(self, sID, seasonYear):
        """
        Gets all aggregated statistics for a given team during a season.  

        Calls the VolleyballEventDAO to get  all aggregated event statistics and maps the result to
        to a JSON that contains all the statistics for that athlete during the given season
        in the system. That JSON object is then returned.

        Args:
            seasonYear: the season year of which statistics need to be fetched
            sID: The ID of the sport of which team statistics need to be fetched

        Returns:
            A JSON containing the aggregated team statistics in the system for the specified team and season year.
        """

        # validate existing volleyball_event entries and format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.getAggregatedTeamStatisticsPerSeason(sID, seasonYear)
            if not result:
                return jsonify(Error="No se encontraron Estadisticas de Equipo paraEvento de Voleibol para deporte con ID:{} con año de temproada:{}.".format(sID, seasonYear)), 404
            mappedResult = []
            mappedResult = self.mapTeamSeasonAggregate(result)
            # print(mappedResult)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para eventos de voleibol desde el DAO."), 500

        return jsonify(Volleyball_Event_Season_Team_Statistics=mappedResult), 200

    # NEW get ALL the statistics for a given event be it team or individual
    # TODO: naming is confusign with the top function

    def getAllStatisticsByEventID(self, eID):
        """
        Gets all the team and individual statistics for a given event. 

        Calls the VolleyballEventDAO to get event statistics and maps the result to
        to a JSON that contains all the statistics for that event in the system. 
        That JSON object is then returned.

        Args:
            eID: The ID of the event of which statistics need to be fetched

        Returns:
            A JSON containing all the statistics in the system for the specified event.
        """

        # validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        try:
            dao = VolleyballEventDAO()
            team_result = dao.getAllTeamStatisticsByEventID(eID)
            # if not team_result:
            #     return jsonify(Error="Estadisticas de Equipo para Evento de Voleibol  no se encontraron para el Evento con ID:{}.".format(eID)), 404
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo. (TEAM STATS)"), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para eventos de voleibol desde el DAO."), 500

        try:
            all_stats_result = dao.getAllStatisticsByEventID(eID)
            # if not all_stats_result:
            #     return jsonify(Error="Estadisticas de Evento de Voleibol no se encontro para evento con ID:{}.".format(eID)), 404
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo. (ALL STATS)"), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        try:
            fs_dao = FinalScoreDAO()
            final_score_result = fs_dao.getFinalScore(eID)
            if not final_score_result:
            #     return jsonify(Error = "Volleyball Event Statistics not found for the event: {}.".format(eID)),404
                final_score_result = [None, None]
            mappedResult = self.mapEventAllStatsToDict(
                team_result, all_stats_result, final_score_result)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo. (FINAL SCORE)"), 400
        except:
            return jsonify(ERROR="No se pudo verificar puntuacion final desde el DAO."), 500

        return jsonify(Volleyball_Event_Statistics=mappedResult), 200

# ===========================//II.POSTS//====================================
    # Instantiates a Volleyball Event DAO in order to complete the desired post request and it returns a JSON with either a confirmation or error message.
    def addStatistics(self, eID, aID, attributes):
        """
        Adds a new statistics record with the provided information.

        Calls the BastketballEventDAO to add a new statistics record and maps the result to
        to a JSON that contains the desired record. That JSON object 
        is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be added.
            aID: the ID of the athlete for which the statistics record will be added.
            attributes:
                kill_points:
                attack_errors:
                assists:
                aces:
                service_errors:
                digs:
                blocks:
                blocking_errors:
                reception_errors:
                blocking_points:

        Returns:
            A JSON containing the id for the new Volleyball Event record.
        """

        # Validate Avoid Duplication

        try:
            dao = VolleyballEventDAO()
            if dao.getVolleyballEventID(eID, aID):
                # TODO: Use 403 for duplicates
                return jsonify(Error="Entrada de Evento de Voleibol ya existe para Evento con ID:{} y Atleta con ID:{}".format(eID, aID)), 403
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500
        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Get Event Team For Validation

        # TODO: (Luis) Need EventDAO method to obtain team ID
        try:
            e_dao = EventDAO()
            tID = e_dao.getEventTeamByID(eID)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Validate that the event belongs to the correct sport.
        # TODO: (Herbert) Need TeamDAO to return sport_id of a team.
        try:
            t_dao = TeamDAO()
            sID = t_dao.getTeamSportByID(tID)[0]
            if sID != VOLLEYBALL_IDF and sID != VOLLEYBALL_IDM:
                return jsonify(Error="Query Malformado, Evento con ID:{} no pertenece a Voleibol.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # Validate existing athlete

        try:
            a_dao = AthleteDAO()
            athlete = a_dao.athleteExists(aID)
            if not athlete:
                return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

        # Validate athlete belongs to team playing event
        # TODO: (Herbert) Need TeamDAO method to get a team_member record to validate team membership. Could be a Boolean
        try:
            # alternatively: t_dao.athleteBelongsToTeam(aID,tID)
            if not t_dao.getTeamMemberByIDs(aID, tID):
                return jsonify(Error="Query Malformado, Atleta con ID:{} no pertenece a el Equipo con ID:{} de el Evento con ID:{}.".format(aID, tID, eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # check if existing invalid, in this case we PUT/update instead of POST/add. sorta.
        invalid_duplicate = False
        try:
            if dao.getVolleyballEventIDInvalid(eID, aID):
                invalid_duplicate = True
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        # the case of there already existing an entry, but marked as invalid
        if invalid_duplicate:
            try:
                result = dao.editStatistics(eID, aID, attributes['kill_points'], attributes['attack_errors'], attributes['assists'], attributes['aces'],
                                            attributes['service_errors'], attributes['digs'], attributes['blocks'], attributes['blocking_errors'], attributes['reception_errors'], attributes['blocking_points'])
                if not result:
                    return jsonify(Error="Record de Estadisticas no se encontro para atleta con ID:{} en evento con id:{}.".format(aID, eID)), 404

            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500
        else:
            # Create and Validate new Volleyball_Event
            try:
                result = dao.addStatistics(eID, aID, attributes['kill_points'], attributes['attack_errors'], attributes['assists'], attributes['aces'],
                                           attributes['service_errors'], attributes['digs'], attributes['blocks'], attributes['blocking_errors'], attributes['reception_errors'], attributes['blocking_points'])
                if not result:
                    return jsonify(Error="Problema insertando nuevo record de estadisticas."), 500
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        # update and validate Volleyball Event Team Statistic
        # If existing Team Statistics update, else create
        try:
            if dao.getVolleyballEventTeamStatsID(eID) or dao.getVolleyballEventTeamStatsIDInvalid(eID):
                team_result = dao.editTeamStatistics(eID)
                if not team_result:
                    return jsonify(Error="Record de Estadisticas de Equipo no se encontro para Evento con ID:{}.".format(eID)), 404
            else:
                dao.addTeamStatistics(eID, attributes['kill_points'], attributes['attack_errors'], attributes['assists'], attributes['aces'],
                                      attributes['service_errors'], attributes['digs'], attributes['blocks'], attributes['blocking_errors'], attributes['reception_errors'], attributes['blocking_points'])
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO.."), 500

        if invalid_duplicate:
            mappedResult = self.mapEventAthleteStatsToDict(result)
            dao.commitChanges()
            return jsonify(Volleyball_Event_Athlete_Statistics=mappedResult), 200
        else:
            dao.commitChanges()
            return jsonify(Volleyball_Event_Athlete_Statistics="Se añadio nuevo record de estadisticas con ID:{} para atleta con ID:{} en evento con ID:{}.".format(result, aID, eID)), 201

    # NEW
    # Instantiates a Volleyball Event DAO in order to complete the desired post request and it returns a JSON with either a confirmation or error message.
    def addTeamStatistics(self, eID, attributes):
        """
        Adds a new team statistics record with the provided information.

        Calls the BastketballEventDAO to add a new team statistics record and maps the result to
        to a JSON that contains the desired record. That JSON object 
        is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be added.
            attributes:
                kill_points:
                attack_errors:
                assists:
                aces:
                service_errors:
                digs:
                blocks:
                blocking_errors:
                reception_errors:
                blocking_points:

        Returns:
            A JSON containing the id for the new Volleyball Event team statistics record.
        """

        # Validate Avoid Duplication

        try:
            dao = VolleyballEventDAO()
            if dao.getVolleyballEventTeamStatsID(eID):
                return jsonify(Error="Entrada de Estadisticas de Evento de Equipo ya existe para evento con ID:{}.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Get Event Team For Validation

        # TODO: (Luis) Need EventDAO method to obtain team ID
        try:
            e_dao = EventDAO()
            tID = e_dao.getEventTeamByID(eID)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # Validate that the event belongs to the correct sport.
        # TODO: (Herbert) Need TeamDAO to return sport_id of a team.
        try:
            t_dao = TeamDAO()
            sID = t_dao.getTeamSportByID(tID)[0]
            if sID != VOLLEYBALL_IDF and sID != VOLLEYBALL_IDM:
                return jsonify(Error="Query Malformado, Evento con ID:{} no pertenece a Voleibol.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # check if existing invalid, in this case we PUT/update instead of POST/add. sorta.
        invalid_duplicate = False
        try:
            if dao.getVolleyballEventTeamStatsIDInvalid(eID):
                invalid_duplicate = True
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500
        # the case of there already existing an entry, but marked as invalid
        if invalid_duplicate:
            try:
                result = dao.editTeamStatisticsManual(eID, attributes['kill_points'], attributes['attack_errors'], attributes['assists'], attributes['aces'],
                                                      attributes['service_errors'], attributes['digs'], attributes['blocks'], attributes['blocking_errors'], attributes['reception_errors'], attributes['blocking_points'])
                if not result:
                    return jsonify(Error="Record de Estadisticas de Equipo no se encontro para evento con id:{}.".format(eID)), 404
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

            mappedResult = self.mapEventTeamStatsToDict(result)
            dao.commitChanges()
            return jsonify(Volleyball_Event_Team_Stats=mappedResult), 200
        else:
            # Create and Validate new Volleyball_Event team stats
            try:
                result = dao.addTeamStatistics(eID, attributes['kill_points'], attributes['attack_errors'], attributes['assists'], attributes['aces'],
                                               attributes['service_errors'], attributes['digs'], attributes['blocks'], attributes['blocking_errors'], attributes['reception_errors'], attributes['blocking_points'])
                if not result:
                    return jsonify(Error="Problema insertando nuevo record de estadisticas de equipo."), 500
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

            dao.commitChanges()
            return jsonify(Volleyball_Event_Team_Stats="Se añadio nuevo record de estadisticas de equipo con ID:{} para evento con ID:{}".format(result, eID)), 201

    # NEW
    # Instantiates a Volleyball Event DAO in order to complete the desired post request and it returns a JSON with either a confirmation or error message.
    def addTeamStatisticsAuto(self, eID):
        """
        Adds a new team statistics record with the provided information and an aggregate of existing information.

        Calls the BastketballEventDAO to add a new team statistics record and maps the result to
        to a JSON that contains the desired record. That JSON object 
        is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be added.

        Returns:
            A JSON containing  the id for the new Volleyball Event team statistics record.
        """

        # Validate Avoid Duplication

        try:
            dao = VolleyballEventDAO()
            if dao.getVolleyballEventTeamStatsID(eID):
                return jsonify(Error="Entrada de Estadisticas de Evento de Equipo ya existe para evento con ID:{}.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Get Event Team For Validation

        # TODO: (Luis) Need EventDAO method to obtain team ID
        try:
            e_dao = EventDAO()
            tID = e_dao.getEventTeamByID(eID)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # Validate that the event belongs to the correct sport.
        # TODO: (Herbert) Need TeamDAO to return sport_id of a team.
        try:
            t_dao = TeamDAO()
            sID = t_dao.getTeamSportByID(tID)[0]
            if sID != VOLLEYBALL_IDF and sID != VOLLEYBALL_IDM:
                return jsonify(Error="Query Malformado, Evento con ID:{} no pertenece a Voleibol.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # check if existing invalid, in this case we PUT/update instead of POST/add. sorta.
        invalid_duplicate = False
        try:
            if dao.getVolleyballEventTeamStatsIDInvalid(eID):
                invalid_duplicate = True
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500
        # the case of there already existing an entry, but marked as invalid
        if invalid_duplicate:
            try:
                result = dao.editTeamStatistics(eID)
                if not result:
                    return jsonify(Error="Record de Estadisticas de Equipo no se encontro para Evento con ID:{}.".format(eID)), 404
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

            mappedResult = self.mapEventTeamStatsToDict(result)
            dao.commitChanges()
            return jsonify(Volleyball_Event_Team_Stats=mappedResult), 200
        else:
            # Create and Validate new Volleyball_Event team stats
            try:
                result = dao.addTeamStatisticsAuto(eID)
                if not result:
                    return jsonify(Error="Problema insertando nuevo record de estadisticas de equipo."), 500
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar estadisticas de equipo para eventos de voleibol desde el DAO."), 500
            dao.commitChanges()
            return jsonify(Volleyball_Event_Team_Stats="Se añadio nuevo record de estadisticas de equipo con ID:{} para evento con ID:{}".format(result, eID)), 201

    # NEW: the mega query
    def addAllEventStatistics(self, eID, attributes):
        """
        Adds new statistics records with the provided information.

        Calls the BastketballEventDAO to add new statistics records and maps the result to
        to a JSON that contains the desired records. That JSON object 
        is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be added.
            team_statistics: the IDs of the athletes for which the statistics record will be added.
            Attributes:
                Athlete Statistics:
                   kill_points:
                    attack_errors:
                    assists:
                    aces:
                    service_errors:
                    digs:
                    blocks:
                    blocking_errors:
                    reception_errors:
                    blocking_points:
                team_statistis:
                    kill_points:
                    attack_errors:
                    assists:
                    aces:
                    service_errors:
                    digs:
                    blocks:
                    blocking_errors:
                    reception_errors:
                    blocking_points:
                local_score: the final score for the local uprm team
                opponent_score: the final score for the opponent team


        Returns:
            A JSON the id for the new Volleyball Event record.
        """
        team_statistics = attributes['team_statistics']['volleyball_statistics']
        athlete_statistics = attributes['athlete_statistics']
        local_score = attributes['uprm_score']
        opponent_score = attributes['opponent_score']

        # Validate Avoid Duplication Team Stats
        try:
            dao = VolleyballEventDAO()
            if dao.getVolleyballEventTeamStatsID(eID):
                return jsonify(Error="Entrada de Estadisticas de Evento de Equipo ya existe para evento con ID:{}.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para eventos de voleibol desde el DAO."), 500

        # Validate Avoid Duplication Final Score
        try:
            fs_dao = FinalScoreDAO()
            if fs_dao.getFinalScore(eID):
                return jsonify(Error="Entrada de Puntuacion Final ya existe para Evento con ID:{}.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar puntuacion final desde el DAO."), 500

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Get Event Team For Validation

        # TODO: (Luis) Need EventDAO method to obtain team ID
        try:
            e_dao = EventDAO()
            tID = e_dao.getEventTeamByID(eID)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # Validate that the event belongs to the correct sport.
        # TODO: (Herbert) Need TeamDAO to return sport_id of a team.
        try:
            t_dao = TeamDAO()
            sID = t_dao.getTeamSportByID(tID)[0]
            if sID != VOLLEYBALL_IDF and sID != VOLLEYBALL_IDM:
                return jsonify(Error="Query Malformado, Evento con ID:{} no pertenece a Voleibol.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

        # Go through every set of athlete to add attributes for.
        for athlete_attributes in athlete_statistics:

            aID = athlete_attributes['athlete_id']
            try:
                # Validate Avoid Duplication Volleyball Event Entry
                if dao.getVolleyballEventID(eID, aID):
                    return jsonify(Error="Entrada de Evento de Voleibol ya existe para Evento con ID:{} y Atleta con ID:{}".format(eID, aID)), 400
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

            # Validate existing athlete
            statistics = athlete_attributes['statistics']['volleyball_statistics']

            try:
                a_dao = AthleteDAO()
                athlete = a_dao.athleteExists(aID)
                if not athlete:
                    return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

            # Validate athlete belongs to team playing event
            # TODO: (Herbert) Need TeamDAO method to get a team_member record to validate team membership. Could be a Boolean
            try:
                # alternatively: t_dao.athleteBelongsToTeam(aID,tID)
                if not t_dao.getTeamMemberByIDs(aID, tID):
                    return jsonify(Error="Query Malformado, Atleta con ID:{} no pertenece a el Equipo con ID:{} de el Evento con ID:{}.".format(aID, tID, eID)), 400
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar equipo desde el DAO."), 500

            # check if existing invalid, in this case we PUT/update instead of POST/add. sorta.
            invalid_duplicate = False
            try:
                if dao.getVolleyballEventIDInvalid(eID, aID):
                    invalid_duplicate = True
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

            # the case of there already existing an entry, but marked as invalid
            if invalid_duplicate:
                try:
                    result = dao.editStatistics(eID, aID, statistics['kill_points'], statistics['attack_errors'], statistics['assists'], statistics['aces'],
                                                statistics['service_errors'], statistics['digs'], statistics['blocks'], statistics['blocking_errors'], statistics['reception_errors'], statistics['blocking_points'])
                    if not result:
                        return jsonify(Error="Record de Estadisticas no se encontro para atleta con ID:{} en evento con id:{}.".format(aID, eID)), 404

                except (TypeError, ValueError):
                    return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
                except:
                    return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500
            else:
                # Create and Validate new Volleyball_Event
                try:
                    result = dao.addStatistics(eID, aID, statistics['kill_points'], statistics['attack_errors'], statistics['assists'], statistics['aces'],
                                               statistics['service_errors'], statistics['digs'], statistics['blocks'], statistics['blocking_errors'], statistics['reception_errors'], statistics['blocking_points'])
                    if not result:
                        return jsonify(Error="Problema insertando nuevo record de estadisticas."), 500
                except (TypeError, ValueError):
                    return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
                except:
                    return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

            # SUCCESS MESSAGE
            # return jsonify(Volleyball_Event_Athlete_Statistics = "Added new statistics record with id:{} for athlete id:{} in event id:{}.".format(result,aID,eID)),201
        # Check if existing invalid duplicate
        invalid_duplicate = False
        try:
            fs_dao = FinalScoreDAO()
            if fs_dao.getFinalScoreInvalid(eID):
                invalid_duplicate = True
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar puntuacion final desde el DAO."), 500

        # case with previously existing invalid entry, in that case update that entry
        if invalid_duplicate:
            try:
                result = fs_dao.editFinalScoreAltCursor(
                    eID, attributes['uprm_score'], attributes['opponent_score'], dao.getCursor())
                if not result:
                    return jsonify(Error="Record de Puntuacion Final no se encontro para evento con ID:{}.".format(eID)), 404
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar puntuacion final desde el DAO."), 500
        else:
            # Create and Validate Final Score entry
            try:
                result = fs_dao.addFinalScoreAltCursor(
                    eID, local_score, opponent_score, dao.getCursor())
                if not result:
                    return jsonify(Error="Problem inserting new final score record."), 500
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar puntuacion final desde el DAO."), 500

        # check if existing invalid, in this case we PUT/update instead of POST/add. sorta.
        invalid_duplicate = False
        try:
            if dao.getVolleyballEventTeamStatsIDInvalid(eID):
                invalid_duplicate = True
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500
        # the case of there already existing an entry, but marked as invalid
        if invalid_duplicate:
            try:
                result = dao.editTeamStatistics(eID)
                if not result:
                    return jsonify(Error="Record de Estadisticas de Equipo no se encontro para atleta con ID:{} en evento con id:{}.".format(aID, eID)), 404
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500
        else:
            # Create and Validate new Volleyball_Event team stats
            try:
                result = dao.addTeamStatistics(eID, team_statistics['kill_points'], team_statistics['attack_errors'], team_statistics['assists'], team_statistics['aces'],
                                               team_statistics['service_errors'], team_statistics['digs'], team_statistics['blocks'], team_statistics['blocking_errors'], team_statistics['reception_errors'], team_statistics['blocking_points'])
                if not result:
                    return jsonify(Error="Problema insertando nuevo record de estadisticas de equipo."), 500
            except (TypeError, ValueError):
                return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
            except:
                return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO.."), 500
        dao.commitChanges()
        return jsonify(Volleyball_Event_Team_Stats="Se añadio nuevo record de estadisticas de equipo con ID:{} y estadisticas individuales para evento con ID:{}".format(result, eID)), 201


# ===========================//III.PUTS//====================================

    # Instantiates a Volleyball Event DAO in order to complete the desired put request and it returns a JSON with either a confirmation or error message.

    def editStatistics(self, eID, aID, attributes):
        """
        Updates the statistics for the volleyball event with the given IDs.

        Calls the BasktballEventDAO to update the statistics of a volleyball event. It then
        maps the result to a JSON that contains the desired record. That JSON 
        object is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be updated.
            aID: the ID of the athlete for which the statistics record will be updated.
            attributes:
                kill_points:
                attack_errors:
                assists:
                aces:
                service_errors:
                digs:
                blocks:
                blocking_errors:
                reception_errors:
                blocking_points:

        Returns:
            A JSON containing all the user with the updated entry.
        """

        # Validate Exists in order to update

        try:
            dao = VolleyballEventDAO()
            # TODO: what is the error code for this case, where it DOESNT exit?
            if not dao.getVolleyballEventID(eID, aID):
                return jsonify(Error="Entrada de Evento de Voleibol no existe para Evento con ID:{} y Atleta con ID:{}.".format(eID, aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Validate existing athlete

        try:
            a_dao = AthleteDAO()
            athlete = a_dao.athleteExists(aID)
            if not athlete:
                return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

        # Update and Validate Volleyball event, format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.editStatistics(eID, aID, attributes['kill_points'], attributes['attack_errors'], attributes['assists'], attributes['aces'],
                                        attributes['service_errors'], attributes['digs'], attributes['blocks'], attributes['blocking_errors'], attributes['reception_errors'], attributes['blocking_points'])
            if not result:
                return jsonify(Error="Record de Estadisticas no se encontro para atleta con ID:{} en evento con id:{}.".format(aID, eID)), 404
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        # update and validate Volleyball Event Team Statistic
        try:
            team_result = dao.editTeamStatistics(eID)
            if not team_result:
                return jsonify(Error="Record de Estadisticas de Equipo no se encontro para Evento con ID:{}.".format(eID)), 404
            mappedResult = self.mapEventAthleteStatsToDict(result)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO.."), 500

        dao.commitChanges()
        return jsonify(Volleyball_Event_Athlete_Statistics=mappedResult), 200

    # Instantiates a Volleyball Event DAO in order to complete the desired put request and it returns a JSON with either a confirmation or error message.
    def editTeamStatistics(self, eID):
        """
        Updates the team statistics for the volleyball event with the given ID and aggregates of existing data.

        Calls the BasktballEventDAO to update the statistics of a volleyball event. It then
        maps the result to a JSON that contains the desired record. That JSON 
        object is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be updated.


        Returns:
            A JSON containing all the user with the updated entry.
        """

        # Validate exists so can update

        try:
            dao = VolleyballEventDAO()
            if not dao.getVolleyballEventTeamStatsID(eID):
                return jsonify(Error="Entrada de Estadisticas de Equipo para  Evento de Voleibol no existe para Evento con ID:{}.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Update and Validate Volleyball event team stats, format returnable

        try:
            dao = VolleyballEventDAO()
            result = dao.editTeamStatistics(eID)
            if not result:
                return jsonify(Error="Record de Estadisticas de Equipo no se encontro para Evento con ID:{}.".format(eID)), 404
            mappedResult = self.mapEventTeamStatsToDict(result)
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO.."), 500

        dao.commitChanges()
        return jsonify(Volleyball_Event_Team_Stats=mappedResult), 200

# ===========================//IV.REMOVE//====================================
    # Instantiates a Volleyball Event DAO in order to complete the desired put request and it returns a JSON with either a confirmation or error message.
    def removeStatistics(self, eID, aID):
        """
        Invalidates a statistics record in the database based on the given IDs.

        Calls the VolleyballEventDAO to invalidate a statistics record. It then
        maps the result to a JSON that contains the desired record. That JSON 
        object is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be invalidated.
            aID: the ID of the athlete for which the statistics record will be invalidated.

        Returns:
            A JSON containing the id of the invalidated record.
        """

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Validate existing athlete

        try:
            a_dao = AthleteDAO()
            athlete = a_dao.athleteExists(aID)
            if not athlete:
                return jsonify(Error="Atleta con ID:{} no se encontro.".format(aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar atleta desde el DAO."), 500

        # Validate Exists in order to remove

        try:
            dao = VolleyballEventDAO()
            # TODO: what is the error code for this case, where it DOESNT exit?
            if not dao.getVolleyballEventID(eID, aID):
                return jsonify(Error="Entrada de Evento de Voleibol no existe para Evento con ID:{} y Atleta con ID:{}.".format(eID, aID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        # Remove Volleyball_Event Statistics and format returnabe

        try:
            result = dao.removeStatistics(eID, aID)
            if not result:
                return jsonify(Error="Record de Estadisticas no se encontro para evento con ID:{} para Atleta con ID:{}.".format(eID, aID)), 404
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar evento de voleibol desde el DAO."), 500

        # update and validate Volleyball Event Team Statistic
        try:
            team_result = dao.editTeamStatistics(eID)
            if not team_result:
                return jsonify(Error="Record de Estadisticas de Equipo no se encontro para Evento con ID:{}.".format(eID)), 404
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO.."), 500

        dao.commitChanges()
        return jsonify(Volleyball_Event_Athlete_Statistics="Se removio record de estadisticas con ID:{} para atleta con ID:{} en evento con id:{}.".format(result[0], aID, eID)), 200

    # NEW
    # Instantiates a Volleyball Event DAO in order to complete the desired put request and it returns a JSON with either a confirmation or error message.
    def removeTeamStatistics(self, eID):
        """
        Invalidates a team statistics record in the database based on the given ID.

        Calls the VolleyballEventDAO to invalidate a team statistics record. It then
        maps the result to a JSON that contains the desired record. That JSON 
        object is then returned.

        Args:
            eID: the ID of the event for which the statistics record will be invalidated.

        Returns:
            A JSON the id of the invalidated Volleyball Event.
        """

        # Validate existing event

        try:
            e_dao = EventDAO()
            event = e_dao.eventExists(eID)
            if not event:
                return jsonify(Error="Evento para ID:{} no se encontro.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar Evento desde el DAO."), 500

        # Validate exists so can remove

        try:
            dao = VolleyballEventDAO()
            if not dao.getVolleyballEventTeamStatsID(eID):
                return jsonify(Error="Entrada de Estadisticas de Equipo para Evento de Voleibol no existe para Evento con ID:{}.".format(eID)), 400
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para evento de voleibol desde el DAO."), 500

        # Remove Volleyball_Event Team Statistics and format returnabe

        try:
            result = dao.removeTeamStatistics(eID)
            if not result:
                return jsonify(Error="Record de Estadisticas de Equipo no se encontro para evento con ID:{}.".format(eID)), 404
        except (TypeError, ValueError):
            return jsonify(ERROR="Solicitud Incorrecta, Error de Tipo."), 400
        except:
            return jsonify(ERROR="No se pudo verificar estadisticas de equipo para eventos de voleibol desde el DAO."), 500

        dao.commitChanges()
        return jsonify(Volleyball_Event_Team_Statistics="Se removio record de estadisticas de equipo con ID:{} para evento con ID:{}.".format(result, eID)), 200

