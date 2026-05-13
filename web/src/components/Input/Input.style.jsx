import styled, { keyframes } from 'styled-components';



export const Input = styled.input`
    width: 100%;
    padding: 10px  12px;
    font-size: 16px;
    border-radius: 8px;
    
    outline: none;
    
    transition: all 0.3s ease;
    background-color: var(--color-surface);
    
    color: var(--color-text-main);
    
    box-sizing: border-box;
    border: 2px solid var(--color-surface);
    
    &:focus {
        border-color: var(--color-success);
    }
    
`;