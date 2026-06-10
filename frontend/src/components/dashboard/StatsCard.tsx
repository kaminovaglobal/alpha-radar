type Props = {

 title:string

 value:number
}

export default function StatsCard({
 title,
 value
}:Props){

 return(

  <div className="border p-4">

   <h3>{title}</h3>

   <p>{value}</p>

  </div>

 )
}