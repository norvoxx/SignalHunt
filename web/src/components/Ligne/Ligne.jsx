

export function Ligne({ start, end, onClick }) {
    return (
        <svg style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            pointerEvents: 'none'
        }}>
            <line
                x1={start.x + 25} y1={start.y + 25}
                x2={end.x + 25} y2={end.y + 25}
                stroke="var(--color-alpha)"
                strokeWidth="2"
                strokeDasharray="10 0"


                style={{
                    cursor: "pointer",
                    pointerEvents: 'auto'
                }}

                onClick={()=>{
                    console.log("clicked");
                }}
            />
        </svg>
    );
}

export function LigneA({ start, end }) {
    const midX = (start.x + end.x) / 2;
    const midY = (start.y + end.y) / 2;

    return (
        <svg style={{
            position: 'absolute',
            top: 0,
            left: 0,
            width: '100%',
            height: '100%',
            pointerEvents: 'none'
        }}>
            <path
                d={`
                    M ${start.x + 25} ${start.y + 25}
                    Q ${midX + 25} ${start.y - 50}
                      ${end.x + 25} ${end.y + 25}
                `}
                stroke="var(--color-alpha)"
                strokeWidth="2"
                fill="none"
                style={{
                    cursor: "pointer",
                    pointerEvents: 'auto'
                }}
                onClick={() => console.log("clicked")}
            />
        </svg>
    );
}