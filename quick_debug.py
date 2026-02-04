import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    # Test 1: Basic imports
    print("1. Testing imports...")
    from src.modules.intent_decompiler.analyzer import IntentDecompiler
    from src.modules.intent_decompiler.blueprint import BlueprintGenerator
    print("    Imports successful")
    
    # Test 2: Create objects
    print("\n2. Creating objects...")
    decompiler = IntentDecompiler()
    blueprint_gen = BlueprintGenerator()
    print("    Objects created")
    
    # Test 3: Analyze query
    print("\n3. Analyzing query...")
    analysis = decompiler.analyze("test query")
    print(f"    Analysis: {analysis.primary_intent}")
    
    # Test 4: Generate blueprint
    print("\n4. Generating blueprint...")
    blueprint = blueprint_gen.generate(analysis)
    print(f"    Blueprint: {len(blueprint.sections)} sections")
    
    print("\n All tests passed!")
    
except Exception as e:
    print(f"\n Error: {e}")
    import traceback
    traceback.print_exc()
