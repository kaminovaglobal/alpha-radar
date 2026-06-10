import OpportunityCard
from "./OpportunityCard"

export default function OpportunityFeed({
 opportunities
}: any) {

 return (

  <div className="grid gap-4">

   {opportunities.map(
    (item:any)=>(
      <OpportunityCard
       key={item.title}
       {...item}
      />
    )
   )}

  </div>

 )
}