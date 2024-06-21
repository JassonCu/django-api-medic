import { DataEntry } from "@/@layouts/types"

const BASE_URL = 'http://localhost:8000';

export async function fetchData(endpoint: string): Promise<DataEntry[]> {
  const url = `${BASE_URL}/${endpoint}`;

  try {
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    return await response.json();
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error; // Propaga el error para que sea manejado en el componente que hace la llamada
  }
}
