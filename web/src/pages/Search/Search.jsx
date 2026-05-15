import { Input } from "../../components/Input/Input.jsx";
import { InputBtn } from "../../components/InputBtn/InputBtn.jsx";
import { CardProfile } from "../../components/CardProfile/CardProfile.jsx";

import * as S from './Search.style.jsx';
import { useState } from 'react';

export function Search() {
    const [search, setSearch] = useState("");

    const [data, setData] = useState(() => {
        const savedSearch = localStorage.getItem("search");
        if (savedSearch) {
            const parsed = JSON.parse(savedSearch);
            return parsed["item"] || [];
        }
        return [];
    });
    const handleSubmit = (e) => {
        e.preventDefault();
        fetch(`http://127.0.0.1:8000/search/${search}`)
            .then(res => res.json())
            .then(result => {
                setData(result["item"]);
                localStorage.setItem("search", JSON.stringify(result));
            })
            .catch(err => console.error("Erreur lors de la recherche :", err));

        setSearch("");
    };
    return (
        <div>
            <S.ContainerSearch onSubmit={handleSubmit}>
                <div className={"from"}>
                    <h1>Search all traces online with username</h1>
                    <S.Container>
                        <Input
                            value={search}
                            onChange={(e) => setSearch(e.target.value)}
                            placeholder="search..."
                            style={{ borderRadius: "10px 0px 0px 10px" }}
                        />
                        <InputBtn type="submit">Search</InputBtn>
                    </S.Container>
                </div>
            </S.ContainerSearch>

            <S.Cardbiblio>
                {data && data.map((item, index) => (
                    item.exist && (
                        <CardProfile
                            key={index}
                            website={item.website}
                            tag={item.tag}
                            avatar={item.avatar}
                            username={item.username}
                            htmlUrl={item.htmlUrl}
                        />
                    )
                ))}
            </S.Cardbiblio>
        </div>
    );
}