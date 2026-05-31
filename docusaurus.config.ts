import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Customer-Driven AI CTI Project',
  tagline: 'A gate-controlled CTI-to-detection methodology for customer outcomes.',
  favicon: 'img/favicon.svg',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://anpa1200.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/customer-driven-ai-cti-project/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'anpa1200',
  projectName: 'customer-driven-ai-cti-project',

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/anpa1200/customer-driven-ai-cti-project/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'AI CTI Project',
      logo: {
        alt: '1200km',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'docsSidebar',
          position: 'left',
          label: 'Docs',
        },
        {to: '/docs/ecosystem', label: 'Ecosystem', position: 'left'},
        {to: '/docs/published-articles', label: 'Articles', position: 'left'},
        {
          label: 'Projects',
          position: 'right',
          items: [
            {label: 'Field Manual', href: 'https://anpa1200.github.io/cti-analyst-field-manual/'},
            {label: 'CTI as a Code', href: 'https://anpa1200.github.io/CTI_as_a_Code/'},
            {label: 'Operation Desert Hydra', href: 'https://anpa1200.github.io/operation-desert-hydra/'},
            {label: 'Customer-Driven AI CTI', href: 'https://anpa1200.github.io/customer-driven-ai-cti-project/'},
            {label: 'Israel Threat Actors CTI', href: 'https://anpa1200.github.io/israel-government-threat-actors-cti/'},
            {label: 'AI vs Defense', href: 'https://anpa1200.github.io/ai-vs-defense/'},
            {label: 'HexStrike AI', href: 'https://github.com/0x4m4/hexstrike-ai'},
          ],
        },
        {
          href: 'https://github.com/anpa1200/customer-driven-ai-cti-project',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Overview',
              to: '/docs/',
            },
          ],
        },
        {
          title: 'Project',
          items: [
            {
              label: 'Workflow',
              to: '/docs/workflow/full-workflow-quick-reference',
            },
            {
              label: 'Foundations',
              to: '/docs/methodology/foundations',
            },
            {
              label: 'Reference Toolkit',
              to: '/docs/methodology/reference-toolkit',
            },
          ],
        },
        {
          title: 'Ecosystem',
          items: [
            {label: 'Field Manual', href: 'https://anpa1200.github.io/cti-analyst-field-manual/'},
            {label: 'CTI as a Code', href: 'https://anpa1200.github.io/CTI_as_a_Code/'},
            {label: 'Operation Desert Hydra', href: 'https://anpa1200.github.io/operation-desert-hydra/'},
            {label: 'Customer-Driven AI CTI', href: 'https://anpa1200.github.io/customer-driven-ai-cti-project/'},
            {label: 'Israel Threat Actors CTI', href: 'https://anpa1200.github.io/israel-government-threat-actors-cti/'},
            {label: 'AI vs Defense', href: 'https://anpa1200.github.io/ai-vs-defense/'},
            {label: 'HexStrike AI', href: 'https://github.com/0x4m4/hexstrike-ai'},
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Medium',
              href: 'https://medium.com/@1200km/customer-driven-ai-cti-project-c0db3cdc1830',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/anpa1200/customer-driven-ai-cti-project',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Andrey Pautov. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
