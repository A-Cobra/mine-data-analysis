import React from 'react';
import style from './Navbar.module.css';
import { Link } from 'react-router-dom';

const navigationRoutes = [
  { path: '/carga', name: 'Cargar' },
  { path: '/resumen', name: 'Resumen' },
];

const Navbar = () => {
  return (
    <header>
      <nav>
        <ul className={style.flex_container}>
          {navigationRoutes.map((navigationRoute, index) => {
            return (
              <li className={style.navigation_item} key={index}>
                <Link
                  className={style.anchor}
                  to={navigationRoute.path}
                  title={navigationRoute.name}
                >
                  {navigationRoute.name}
                </Link>
              </li>
            );
          })}
        </ul>
      </nav>
    </header>
  );
};

export default Navbar;
