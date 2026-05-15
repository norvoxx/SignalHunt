import styled from 'styled-components';

export const MapContainer = styled.div`
    height: 100vh;
    width: 100%;
    background-image: radial-gradient(#616161 1px, transparent 1px);
    background-size: 40px 40px;
    position: 'relative';
    overflowY: "scroll"
`

export const Node = styled.div`
    z-index: 2;
    min-height: 50px;
    min-width: 50px;
    
    background-color: gray;
    border-radius: 50%;
    cursor: pointer;
    userSelect: none;
    
    display: flex;
    align-items: center;
    justify-content: center;
    color: black;
    
    font-size: 30px;
    i{
        pointer-events: none;
    }
    &.hovered {
        border-color: #4da3ff;
        transform: scale(1.1);
    }

    &.selected {
        border-color: #00ff88;
        box-shadow: 0 0 10px rgba(0,255,136,0.6);
    }
`