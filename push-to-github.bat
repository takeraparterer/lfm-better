@echo off
REM Push RAG System files to GitHub (Windows batch)
REM Run this script in your repository directory

echo.
echo ========================================================================
echo PUSHING RAG SYSTEM FILES TO GITHUB
echo ========================================================================
echo.

REM Configure git
echo [*] Configuring git...
git config --global user.email "you@example.com" 2>nul
git config --global user.name "Your Name" 2>nul

REM Add files
echo [*] Adding files...
git add lfm-rag-system.py ^
        lfm-rag-api.py ^
        test-rag.py ^
        test-api.py ^
        RAG-TEST-RESULTS.md ^
        RAG-TESTING-COMPLETE.md ^
        RAG-FINAL-SUMMARY.md ^
        RAG-TESTING-INDEX.md ^
        RAG-TESTING-CHECKLIST.md

if %errorlevel% equ 0 (
    echo [+] Files added successfully
) else (
    echo [-] Error adding files
    exit /b 1
)

REM Commit
echo [*] Committing...
git commit -m "RAG System Testing Complete - All tests passed (100%%), 22 axioms indexed with semantic search" ^
           -m "" ^
           -m "Features: Semantic search (77-89%% accuracy), Citation enforcement, 6 API endpoints, Full test coverage"

if %errorlevel% equ 0 (
    echo [+] Commit successful
) else (
    echo [-] Error committing
    exit /b 1
)

REM Push
echo [*] Pushing to GitHub...
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo [+] Push successful!
    echo.
    echo ========================================================================
    echo SUCCESS - RAG FILES PUSHED TO GITHUB
    echo ========================================================================
    echo.
    echo Repository: https://github.com/keithluton/lfm-
    echo.
    echo Files Pushed:
    echo   - lfm-rag-system.py
    echo   - lfm-rag-api.py
    echo   - test-rag.py
    echo   - test-api.py
    echo   - RAG-TEST-RESULTS.md
    echo   - RAG-TESTING-COMPLETE.md
    echo   - RAG-FINAL-SUMMARY.md
    echo   - RAG-TESTING-INDEX.md
    echo   - RAG-TESTING-CHECKLIST.md
    echo.
) else (
    echo [-] Error pushing
    exit /b 1
)
