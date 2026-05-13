import styled, { keyframes } from 'styled-components';

export const InputBtnStyle = styled.button`
    padding: 0 20px;
    background-color: var(--color-alpha);
    color: white;
    border: none;
    font-family: 'Aquire', sans-serif;
    font-size: 0.8rem;
    cursor: pointer;
    transition: all 0.2s ease;
    text-transform: uppercase;
    
    border-radius: 0px 10px 10px 0px;
    font-weight: bold;

    &:hover {
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.8), 0 0 20px var(--color-alpha);
        
        box-shadow: 0 0 150px var(--color-alpha-glow);
    }

    &:active {
        transform: scale(0.95);
    }
`;


