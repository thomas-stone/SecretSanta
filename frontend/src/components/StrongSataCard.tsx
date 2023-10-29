import strong_santa from "../assets/strong_santa.gif";

interface Props {
    className: string
}

const StrongSataCard = ({className}: Props) => {
  return (
    <div className={`grid place-items-center relative cursor-pointer group hover:cursor-default ${className}`}>
      <img loading="lazy" src={strong_santa} alt="strong_santa" className=" border border-slate-300 rounded-xl"/>
    </div>
  );
}

export default StrongSataCard