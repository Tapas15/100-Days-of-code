//
//  MyTests.swift
//  MyTests
//
//  Created by Philipp Muellauer on 02/10/2020.
//

import XCTest

public class MyTests: XCTestCase {

//    public override init() {
//
//    }


    func testExample() throws {
        // This is an example of a functional test case.
        // Use XCTAssert and related functions to verify your tests produce the correct results.
    }

    func testPerformanceExample() throws {
        // This is an example of a performance test case.
        measure {
            // Put the code you want to measure the time of here.
        }
    }
    
    public func testAddCheck() {
        XCTAssertEqual(Calculator().add(1,1),2, "Should evaluate to 2")
    }

}


