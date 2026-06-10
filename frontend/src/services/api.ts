const API_URL =
"http://localhost:8000"


export async function getOpportunities() {

 const response =
 await fetch(
 `${API_URL}/opportunities`
 )

 return response.json()
}