#!/usr/bin/env python3
import os
import sys

# Import our agents
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'agents')))

try:
    import auditor
    import trust_calculator
    import refactor
except ImportError as e:
    print(f"Error importing agents: {e}")
    sys.exit(1)

def main():
    print("================================================================")
    print("   🌐 CYBER-URBAN PORTFOLIO AGENTS ORCHESTRATION PIPELINE 🌐   ")
    print("================================================================")
    
    html_path = "index.html"
    charter_path = "charte_design_portfolio.md"

    # Step 1: Baseline Audit
    print("\n[STEP 1] Running baseline Audit...")
    auditor.run_audit(html_path, charter_path)
    
    # Step 2: Baseline Trust Score
    print("\n[STEP 2] Calculating baseline Trust Score...")
    baseline_score = trust_calculator.calculate_trust_score(html_path)
    
    # Step 3: Run Refactoring
    print("\n[STEP 3] Running Automated Refactoring & Design Update...")
    refactor_results = refactor.run_refactor(html_path, charter_path)
    
    # Step 4: Final Pass Audit & Score
    print("\n[STEP 4] Re-evaluating updated portfolio metrics...")
    auditor.run_audit(html_path, charter_path)
    final_score = trust_calculator.calculate_trust_score(html_path)

    # Display Dashboard
    print("\n================================================================")
    print("   📊 PIPELINE DASHBOARD SUMMARY")
    print("================================================================")
    print(f"   Baseline Trust Score   : {baseline_score}/100")
    print(f"   Refactored Actions     : {refactor_results.get('actions', 0)} changes applied")
    print(f"   Charter Rules Status   : {'Updated' if refactor_results.get('charter_updated') else 'Up to date'}")
    print(f"   Final trust Score      : {final_score}/100")
    
    bar_len = 20
    filled = int((final_score / 100) * bar_len)
    bar = "█" * filled + "░" * (bar_len - filled)
    print(f"   Status Bar             : [{bar}] ({final_score}%)")
    
    if final_score >= 90:
        print("   Silicon Valley Status  : ✅ APPROVED - Silicon Valley Ready")
    else:
        print("   Silicon Valley Status  : ⚠️ WARNING - Needs further tuning")
    print("================================================================\n")

if __name__ == "__main__":
    main()
