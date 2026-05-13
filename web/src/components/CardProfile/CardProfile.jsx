import * as S from './CardProfile.style.jsx';
import {CardContent, Link} from "./CardProfile.style.jsx";
import dontImg from "../../assets/errorProfile.png";

export function CardProfile({website, tag, avatar , username , htmlUrl,props}) {
    return (
        <S.CardContent>
            <div className={"headerCard"}>
                <h3>{website}</h3>
                <div className="tag">{tag}</div>
            </div>
            <div className="card-profile">
                <img className={"avatar"} src={avatar || dontImg}></img>
                <p><strong>Usename</strong> : {username}</p>
                <Link  target="_blank" rel="noopener noreferrer" href={htmlUrl}>Profile</Link>
            </div>
        </S.CardContent>
    )}