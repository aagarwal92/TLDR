var jsonData = null;
var cluster = null;
var vis = null;
var diagonal = null;
var blah = null;
var count = 0;
var rentList = ""
var w =0,
    h = 0,
    i = 0,
    duration = 0;
    
d3.json("REDDITS.json", function(json) {
  json.x0 = 800;
  json.y0 = 0;

 jsonData = json;
 //console.log(jsonData);

  getHeight(jsonData);
 //update(root = json)

    
    
// cluster = d3.layout.cluster()
  //  .size([h, w - 160]);

 diagonal = d3.svg.diagonal()
    .projection(function(d) { return [d.y, d.x]; });

 vis = d3.select("#chart").append("svg:svg")
    .attr("width", w)
    .attr("height", h)
  .append("svg:g")
    .attr("transform", "translate(100,0)");

 update(root = jsonData); 
});


function update(source) {
  
    var nodes = cluster.nodes(source).reverse();
  
  
     var node = vis.selectAll("g.node")
         .data(nodes)
       .enter().append("svg:g")
         .attr("class", "node")
         .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; })

      node.append("svg:text")
          .attr("dx", function(d) { return d.children ? -8 : 8; })
          .attr("dy", 3)
          .attr("text-anchor", function(d) { return d.children ? "end" : "start"; })
          .text(function(d) { return d.name; });
  
  // Update the nodes…
  var node = vis.selectAll("circle.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });
      
      //d.szie>1000 if statement. d,.class "node med(css class defined in html).
  /*   Code trying to add circle size changes
    nodes.forEach(function(d) {
        
      if (d.size >= 1000 && d.size <= 5000)
      {
      //  console.log(d); 
  
  var node = vis.selectAll("circle.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });
        
      node.select("circle.node");
      
      node.enter().append("svg:circle")
      .attr("class", "node2")
      .attr("cx", function(d) { return source.y0; })
      .attr("cy", function(d) { return source.x0; })
      .text(function (d) {return d.name; })
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      .on("mouseover", mouseon)
      .on("mouseout", mouseoff)
      .on("click", click)
    .transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; });
     }
    
  if (d.size >= 5001)
      {
       // console.log(d); 
  
    var node = vis.d("circle.node")
      .data(nodes, function(d) { return d.id || (d.id = ++i); });
        
      node.select("circle.node");
      
      node.enter().append("svg:circle")
      .attr("class", "node3")
      .attr("cx", function(d) { return source.y0; })
      .attr("cy", function(d) { return source.x0; })
      .text(function (d) {return d.name; })
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      .on("mouseover", mouseon)
      .on("mouseout", mouseoff)
      .on("click", click)
    .transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; });
     }
    
    
    });
  */
    
/* Another attempt at the same thing
 
 if (nodes[i].size >= 1000 && nodes[i].size <= 2000)
    {
      node.enter().append("svg:circle")
      .attr("class", "node")
      .attr("cx", function(d) { return source.y0; })
      .attr("cy", function(d) { return source.x0; })
      .text(function (d) {return d.name; })
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      .on("mouseover", mouseon)
      .on("mouseout", mouseoff)
      .on("click", click)
    .transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; });
    }
    
    if (nodes[i].size >= 2001 && nodes[i].size <= 5000)
    {
      node.enter().append("svg:circle")
      .attr("class", "node2")
      .attr("cx", function(d) { return source.y0; })
      .attr("cy", function(d) { return source.x0; })
      .text(function (d) {return d.name; })
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      .on("mouseover", mouseon)
      .on("mouseout", mouseoff)
      .on("click", click)
    .transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; });
    }
    
    if (nodes[i].size >= 5001)
    {
      node.enter().append("svg:circle")
      .attr("class", "node3")
      .attr("cx", function(d) { return source.y0; })
      .attr("cy", function(d) { return source.x0; })
      .text(function (d) {return d.name; })
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      .on("mouseover", mouseon)
      .on("mouseout", mouseoff)
      .on("click", click)
    .transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; });
    }

*/
  // Enter any new nodes at the parent's previous position.
 
    node.enter().append("svg:circle")
      .attr("class", "node")
      .attr("cx", function(d) { return source.y0; })
      .attr("cy", function(d) { return source.x0; })
      .text(function (d) {return d.name; })
      .attr("r", 4.5)
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; })
      .on("mouseover", mouseon)
      .on("mouseout", mouseoff)
      .on("click", click)
    .transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; });
    
  
  node.enter().append("svg:text")
      .attr("dx", function(d) { return d.children ? -8 : 8; })
      .attr("dy", 3)
      .attr("text-anchor", function(d) { return d.children ? "end" : "start"; })
      //.text(function(d) { return d.name; })
      //.text(function(d) { return d.name; });
  // Transition nodes to their new position.
  node.transition()
      .duration(duration)
      .attr("cx", function(d) { return d.y; })
      .attr("cy", function(d) { return d.x; })
      .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

  // Transition exiting nodes to the parent's new position.
  node.exit().transition()
      .duration(duration)
      .attr("cx", function(d) { return source.y; })
      .attr("cy", function(d) { return source.x; })
      .remove();

  // Update the links…
  var link = vis.selectAll("path.link")
      .data(cluster.links(nodes), function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("svg:path", "circle")
      .attr("class", "link")
      .attr("d", function(d) {
        var o = {x: source.x0, y: source.y0};
        return diagonal({source: o, target: o});
      })
    .transition()
      .duration(duration)
      .attr("d", diagonal);

  // Transition links to their new position.
  link.transition()
      .duration(duration)
      .attr("d", diagonal);

  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
      .attr("d", function(d) {
        var o = {x: source.x, y: source.y};
        return diagonal({source: o, target: o});
      })
      .remove();

  // Stash the old positions for transition.
  nodes.forEach(function(d) {
    d.x0 = d.x;
    d.y0 = d.y;
  });
 // return source;
 getHeight(source);
}

function resetNames ()
{
  var nodes = cluster.nodes(jsonData).reverse();
    var node = vis.selectAll("g.node")
       .data(nodes)
       .remove(); 
  
  
  for (i = 0; i< nodes.length ;i++)
  {
    nodes[i] = "";
    //console.log(i);
  }
  if (nodes[i]== "")
  {
    return true;
   console.log("true");
  }
}

function getHeight(x)
{
  w = 960;
  i = 0;
  duration = 500;
  
  //console.log(x.children.length);
  h = (x.children.length*40);
  
  //console.log("height is"+ h);
  
//  return h;

  cluster = d3.layout.cluster()
    .size([h+500, w - 250]);
  window.scrollTo( 0,0) ;
}

var temp = null;

function click (d)
{
  if (d==undefined)
  {
    return;
  }
  if (d.children == null)
  {
    console.log("Node has no children");
    return;
  }
  
  //console.log(d._children);
  if (d.name != "Reddit")
  {
    //console.log("yes")
    resetNames();
  }
  console.log(d.parent.parent);
  blah = d;
  blahParent = d.parent;
  root = d;
  temp = root.parent;
  getHeight(d);
  update(root);
  
  var subsInfo = "";
  subsInfo = d.name + "</br>" + "Subscriber Count: " + d.size;
  
  showRentList2();
  console.log(d.name);
  count == 0; 
  if(d.name == "Reddit"){
    document.getElementById("subredditinfo").style.display = "none";
    document.getElementById("subscribers").style.display = "none";
    document.getElementById("redditinfo").style.display = "block";
    //document.getElementById("subscribers").style.display = "block";

  }
  else
  {
    document.getElementById("redditinfo").style.display = "none";
    document.getElementById("subredditinfo").style.display = "block";
    document.getElementById("subscribers").style.display = "block";
    showRentList2();
    var rentList2 = document.getElementById('subredditinfo');
    rentList2.innerHTML = rentList + "</br>" + " ↓ " + "</br>" + d.name;
    var subs = document.getElementById('subscribers');
    subs.innerHTML = subsInfo;
    //rentList2.innerHTML = "Parent1<br/>Parent2<br/>Parent3";
  }
  
  function showRentList()
  {
    var rentList = ""
    var tempRent = d.parent;
      if (tempRent.name == "Reddit")
      {
        rentList = d.name + "</br>" +  " ↓ " + "</br>" + tempRent.name;
        return rentList;
      }
      for (x = 0; x < 20; x++)
      {
        
        rentList = rentList + d.name + "</br>" +  " ↓ " + "</br>" + tempRent.name + "</br>" +  " ↓ " + "</br>";
        if (tempRent.parent != undefined)
        {
          tempRent = tempRent.parent;
          if (tempRent.name == "Reddit")
          {
            rentList = rentList  + tempRent.name;
            return rentList;
          }
        }
        //return rentList;
      }
   
      return rentList;
      console.log("goes into rentlist")
      
      
      
      //return rentList2;
     // var blah = "L;KFLASDFJKL;ASJDFKL;ASJDFL;AKFJ";
      //return blah;
  }
}
function back2()
{
  if (blah==null)
  {
    return;
  }
    resetNames();
    getHeight(blahParent);
    update(blahParent);
   

  
  if (blahParent.name == "Reddit")
  {
    document.getElementById("subredditinfo").style.display = "none";
    document.getElementById("redditinfo").style.display = "block";
  }
  else
  { 
    
        
    if (blahParent.parent != null)
    {
      blahParent = blahParent.parent;
    }

    //showRentList2();
    document.getElementById("subredditinfo").style.display = "block";
    document.getElementById("subscribers").style.display = "block";
    document.getElementById("redditinfo").style.display = "none";
    var subs = document.getElementById('subscribers');
    subs.innerHTML = showSubs();
    var rentList2 = document.getElementById('subredditinfo');
    rentList2.innerHTML = showRentList2();

   count ++;
  console.log(count);
  
  }
}

function moveUpParentList(x)
{
  var clickedParent = null;
    //rentList.forEach(function(item) {
      //clickedParent = item[x];
    //})
    
    for (i=0; i<rentList.length; i++)
    {
      console.log("GOES IN")
      clickedParent = rentList[i];
            console.log("GOES IN2")

      console.log(rentList[i]);
    }
    //console.log(clickedParent);
}

function showSubs()
{
  var blah2 = blah;
  var subsInfo2 = "";
  
    for (i = 0; i < count; i++)
    {
      blah2 = blah2.parent;
    }
    subsInfo2 = blah2.parent.name + "</br>" + "SUBS Count: " + blah2.parent.size;
    return subsInfo2;
    
}
/*
function showRentList3()
{
  var rentList = "";
  var blah2 = blah;
  var tempRent;
   
  for (i = 0; i < count; i++)
  {
    blah2 = blah2.parent;
  }
  
  if (blah2.parent.parent.name == "Reddit")
  {
    var bolded = blah2.parent.name;
    bolded = bolded.bold();
    rentList = blah2.parent.parent.name + "</br>" +  " ↓ " + "</br>" + bolded;
      return rentList;
  }
  
  tempRent = blah2.parent;
  for (x = 0; x < 20; x++)
  {
    rentList = rentList + tempRent.parent.name + "</br>" +  " ↓ " + "</br>" + blah2.parent.name + "</br>" +  " ↓ " + "</br>";
    if (tempRent.parent != undefined)
    {
       tempRent = blah2.parent.parent;
        if (tempRent.name == "Reddit")
        {
          //var bolded = blah2.parent.name;
          //bolded = bolded.bold();
          rentList = tempRent.name + "</br>" +  " ↓ " + "</br>" + rentList;
          return rentList;
        }
    }
  }
  return rentList;
  
}

*/
function showRentList2()
  {
    //var rentList = ""
    var blah2 = blah;
    for (i = 0; i < count; i++)
    {
      blah2 = blah2.parent;
    }
     var tempRent = blah2; 

   /*   if (tempRent.name == "Reddit")
      {
        rentList = tempRent.name + "</br>" +  " ↓ " + "</br>" +  blah.name;
        return rentList;
      }*/
      
      {
      for (x = 0; x < 20; x++)
      {
        if (x == 0)
        {
          rentList = tempRent.parent.name;
          if (tempRent.parent != undefined)
        {
          tempRent = tempRent.parent;
          if (tempRent.name == "Reddit")
          {
           // rentList = tempRent.name + "</br>" +  " ↓ " + "</br>" + rentList;
      //     var rentList2 = rentList.substring(0, rentList.length-2);
            return rentList;
          }
        }
        }
        else
        {
          
      
        rentList = tempRent.parent.name + "</br>" +  " ↓ " + "</br>" + rentList;// +  tempRent.parent.name; //+ "</br>" +  " ↓ " + "</br>" + blah2.parent.name ;
        if (tempRent.parent != undefined)
        {
          tempRent = tempRent.parent;
          if (tempRent.name == "Reddit")
          {
           // rentList = tempRent.name + "</br>" +  " ↓ " + "</br>" + rentList;
      //     var rentList2 = rentList.substring(0, rentList.length-2);
            return rentList;
          }
        }
       // blah2 = blah2.parent;
        //return rentList;
        }
      }
      }
     // var rentList2 = rentList.substring(0, rentList.length-2);
      return rentList;
  }



    //var rentList = ""

function mouseon(d)
{
  function kids()
  {
    if (d.children != null)
    {
      
    //console.log(d.children);
    var childs = d.children;
    var finalChilds = "";

    childs.forEach(function(child)
    {
      if (child.name != undefined)
      {
      finalChilds = finalChilds + "{" + child.name + "}  ";
      }
    });
    //console.log(finalChilds);
    return finalChilds;
    }    
  }

    var rentList = ""
    var tempRent = d.parent;
   function parentals()
   {
      if (tempRent.name == "Reddit")
      {
        rentList = "{" + tempRent.name  + "}  ";
        return rentList;
      }
      for (x = 0; x < 20; x++)
      {
        
        rentList = rentList + "{" + tempRent.name + "}  ";
        if (tempRent.parent != undefined)
        {
          tempRent = tempRent.parent;
          if (tempRent.name == "Reddit")
          {
            rentList = rentList + "{" + tempRent.name + "}  ";
            return rentList;
          }
        }
      } 
    return rentList;
   }
  
  tooltip.show('<strong> Sub-Reddit Name: </strong>' + d.name +
               '<br /><strong> Subscriber Count: </strong>' + d.size +
               '<br /><strong> Parent List: </stong>' + parentals() + 
               '<br /><strong> Children: </strong>' + kids() +
               '<br /> Click here' + <a> www.reddit.com/r/ </a> + ' to view the actual reddit page.' +
               '<br /> You may also click on this Sub-Reddit to view a tree of its children and view further details.');
  //tooltip.show('Testing  123');
  //update(d);
}

function test()
{
  console.log("test");
  console.log(rentList)
}

function mouseoff(d)
{
  tooltip.hide();
}

function nodeSize()
{
  var size = 150;
  return size;
}
function reset()
{
  window.location.reload();
  count == 0;
}