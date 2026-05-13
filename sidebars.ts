import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  docsSidebar: [
    'intro',
    'published-articles',
    {
      type: 'category',
      label: 'Workflow',
      collapsed: false,
      items: ['workflow/full-workflow-quick-reference'],
    },
    {
      type: 'category',
      label: 'Methodology',
      collapsed: false,
      items: [
        'methodology/foundations',
        'methodology/phase-by-phase-execution-guide',
        'methodology/reference-toolkit',
        'methodology/complete-template',
      ],
    },
  ],
};

export default sidebars;
