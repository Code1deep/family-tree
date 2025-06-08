// /app/static/js/tree.js
fetch('/data')
  .then(res => res.json())
  .then(data => {
    const stratify = d3.stratify()
      .id(d => d.id)
      .parentId(d => d.parent);
    
    const root = stratify(data);
    const treeLayout = d3.tree().size([800, 600]);
    treeLayout(root);

    const svg = d3.select("svg")
      .attr("viewBox", "0 0 800 800");

    svg.selectAll('line')
      .data(root.links())
      .enter()
      .append('line')
      .attr('x1', d => d.source.x)
      .attr('y1', d => d.source.y)
      .attr('x2', d => d.target.x)
      .attr('y2', d => d.target.y)
      .attr('class', 'link');

    const node = svg.selectAll('g.node')
      .data(root.descendants())
      .enter()
      .append('g')
      .attr('class', 'node')
      .attr('transform', d => `translate(${d.x},${d.y})`);

    node.append('rect')
      .attr('x', -50).attr('y', -20)
      .attr('width', 100).attr('height', 40)
      .attr('rx', 10).attr('ry', 10);

    node.append('text')
      .attr('dy', 5)
      .attr('text-anchor', 'middle')
      .text(d => d.data.name);
  });
