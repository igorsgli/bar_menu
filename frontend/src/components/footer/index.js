import styles from './style.module.css'
import { Container, LinkComponent } from '../index'

const Footer = () => {
  return <footer className={styles.footer}>
      <Container className={styles.footer__container}>
        <LinkComponent href='#' title='Барное меню' className={styles.footer__brand} />
      </Container>
  </footer>
}

export default Footer