import styled from 'styled-components';

export const ContainerSearch = styled.form`
    position: relative;
    width: 100%;
    height: 60vh;

    background-image:
            linear-gradient(to right, var(--color-surface) 1px, transparent 1px),
            linear-gradient(to bottom, var(--color-surface) 1px, transparent 1px);

    background-size: 60px 60px;

    -webkit-mask-image: linear-gradient(to bottom, var(--color-background) 80%, transparent 100%);
    mask-image: linear-gradient(to bottom, var(--color-background) 80%, transparent 100%);

    z-index: 1; /* important */

    .from {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);

        

        width: 90%;
        max-width: 600px;
    }

    h1 {
        font-size: 2.5rem;
    }

    @media (max-width: 768px) {
        height: 50vh;

        h1 {
            font-size: 2rem;
        }

        .from {
            width: 95%;
        }
    }

    /* MOBILE */
    @media (max-width: 480px) {
        height: 45vh;

        h1 {
            font-size: 1.6rem;
        }

        .from {
            gap: 0.7rem;
        }
    }
`;

export const Container = styled.div`
    display: flex;
    flex-direction: row;
    width: 100%;
    margin: 0 auto;
    
    @media (max-width: 768px) {
        width: 90%;
        flex-direction: column;
    }

    /* MOBILE */
    @media (max-width: 480px) {
        width: 95%;
    }
`;

export const Cardbiblio = styled.div`
    margin: 1rem 10rem;
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
    justify-content: center;

    @media (max-width: 1024px) {
        margin: 1rem 3rem;
        gap: 1.5rem;
    }

    @media (max-width: 600px) {
        margin: 1rem;
        flex-direction: column;
        align-items: center;
    }
`;