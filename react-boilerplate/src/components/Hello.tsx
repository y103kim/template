import { TextField } from "@material-ui/core";
import React from "react";
import { useRecoilState } from "recoil";
import { helloState } from "../stores/hello";

export const Hello: React.FC = () => {
    const [hello, setHello] = useRecoilState(helloState);
    return (
        <React.Fragment>
            <TextField value={hello} onChange={(e) => setHello(e.target.value)} />
        </React.Fragment>
    );
};
