<template>
  <v-simple-table fixed-header>
    <thead>
      <tr>
        <th class="text-center">ESTADÍSTICAS DE INTERÉS</th>
        <th class="text-center">VALOR DE ESTADÍSTICAS</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="text-center">GOLES</td>
        <td class="text-center">{{ soccer_stats.Goal }}</td>
      </tr>
      <tr>
        <td class="text-center">TIROS A PORTERÍA</td>
        <td class="text-center">{{ soccer_stats.GoalAttempt }}</td>
      </tr>
      <tr>
        <td class="text-center">ASISTENCIAS</td>
        <td class="text-center">{{ soccer_stats.Assist }}</td>
      </tr>
      <tr>
        <td class="text-center">ATAJADAS</td>
        <td class="text-center">{{ soccer_stats.Tackle }}</td>
      </tr>
      <tr>
        <td class="text-center">FALTAS</td>
        <td class="text-center">{{ soccer_stats.Foul }}</td>
      </tr>
      <tr>
        <td class="text-center">TARJETAS AMARILLAS</td>
        <td class="text-center">{{ soccer_stats.YellowCard }}</td>
      </tr>
      <tr>
        <td class="text-center">TARJETAS ROJAS</td>
        <td class="text-center">{{ soccer_stats.RedCard }}</td>
      </tr>
    </tbody>
  </v-simple-table>
</template>

<script>
export default {
  props: {
    soccer_stats: {}
  }
};
</script>
