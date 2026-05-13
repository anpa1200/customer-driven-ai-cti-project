import type {ReactNode} from 'react';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

const cards = [
  {
    title: 'Workflow Quick Reference',
    text: 'The 15-phase operational map from customer decision to production detection and final delivery.',
    to: '/docs/workflow/full-workflow-quick-reference',
  },
  {
    title: 'Part 1: Foundations',
    text: 'Analytic standards, evidence labels, source reliability, AI governance, roles, and readiness levels.',
    to: '/docs/methodology/foundations',
  },
  {
    title: 'Part 2A: Execution Guide',
    text: 'Phase 0 through Phase 14 activities, validation tests, templates, and exit criteria.',
    to: '/docs/methodology/phase-by-phase-execution-guide',
  },
  {
    title: 'Part 2B: Reference Toolkit',
    text: 'AI workflows, LLM task cards, strict quality gates, registers, worked example, and delivery package.',
    to: '/docs/methodology/reference-toolkit',
  },
];

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={styles.hero}>
      <div className="container">
        <p className={styles.kicker}>CTI to Detection Engineering</p>
        <Heading as="h1" className={styles.title}>
          {siteConfig.title}
        </Heading>
        <p className={styles.subtitle}>{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link className="button button--primary button--lg" to="/docs/">
            Open Documentation
          </Link>
          <Link className="button button--secondary button--lg" to="/docs/published-articles">
            Published Articles
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="Docusaurus site for the Customer-Driven AI CTI Project methodology.">
      <HomepageHeader />
      <main className={styles.main}>
        <section className="container">
          <div className={styles.grid}>
            {cards.map((card) => (
              <Link className={styles.card} to={card.to} key={card.to}>
                <h2>{card.title}</h2>
                <p>{card.text}</p>
              </Link>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
