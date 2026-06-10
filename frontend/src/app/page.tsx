import DashboardLayout from
"@/components/layout/DashboardLayout"

export default function Home() {

 return (

  <DashboardLayout>

   <h1 className="text-3xl font-bold">

    Alpha Radar Dashboard

   </h1>

  </DashboardLayout>

 )
}

import OpportunityFeed
from "@/components/opportunities/OpportunityFeed"

const opportunities = [

 {
  title:"Monad Testnet",
  category:"AIRDROP",
  score:92
 },

 {
  title:"Security Grant",
  category:"GRANT",
  score:88
 }

]

export default function Home() {

 return (

  <div>

   <OpportunityFeed
    opportunities={opportunities}
   />

  </div>

 )
}