# Research Plan

## Research Question
=> `Active Nematics of Zebrafish Heart Sarcomere Organisation`


## Research Focus
### What are we looking at (modelling)?
We are looking at sarcomere organisation (suggesting strong nematic order and clear director field of actin filaments) described by actin-myosin filament active nematics. In other words: modelling the actin-myosin filaments, as an active nematic framework driven by the zebrafish heart shape stretching and cell parameter tension, allows us to observe and dictate the organisation of sarcomeres for the zebrafish heart during function (beating) and formation. This modelling will be done at the cardiomyocyte scale. 

Start with assuming the nematic to quadratic phase transition is homogeneous with all cardiomyocytes (look at just one cell). Then try to model this phase transition for the whole ventral view. Since this change is only observed in the ventral side while the lateral side stays nematic, we can start by making a 2D movie then transition into 3D to incorporate the lateral side. Though filaments do not span the whole cell, we can start by assuming they do to simplify the model and add noise later.

We are focused on the fine-scale model where the individual actin filaments are represented as rods and their active nematic ordering allows us to conclude how they form sarcomere precursors and in turn how the sarcomeres are formed (disordered to ordered). 

The steps taken to model this follows thusly:
Ising model - descibes the up and down motion of the rods.
X-Y model - describes the omnidirectional movement of the rods.
nematic model - describes the directionality of rods where n = -n (head and tail).
quartic model - describes the directionality of rods where all four sides are equal.
Monte Carlo Metropolis model.


## Materials & Methods
### Theoretical
`?? Universality Class`


`Hydrodynamic Equations`


### Computational
`Ising Model`
- Start with modelling the Ising model to show up/down motion of the rods.

`X-Y Model`
- Move onto the X-Y model to show omnidirectional movement of the rods.

`Nematic Model`
- Model the rods with a 'head' and 'tail' where directional order n = -n

`Quartic Model`
- Show that the rods can be arranged quartically.


## Results & Discussion

### Output
A movie (active nematic) showing the modelled antin and myosin filaments at the cardiomyocyte scale. The movie should highlight the obvious change in phase of the actin filaments from nematic to quadratic. A fine-scaled model accurately depicting the shift of phase.

(Potentially) A crude and predictive movie showing the movement of the filaments organising into sarcomeres while portraying the construction of sarcomeres.

(Potentially) A crude and predictive movie of the sarcomere organisation in myofibril scale / perspective.

### What do we expect to see?
Nematic phase shifting into quadratic phase to form quadratic patches. Potentially the organisation of the patches into one quadratic network across the ventral zebrafish atrium. We will assume that the myosin filaments will always face in the same direction as the actin filaments.


## Questions
    Are we focused on sarcomere (rod) active nematics (coarse-grained) or actin-myosin (rod/filaments) active nematics (fine-scaled) that describe sarcomere organisation? Or do both?
> Find out through Mia Yap or ask Chiu Fan
===
`We are looking at the actin-myosin filaments (fine-scaled)`
`There are actin rail deposits that disappear in later stages of heart development`
`Patchwork quadratic of individual cells gather to become one large quadratic network`
`Filaments may not span the whole cell`
`Model phenomena with one cell first and assume homogeneity across the patch`
`Find a way to introduce noise to randomise parameters`

    Can you break down the layers of the heart at a cell-by-cell level? How thick are each layer? How are the cardiomyocytes ordered?
===
`Lowerest layer is the endocardium (touches the blood and interacts with blood flow). It is only a one-cell layer. Middle layer is the cardiac jelly (ECM - facilitates communication between the 2 layers). Some parts of the ECM are more abundant than other especially the left side of the atrium. Top layer is the myocardium (mechanical layer). Potentially single layer during cell development - actin in one cell is criss-crossing.`

    What was the observed nematic and quadratic order phenomena during heart development?
===
`Nematic vs quadratic relationship is due to cell size and heart curvature. Places of higher stress due to curvature contribute to the nematic phase structuring of the actin filaments.`

    Was the ordering observed related to the actin-myosin filaments or the sarcomeres?
===
`Related to actin filaments.`

    Where did the observed ordering happen on the heart? (Are they in specific areas?)
===
`Just the atrium for now`

    Did this ordering differ in different regions? (Atrium, Ventrical, and Atrioventricular canal)
===
`Only in the atrium. Potentially the change in heart beat function dictates the filament phase organisation. Pumping in tube shape requires circular contraction suggesting nematic while contration from atrium to ventrical is more akin to a deflating balloon and therefore may require quadratic phase.`

    Did the change from nematic to quadratic happen simultaneously or sequential during different hpfs?
===
`Assume sequential change. Defects form from nematic to quadratic.`

    (If the lines are not sarcomeres) Does this nematic ordering happen to myosin filaments also or just the actin filaments?
===
`Not sure yet`

    Do we model active nematics in 3D (mimic the curve and shape of the heart) or take a region of nematic ordering and assume 2D?
> Ask Chiu Fan
===
`The nematic to quadratic phase change is observed in the ventral (flat) side of the  heart. The lateral side (curved) does not change much and it stays nematic. From this, start with a 2D model of the ventral side of the heart showing the nematic phase change into quadratic phase. Then maybe make it 3D to include the lateral side.`

    Are we mainly focused on the significance of hydrodynamics and active nematics within modelling biological systems, featuring sarcomere organisation. Or, are we mainly focused on sarcomeres and its organisation during formation, featuring the use of hydrodynamic equations and active nematics?
> Ask Sulaimann
===
`We are focused on the zebrafish heart and only using active nematics and hydrodynamic equations as a tool to study sarcomere organisation.`

Should I be modelling the individual cells with the phase transitioning or the ventral side of the zebraheart as a whole.
===
`Model individual cells for now and then expand to the ventral view`

What are the methods required to do this?
===