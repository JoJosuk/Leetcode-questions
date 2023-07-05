// Main function
function main() {
    const f = createHelloWorld();
    const result = f();
    console.log(result); // Output: "Hello World"
  }
  
  // Function definition
  var createHelloWorld = function() {
    return function(...args) {
      return "Hello World";
    };
  };
  
  // Invoke the main function
  main();
  