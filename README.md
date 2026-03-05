# translucent_alignment

An example is given in `main.py`.
The graphs can be visualized using `trg.view()` (relating to the DRG in our work) and `tasg.view()` (relating to the MG in our work).
To use these methods, an output folder needs to be created.

A more general view is given in the evaluation.



## Insurance claim log
Below, an overview of translucent variants in the event log is provided: 

- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>f</ins>cdgh⟩ × 80
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 18
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 285
- ⟨<ins>a</ins>, <ins>f</ins>bgh⟩ × 95
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>g</ins>efh, <ins>e</ins>fgh⟩ × 21
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩ × 3
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>f</ins>egh⟩ × 30
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>f</ins>egh⟩ × 3
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>h</ins>dfg, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 11
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>f</ins>egh⟩ × 20
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩ × 173
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩ × 7
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>f</ins>dgh⟩ × 35
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>h</ins>efg, <ins>e</ins>fgh⟩     
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>g</ins>dfh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 22
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>f</ins>bgh⟩ × 6
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 13
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>g</ins>efh, <ins>e</ins>fgh⟩ × 14
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>f</ins>dgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 13
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩ × 14
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>g</ins>efh, <ins>f</ins>egh⟩ × 3
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>f</ins>bgh⟩ × 7
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>g</ins>dfh, <ins>d</ins>fgh, <ins>f</ins>egh⟩ × 2
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩ × 7
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>f</ins>cdgh⟩ × 6
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>f</ins>egh⟩ × 2
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>g</ins>dfh, <ins>f</ins>dgh⟩ × 3
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 21
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>f</ins>cdgh⟩ × 4
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>h</ins>efg, <ins>e</ins>fgh⟩ × 8
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩ × 11
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>c</ins>dfgh, <ins>f</ins>dgh⟩ × 2
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 2 
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>h</ins>dfg, <ins>d</ins>fgh, <ins>f</ins>egh⟩ × 3
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>h</ins>efg, <ins>e</ins>fgh⟩
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩     
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>h</ins>efg, <ins>e</ins>fgh⟩ × 11
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>f</ins>cdgh⟩ × 5
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>c</ins>dfgh, <ins>h</ins>dfg, <ins>d</ins>fgh, <ins>e</ins>fgh⟩    
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>h</ins>efg, <ins>g</ins>efh, <ins>e</ins>fgh⟩ × 3 
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>g</ins>efh, <ins>h</ins>efg, <ins>e</ins>fgh⟩
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 2
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>f</ins>cdgh⟩ × 3
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 2
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>h</ins>dfg, <ins>f</ins>dgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>h</ins>efg, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>g</ins>dfh, <ins>d</ins>fgh, <ins>h</ins>efg, <ins>e</ins>fgh⟩     
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>f</ins>dgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>g</ins>dfh, <ins>h</ins>dfg, <ins>f</ins>dgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>g</ins>cdfh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 2
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>h</ins>dfg, <ins>g</ins>dfh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩     
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>f</ins>dgh⟩
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>d</ins>cfgh, <ins>e</ins>fgh⟩
- ⟨<ins>a</ins>, <ins>g</ins>bfh, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>h</ins>dfg, <ins>d</ins>fgh, <ins>e</ins>fgh⟩     
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>g</ins>bfh, <ins>f</ins>bgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>f</ins>cdgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>d</ins>cfgh, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>h</ins>cdfg, <ins>c</ins>dfgh, <ins>f</ins>dgh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>g</ins>efh, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>h</ins>bfg, <ins>b</ins>fgh, <ins>c</ins>dfgh, <ins>g</ins>dfh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ × 2 
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>h</ins>cdfg, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>f</ins>egh⟩
- ⟨<ins>a</ins>, <ins>b</ins>fgh, <ins>g</ins>cdfh, <ins>h</ins>cdfg, <ins>c</ins>dfgh, <ins>d</ins>fgh, <ins>e</ins>fgh⟩ 
