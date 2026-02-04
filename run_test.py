#!/usr/bin/env python3
"""
Simple test to verify everything works
"""

import sys
import os

# Add src to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    print(" Testing Grae-X AlgoScope Import System")
    print("=" * 50)
    
    # Test 1: Crawl Simulator
    print("\n1. Testing Crawl Simulator...")
    try:
        from src.modules.crawl_simulator import CrawlSimulator
        print("    CrawlSimulator imported successfully")
        
        # Test can create instance
        simulator = CrawlSimulator()
        print("    CrawlSimulator instance created")
    except Exception as e:
        print(f"    Error: {e}")
        return False
    
    # Test 2: Intent Decompiler  
    print("\n2. Testing Intent Decompiler...")
    try:
        from src.modules.intent_decompiler import IntentDecompiler
        print("    IntentDecompiler imported successfully")
        
        # Test can create instance and use it
        decompiler = IntentDecompiler()
        analysis = decompiler.analyze("test query")
        print(f"    Intent analysis completed: {analysis.primary_intent}")
    except Exception as e:
        print(f"    Error: {e}")
        return False
    
    print("\n" + "=" * 50)
    print(" All imports working correctly!")
    return True

if __name__ == "__main__":
    success = test_imports()
    if success:
        print("\n Grae-X AlgoScope is ready to use!")
        print("\nTry these commands:")
        print("  python -m src.cli version")
        print("  python -m src.cli intent \"how to start a blog\"")
        print("  python -m src.cli scan https://httpbin.org/html --depth=1")
    else:
        print("\n Some imports failed. Check the error messages above.")
        sys.exit(1)
