<script setup lang="ts">
import { ref } from 'vue';

const showDialog = ref(true);

const selectedReportType = ref<string | null>(null);
const selectedFormat = ref<string | null>(null);


const reportTypes = ['Medicamentos'];
const reportFormat = ['pdf']

function handleConfirm() {
    if (selectedReportType.value && selectedFormat) {
        console.log(`Generar reporte de ${selectedReportType.value} para ${selectedFormat.value}`);
        showDialog.value = false;
    }
}

// Función para cancelar
function handleCancel() {
    showDialog.value = false;
}
</script>

<template>
    <h1>Create Report</h1>

    <!-- Modal para seleccionar el tipo de reporte y la categoría -->
    <v-dialog v-model="showDialog" max-width="500px">
        <v-card>
            <v-card-title>Seleccionar Reporte</v-card-title>
            <v-card-text>
                <v-select
                    v-model="selectedReportType"
                    :items="reportTypes"
                    label="Tipo de Reporte"
                />
            </v-card-text>
            <!-- Modal para seleccionar el formato del reporte -->
            <v-card-text>
                <v-select
                    v-model="selectedFormat"
                    :items="reportFormat"
                    label="Formato que se desea el reporte"
                />
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary" @click="handleConfirm">Generar</v-btn>
                <v-btn @click="handleCancel">Cancelar</v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>