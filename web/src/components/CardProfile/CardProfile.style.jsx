import styled from 'styled-components';

export const CardContent = styled.div`
    position: relative;
    width: 260px;
    border-radius: 16px;
    background-color: var(--color-surface);
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px 16px;
    
    box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    border: 1px solid rgba(0,0,0,0.05);

    transition: transform 0.2s ease, box-shadow 0.2s ease;

    &:hover {
        transform: translateY(-4px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    }

    h3{
        font-family: 'MaPolice', sans-serif;
        font-size: 1.1rem;
        margin: 12px 0 4px;
        text-align: center;
    }

    .card-profile{
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
    }

    .avatar{
        border-radius: 50%;
        height: 120px;
        width: 120px;
        object-fit: cover;

        /* plus clean que border noir */
        border: 3px solid rgba(0,0,0,0.05);
    }

    .headerCard{
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 6px;
    }

    .tag{
        color: var(--color-success);
        border: 1px solid var(--color-success);
        padding: 3px 8px;
        font-size: 0.7rem;
        border-radius: 999px;
        background-color: rgba(0,0,0,0.02);
    }
`;


export const Link = styled.a`
    color: var(--color-text-main);
    text-decoration: none;
    font-weight: 500;
    position: relative;

    transition: color 0.2s ease;

    &:hover {
        color: var(--color-alpha-hover, var(--color-alpha));
    }

    /* underline animé */
    &::after {
        content: '';
        position: absolute;
        left: 0;
        bottom: -2px;
        width: 0%;
        height: 1px;
        background-color: currentColor;
        transition: width 0.2s ease;
    }

    &:hover::after {
        width: 100%;
    }
`;