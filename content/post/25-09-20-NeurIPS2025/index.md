---
title: PKU-Alignment Group in NeurIPS 2025!
date: 2025-09-20
image:
  focal_point: 'top'
---

**PKU-Alignment Group has 4 papers accepted to NeurIPS 2025, including 2 Spotlights. Full abstracts and project links are provided below in one page.**

Our NeurIPS 2025 papers advances safety alignment and human preference learning across multimodal and embodied AI. SafeVLA proposes an integrated safety approach that formulates safety-constrained policy optimization for vision-language-action models, achieving substantial safety gains while preserving task performance. InterMT introduces the first multi-turn, interleaved multimodal preference dataset with expert oversight and establishes InterMT-Bench, revealing multi-turn scaling behavior for judge models. Generative RLHF-V unifies generative reward modeling with multimodal RLHF in a two-stage pipeline, delivering consistent performance improvements and analyzing reward hacking and generalization. Safe RLHF-V pioneers multimodal safety alignment with dual-preference data and a multi-level guardrail system, significantly improving both safety and helpfulness. Together, these works contribute scalable datasets, principled algorithms, and evaluation protocols that move alignment closer to robust, reliable deployment in complex real-world settings.

<div class="paper-card">
<span class="badge-spotlight">Spotlight</span>

## SafeVLA: Towards Safety Alignment of Vision-Language-Action Model via Safe Reinforcement Learning

Vision-language-action models (VLAs) show potential as generalist robot policies. However, these models pose extreme safety challenges during real-world deployment, including the risk of harm to the environment, the robot itself, and humans. How can safety constraints be explicitly integrated into VLAs? We address this by exploring an integrated safety approach (ISA), systematically modeling safety requirements, then actively eliciting diverse unsafe behaviors, effectively constraining VLA policies via safe reinforcement learning, and rigorously assuring their safety through targeted evaluations. Leveraging the constrained Markov decision process (CMDP) paradigm, ISA optimizes VLAs from a min-max perspective against elicited safety risks. Thus, policies aligned through this comprehensive approach achieve the following key features: (I) effective safety-performance trade-offs, this exploration yields an 83.58% safety improvement compared to the current state-of-the-art method, while also maintaining task performance (+3.85%). (II) strong safety assurance, with the ability to mitigate long-tail risks and handle extreme failure scenarios. (III) robust generalization of learned safety behaviors to various out-of-distribution perturbations. Our data, models and newly proposed benchmark environment are available at https://pku-safevla.github.io/.

Project Page: https://pku-safevla.github.io/
</div>

<div class="paper-card">
<span class="badge-spotlight">Spotlight · D&B Track</span>

## InterMT: Multi-Turn Interleaved Preference Alignment with Human Feedback

As multimodal large models (MLLMs) continue to advance across challenging tasks, a key question emerges: What essential capabilities are still missing? A critical aspect of human learning is continuous interaction with the environment — not limited to language, but also involving multimodal understanding and generation. To move closer to human-level intelligence, models must similarly support multi-turn, multimodal interaction. In particular, they should comprehend interleaved multimodal contexts and respond coherently in ongoing exchanges. In this work, we present an initial exploration through InterMT — the first preference dataset for multi-turn multimodal interaction, grounded in real human feedback. In this exploration, we particularly emphasize the importance of human oversight, introducing expert annotations to guide the process, motivated by the fact that current MLLMs lack such complex interactive capabilities. InterMT captures human preferences at both global and local levels into nine sub-dimensions, consists of 15.6k prompts, 52.6k multi-turn dialogue instances, and 32.4k human-labeled preference pairs. To compensate for the lack of capability for multi-modal understanding and generation, we introduce an agentic workflow that leverages tool-augmented MLLMs to construct multi-turn QA instances. To further this goal, we introduce InterMT-Bench to assess the ability of MLLMs in assisting judges with multi-turn, multimodal tasks. We demonstrate the utility of InterMT through applications such as judge moderation and further reveal the multi-turn scaling law of judge models. Our project website can be found at https://pku-intermt.github.io/.

Project Page: https://pku-intermt.github.io/
</div>

<div class="paper-card">

## Generative RLHF-V: Learning Principles from Multi-modal Human Preference

Training multi-modal large language models (MLLMs) that align with human intentions is a long-term challenge. Traditional score-only reward models for alignment suffer from low accuracy, weak generalization, and poor interpretability, blocking the progress of alignment methods, e.g., reinforcement learning from human feedback (RLHF). This paper introduces Generative RLHF-V, a novel alignment framework that integrates Generative Reward Models (GRMs) with multi-modal RLHF. We propose a two-stage pipeline: generative reward modeling from multi-model preference, where RL guides GRMs to actively capture human intention, then predict the correct pair-wise scores; and RL optimization from grouped comparison, which enhances multi-modal RL scoring precision by grouped responses comparison. Experimental results demonstrate that our framework improves 4 MLLMs' performance across 7 benchmarks by 18.1%, while the baseline RLHF is only 5.3%. We further validate the out-of-distribution generalization of GRMs and the scaling trends of grouped comparisons. Additionally, we investigated GRMs' susceptibility to reward hacking within an overfitting setting. Our findings indicate that MLLMs use self-praising behaviors to deceptively receive high rewards from GRMs. Significantly, this deceptive behavior is also effective in misleading MLLM-as-judge benchmarks that are analogous to GRM scoring. Our code, models, and evaluation details can be found at https://generative-rlhf-v.github.io/.

Project Page: https://generative-rlhf-v.github.io/
</div>

<div class="paper-card">

## Safe RLHF-V: Safe Reinforcement Learning from Multi-modal Human Feedback

Multimodal large language models (MLLMs) are essential for building general-purpose AI assistants; however, they pose increasing safety risks. How can we ensure safety alignment of MLLMs to prevent undesired behaviors? Going further, it is critical to explore how to fine-tune MLLMs to preserve capabilities while meeting safety constraints. Fundamentally, this challenge can be formulated as a min-max optimization problem. However, existing datasets have not yet disentangled single preference signals into explicit safety constraints, hindering systematic investigation in this direction. Moreover, it remains an open question whether such constraints can be effectively incorporated into the optimization process for multi-modal models. In this work, we present the first exploration of Safe RLHF-V — the first multimodal safety alignment framework. The framework consists of: (I) BeaverTails-V, the first open-source dataset featuring dual preference annotations for helpfulness and safety, supplemented with multi-level safety labels (minor, moderate, severe); (II) Beaver-Guard-V, a multi-level guardrail system to proactively defend against unsafe queries and adversarial attacks. Applying the guard model over five rounds of filtering and regeneration significantly enhances the precursor model's overall safety by an average of 40.9%. (III) Based on dual preference, we initiate the first exploration of multi-modal safety alignment within a constrained optimization. Experimental results demonstrate that Safe RLHF effectively improves both model helpfulness and safety. Specifically, Safe RLHF-V enhances model safety by 34.2% and helpfulness by 34.3%.

Project Page: https://github.com/saferlhf-v
</div>
