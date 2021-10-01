import XCTest

public struct TestRunner{
    
    public init() {}
    
//    public func runTests(testClass: AnyClass) {
//        print("Running tests")
//        let tests = testClass as! XCTestCase.Type
//        let testSuite = tests.defaultTestSuite
//        testSuite.run()
//     }

   public func runTests(_ types: XCTestCase.Type...) {
       print("Running tests")
    //    let tests = testClass as! XCTestCase.Type
       let testSuite = XCTestSuite(name: "Required")
       testSuite.addTest(types)
       testSuite.run()
    }    
    
}