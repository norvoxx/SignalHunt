import { useState, useRef ,useEffect} from 'react';
import * as S from './Map.style.jsx';
import {Ligne} from '../../components/Ligne/Ligne.jsx';


export function Map() {
    const draggingNodeId = useRef(null);
    const isDragging = useRef(false);

    const [nodes, setNodes] = useState([
        { id: 0, x: window.innerWidth/2-25,website : " fa-regular fa-circle-user", y: 200 , connection :[]},
    ]);

    useEffect(() => {
        const localData = localStorage.getItem('search');
        const parsed = localData ? JSON.parse(localData) : {};
        const items = parsed["item"] || [];

        const itemFiltered = items.filter(item => item["exist"])

        let index = 1;
        const spacesire = 60;
        const startX = (window.innerWidth/2-25) - ( itemFiltered.length/2 * spacesire) - 30;

        const newNodes = items
            .filter(item => item["exist"])
            .map(item => ({
                id: index++,
                x: startX + (index-1) * spacesire,
                website: "fab fa-"+item["website"],
                y: 300 ,
                connection: [0]
            }));

        setNodes(prev => {
            const existingIds = new Set(prev.map(n => n.id));
            const filtered = newNodes.filter(n => !existingIds.has(n.id));
            return [...prev, ...filtered];
        });
    }, []);

    const handleMouseDown = (id) => (e) => {
        draggingNodeId.current = id;
        isDragging.current = false;
    };

    const handleMouseMove = (e) => {
        if (draggingNodeId.current === null) return;
        isDragging.current = true;
        setNodes((prevNodes) =>
            prevNodes.map((node) =>
                node.id === draggingNodeId.current
                    ? { ...node, x: node.x + e.movementX, y: node.y + e.movementY }
                    : node
            )
        );
    };

    const handleMouseUp = () => {
        draggingNodeId.current = null;
    };



    return (
        <S.MapContainer onMouseMove={handleMouseMove} onMouseUp={handleMouseUp} onMouseLeave={handleMouseUp}>

            {nodes.map((node) => (
                <S.Node
                    key={node.id}
                    id={node.id}

                    onMouseDown={handleMouseDown(node.id)}
                    style={{position: 'absolute', left: `${node.x}px`, top: `${node.y}px`}}>
                    <i className={`${node.website}`}/>
                </S.Node>
            ))}

            {nodes.map((node) =>
                node.connection.map((targetId) => {
                    const targetNode = nodes.find(n => n.id === targetId);
                    return (
                        <Ligne key={`${node.id}-${targetId}`} start={node} end={targetNode}/>
                    );
                })
            )}
        </S.MapContainer>
    );
}