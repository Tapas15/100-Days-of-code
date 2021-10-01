//  Created by Philipp Muellauer on 02/10/2020.
//

import XCTest

class CalculatorTests: XCTestCase {
    
    var calc : Calculator!
  
    override func setUp() {
        super.setUp()
        calc = Calculator()
        
    }
    
    override func tearDown() {
//        something
    }
    
  
    func testAddCheck() {
        XCTAssertEqual(calc.add(1,1),2, "Should evaluate to 2")
    }
}

// Call Tests
TestRunner().runTests(testClass: CalculatorTests.self)
