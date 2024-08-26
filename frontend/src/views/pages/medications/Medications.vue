<template>
    <div>
        <h1>Medicamentos</h1>

        <!-- Botón para generar reporte -->
        <v-btn color="primary" @click="showConfirmationDialog = true">Generar Reporte PDF</v-btn>

        <!-- Modal de confirmación -->
        <v-dialog v-model="showConfirmationDialog" max-width="500px">
            <v-card>
                <v-card-title>Confirmación</v-card-title>
                <v-card-text>
                    ¿Estás seguro de que deseas generar el reporte PDF?
                </v-card-text>
                <v-card-actions>
                    <v-btn color="primary" @click="generateReport">Sí</v-btn>
                    <v-btn @click="showConfirmationDialog = false">Cancelar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <!-- Tabla de medicamentos -->
        <VTable density="compact">
            <thead>
                <tr>
                    <th class="text-uppercase">Id</th>
                    <th class="text-uppercase">Nombre</th>
                    <th class="text-uppercase">Casa</th>
                    <th class="text-uppercase">Fecha de expiración</th>
                    <th class="text-uppercase">Cantidad</th>
                    <th class="text-uppercase">Unidad de medida</th>
                    <th class="text-uppercase">Precio</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="medicamento in medicamentos" :key="medicamento.id">
                    <td>{{ medicamento.id }}</td>
                    <td>{{ medicamento.name }}</td>
                    <td>{{ medicamento.manufacturer_names.join(', ') }}</td>
                    <td>{{ medicamento.expiration_date }}</td>
                    <td>{{ `${medicamento.stock} ${medicamento.presentation_name}` }}</td>
                    <td>{{ medicamento.unit_short_name }}</td>
                    <td>{{ formatPrice(medicamento.currency_symbol, medicamento.price) }}</td> <!-- Cambiado -->
                </tr>
            </tbody>
        </VTable>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { VTable } from 'vuetify/lib/components/index.mjs';
import { useRouter } from 'vue-router';
import { log } from 'console';

const router = useRouter();

interface Medicamento {
    id: number;
    name: string;
    manufacturer_names: string[];
    expiration_date: string;
    stock: string;
    unit: string;
    price: number
    presentation: string
    presentation_name: string;
    currency_symbol: string;
    unit_short_name: string;
}

const headers = ref([
    { text: 'ID', value: 'id' },
    { text: 'Nombre', value: 'name' },
    { text: 'Casa', value: 'manufacturer_names' },
    { text: 'Fecha de expiración', value: 'expiration_date' },
    { text: 'Cantidad', value: 'stock' },
    { text: 'Unidad de medida', value: 'unit_short_name' },
    { text: 'Precio', value: 'price' },
    { text: 'Presentación', value: 'medication_presentation' },
    { text: 'Presentación', value: 'presentation_name' }
]);

const medicamentos = ref<Medicamento[]>([]);

const showConfirmationDialog = ref(false);

const fetchData = async () => {
    try {
        const response = await axios.get('http://localhost:8000/api/');
        console.log(response.data);
        
        medicamentos.value = response.data;
    } catch (error) {
        console.error('Error al obtener los medicamentos:', error);
    }
};

const formatPrice = (currencySymbol: string, price: string | number) => {
  // Convertir el precio a un número si es una cadena
  const numericPrice = typeof price === 'string' ? parseFloat(price) : price;

  if (!isNaN(numericPrice)) {
    return `${currencySymbol} ${numericPrice.toFixed(2)}`;
  }

  return '';
};


onMounted(() => {
    fetchData();
});

const generateReport = () => {
    showConfirmationDialog.value = false;
    router.push('/create-report');
};
</script>