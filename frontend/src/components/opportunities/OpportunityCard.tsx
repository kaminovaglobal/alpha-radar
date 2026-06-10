type Props = {

 title: string

 category: string

 score: number
}

export default function OpportunityCard({
 title,
 category,
 score
}: Props) {

 return (

  <div
   className="border rounded p-4"
  >

   <h3>{title}</h3>

   <p>{category}</p>

   <p>Score: {score}</p>

  </div>

 )
}