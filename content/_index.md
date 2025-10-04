---
# Leave the homepage title empty to use the site title
title:
date: 2025-09-25
type: landing

sections:
  - block: markdown
    content:
      title: Our Mission
      text: |-
        The **PKU-Alignment Group**, under the **[PKU Pair-Lab](www.pair-lab.ai)**, is a pioneering research interest group dedicated to advancing the frontiers of AI safety and alignment. Our mission is to explore the fundamental algorithms and mechanisms that underpin AI alignment, driving both theoretical innovation and practical deployment. 
        
        Our mission is to ensure that AI systems remain consistently aligned with human goals. The team actively shares the latest advances in AI research, while fostering the development and real-world adoption of safety and alignment practices. Our key research direction include:
        - **Mechanisms and Interpretability in Alignment**: Investigating whether large models can be effectively aligned, their resilience to misalignment, and the interpretability of alignment mechanisms;
        - **Reinforcement Learning and Post-training of Language Models**: Designing more efficient and reliable post-alignment algorithms;
        - **Safety Alignment and Superalignment**: Addressing frontier-risk alignment challenges such as deceptive alignment, scalable oversight, CBRN hazards, and interpretability; as well as value alignment issues, including regional value alignment and bidirectional value lock-in.
    design:
      columns: '1'
  
  - block: collection
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  - block: collection
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: compact
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle:
      text: |
        {{% cta cta_link="./people/" cta_text="Meet the team →" %}}
    design:
      columns: '1'
---
