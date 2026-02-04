# final_test.py
import sys
import os
import asyncio

print("=== FINAL TEST - Grae-X AlgoScope ===\n")
sys.path.insert(0, os.getcwd())

# Test all imports
print("?? Testing all imports...")
try:
    from src.modules.crawl_simulator.simulator import CrawlSimulator
    from src.modules.intent_decompiler.analyzer import IntentDecompiler
    from src.modules.intent_decompiler.blueprint import BlueprintGenerator
    from src.modules.competitor_scanner.scanner import CompetitorScanner
    from src.modules.keyword_research.analyzer import KeywordAnalyzer
    
    print("? All imports successful!")
    
    # Test basic functionality
    print("\n?? Testing basic functionality...")
    
    # 1. Test CrawlSimulator
    simulator = CrawlSimulator()
    print("   ? CrawlSimulator created")
    
    # 2. Test IntentDecompiler
    decompiler = IntentDecompiler()
    analysis = decompiler.analyze("test query")
    print(f"   ? IntentDecompiler analyzed query: {analysis.primary_intent}")
    
    # 3. Test BlueprintGenerator
    generator = BlueprintGenerator()
    blueprint = generator.generate(analysis)
    print(f"   ? BlueprintGenerator created blueprint with {len(blueprint.sections)} sections")
    
    # 4. Test KeywordAnalyzer
    keyword_analyzer = KeywordAnalyzer()
    print("   ? KeywordAnalyzer created")
    
    # 5. Test CompetitorScanner
    competitor_scanner = CompetitorScanner()
    print("   ? CompetitorScanner created")
    
    print("\n?? ALL TESTS PASSED!")
    print("Your modules are ready to use with Streamlit!")
    
except Exception as e:
    print(f"\n? Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
