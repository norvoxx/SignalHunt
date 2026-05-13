import * as S from './InputBtn.style.jsx';

export function InputBtn({props,children}) {
    return (
        <S.InputBtnStyle className="btn" {...props}>
            {children}
        </S.InputBtnStyle>
    )
}