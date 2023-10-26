import facebookLogo from '../assets/logos/facebook.svg';
import twitterLogo from '../assets/logos/twitter.svg';
import linkedinLogo from '../assets/logos/linkedin.svg';

// interface Props {
//   logo: string;
// }

const Footer = () => {
  return (
    <div id="contact" className="flex flex-row flex-wrap items-center justify-around p-10 border-t-2 border-t-black bg-slate-400">
        <div className="flex items-center justify-around w-2/3 pt-5 lg:pt-0 lg:w-1/3 ">
            <img src={facebookLogo}></img>
            <img src={linkedinLogo}></img>
            <img src={twitterLogo}></img>
        </div>

        <div className="mt-10 text-lg text-blue-800 lg:mt-0">
            Copyright 2023 Two Stones and Jason
        </div>
  </div>
  );
}

export default Footer