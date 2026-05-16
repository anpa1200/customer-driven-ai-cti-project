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
    'ecosystem',
    'published-articles',
    'infographics',
    {
      type: 'category',
      label: 'Project Governance',
      collapsed: false,
      items: [
        'project-governance/versioning',
        'project-governance/changelog',
        'project-governance/roadmap',
        'project-governance/deprecated',
      ],
    },
    {
      type: 'category',
      label: 'Standard',
      collapsed: false,
      items: [
        'standard/normative-language',
        'standard/artifact-contracts',
        'standard/schemas-and-validation',
        'standard/attack-mappings',
      ],
    },
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
    {
      type: 'category',
      label: 'Practitioner Package',
      collapsed: false,
      items: [
        'practitioner-package/package-index',
        'practitioner-package/fake-customer-scenario',
        'practitioner-package/sample-registers',
        'practitioner-package/detection-artifacts',
        'practitioner-package/replay-example',
        'practitioner-package/gate-evidence-packs',
        'practitioner-package/workflow-output-screenshots',
        'practitioner-package/complete-worked-case',
      ],
    },
  ],
};

export default sidebars;
