---
layout: default
---

## 飛輪效應 測試業面

<script src="https://d3js.org/d3.v5.min.js"></script>
<style>
    text, div {
        font-family: Arial, sans-serif;
        font-size: 12px;
    }
</style>

<svg width="800" height="800" id="flywheel"></svg>

<script>
    document.addEventListener("DOMContentLoaded", function() {
        const data = [
            {
                component: "Content Creation & Quality Improvement",
                description: "Combining original content creation across all platforms and using feedback for continuous refinement."
            },
            {
                component: "Audience & Community Growth",
                description: "blablabla"
            },
            {
                component: "Monetization Through Value Proposition",
                description: "Example description here."
            },
            {
                component: "Brand Building & Collaboration",
                description: "Another description here."
            }
        ];

        const svg = d3.select("#flywheel");
        const width = +svg.attr("width");
        const height = +svg.attr("height");
        const center = [width / 2, height / 2];
        const innerRadius = Math.min(width, height) / 5;   // Shrinking the inner radius
        const outerRadius = Math.min(width, height) / 4;   // Adjusted outer radius
        const descriptionRadius = Math.min(width, height) / 3 + 10;  // Adjusting for better visibility

        function DrawBendingArrow(center, innerRadius, outerRadius, startAngle, endAngle) {
            const arc = d3.arc()
                .innerRadius(innerRadius)
                .outerRadius(outerRadius)
                .startAngle(startAngle)
                .endAngle(endAngle);

            svg.append("path")
                .attr("d", arc)
                .attr("transform", `translate(${center[0]}, ${center[1]})`)
                .attr("fill", "#555");
        }

        const angleStep = 2 * Math.PI / data.length;

        // Draw all the wheel sections first
        data.forEach((d, i) => {
            const startAngle = i * angleStep + Math.PI;  
            const endAngle = (i + 1) * angleStep + Math.PI;  
            DrawBendingArrow(center, innerRadius, outerRadius, startAngle, endAngle);
        });

        // Next, add component names and descriptions
        data.forEach((d, i) => {
            const startAngle = i * angleStep + Math.PI;  
            const endAngle = (i + 1) * angleStep + Math.PI;  
            
            const midAngle = startAngle + (endAngle - startAngle) / 2;
            const textRad = innerRadius - 20;  // Placing the component closer to the center
            const textX = center[0] + textRad * Math.cos(midAngle);
            const textY = center[1] + textRad * Math.sin(midAngle);

            const descriptionX = center[0] + descriptionRadius * Math.cos(midAngle);
            const descriptionY = center[1] + descriptionRadius * Math.sin(midAngle);

            // Adding component text with multi-line capability
            svg.append('foreignObject')
                .attr('x', textX - 50) // Centering the box
                .attr('y', textY - 50) 
                .attr('width', 100)
                .attr('height', 100)
                .append("xhtml:div")
                .style("word-wrap", "break-word")
                .style("text-align", "center")
                .style("color", "black")
                .text(d.component);

            // Adding description text with multi-line capability
            svg.append('foreignObject')
                .attr('x', descriptionX - 100) // Centering the box
                .attr('y', descriptionY - 50) 
                .attr('width', 200)
                .attr('height', 100)
                .append("xhtml:div")
                .style("word-wrap", "break-word")
                .style("text-align", "center")
                .style("color", "blue")
                .text(d.description);
        });
    });
</script>
