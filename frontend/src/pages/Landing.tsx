import Header from "../components/Header"
import Footer from "../components/Footer"
import TestMainPage from "../components/TestMainPage";

const Landing = () => {
  return (
    <div className="flex flex-col h-screen justify-between">
      <Header></Header>
      <TestMainPage></TestMainPage>
      <Footer></Footer>
    </div>
  );
};

export default Landing;
