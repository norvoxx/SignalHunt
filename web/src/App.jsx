import { useState } from 'react'
import {Search} from './pages/Search/Search.jsx'
import {Map} from './pages/Map/Map.jsx'
import "./App.css"

import { createBrowserRouter,RouterProvider,Outlet,NavLink } from "react-router-dom";

const router = createBrowserRouter([
    {
        path: "/",
        element: <Root/>,
        children: [
            {
                path: "/",
                element : <Search/>
            },
            {
                path: "/map",
                element : <Map/>
            }
        ]
    },

]);

function Root(){
    return(<>
        <header className="App-header" >
            <nav className="navbar">
                <NavLink  to="/">Home</NavLink>
                <NavLink  to="/map">Map</NavLink>
            </nav>
        </header>
        <div className="App">
            <Outlet/>
        </div>
    </>)
}

function App() {
  return (
      <RouterProvider router={router} />
  )
}
export default App
