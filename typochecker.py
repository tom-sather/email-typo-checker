#!/usr/bin/env python3
"""
Email Domain Validator - Checks email addresses for common domain typos
Usage: python3 checker.py list.csv
"""

import csv
import sys
import re
from typing import List, Dict, Any, Tuple, Optional


class EmailDomainValidator:
    def __init__(self, common_domains: List[str] = None):
        """Initialize with optional list of common domains"""
        # Start with default domains or use provided list
        default_domains = [
            # Common email providers
            'gmail.com',
            'icloud.com',
            'protonmail.com',
            'mail.com',
            'zoho.com',
            'yandex.com',
            
            # Microsoft domains
            'outlook.com', 'outlook.co', 'outlook.bz', 'outlook.cl', 'outlook.co.cr', 
            'outlook.com.ar', 'outlook.com.br', 'outlook.com.pe', 'outlook.com.py',
            'outlook.ec', 'outlook.hn', 'outlook.ht', 'outlook.mx', 'outlook.pa',
            'outlook.uy', 'outlook.at', 'outlook.be', 'outlook.bg', 'outlook.cm',
            'outlook.co.il', 'outlook.com.es', 'outlook.com.gr', 'outlook.com.hr',
            'outlook.com.tr', 'outlook.com.ua', 'outlook.cz', 'outlook.de', 'outlook.dk',
            'outlook.es', 'outlook.fr', 'outlook.hu', 'outlook.ie', 'outlook.it',
            'outlook.lv', 'outlook.pt', 'outlook.ro', 'outlook.si', 'outlook.sk',
            'outlook.co.id', 'outlook.co.nz', 'outlook.co.th', 'outlook.com.au',
            'outlook.com.vn', 'outlook.in', 'outlook.jp', 'outlook.kr', 'outlook.la',
            'outlook.my', 'outlook.ph', 'outlook.pk', 'outlook.sa', 'outlook.sg',
            
            'hotmail.com', 'hotmail.ca', 'hotmail.at', 'hotmail.ba', 'hotmail.be',
            'hotmail.ch', 'hotmail.co.at', 'hotmail.co.il', 'hotmail.co.ug',
            'hotmail.co.uk', 'hotmail.co.za', 'hotmail.com.ly', 'hotmail.com.pl',
            'hotmail.com.ru', 'hotmail.com.tr', 'hotmail.de', 'hotmail.dk', 'hotmail.ee',
            'hotmail.es', 'hotmail.fi', 'hotmail.fr', 'hotmail.gr', 'hotmail.hu',
            'hotmail.ie', 'hotmail.it', 'hotmail.lt', 'hotmail.lu', 'hotmail.lv',
            'hotmail.ly', 'hotmail.mw', 'hotmail.no', 'hotmail.pt', 'hotmail.rs',
            'hotmail.se', 'hotmail.sh', 'hotmail.sk', 'hotmail.ua', 'hotmail.ac',
            'hotmail.bb', 'hotmail.bs', 'hotmail.cl', 'hotmail.co.ve', 'hotmail.com.ar',
            'hotmail.com.bo', 'hotmail.com.br', 'hotmail.com.do', 'hotmail.com.tt',
            'hotmail.com.ve', 'hotmail.as', 'hotmail.co.id', 'hotmail.co.in',
            'hotmail.co.jp', 'hotmail.co.kr', 'hotmail.co.nz', 'hotmail.co.pn',
            'hotmail.co.th', 'hotmail.com.au', 'hotmail.com.hk', 'hotmail.com.my',
            'hotmail.com.ph', 'hotmail.com.sg', 'hotmail.com.tw', 'hotmail.com.uz',
            'hotmail.com.vn', 'hotmail.hk', 'hotmail.jp', 'hotmail.la', 'hotmail.mn',
            'hotmail.my', 'hotmail.net.fj', 'hotmail.ph', 'hotmail.pn', 'hotmail.sg',
            'hotmail.vu',
            
            'live.com', 'live.ca', 'live.cl', 'live.com.ar', 'live.com.co', 'live.com.mx',
            'live.com.pe', 'live.com.ve', 'live.at', 'live.be', 'live.ch', 'live.co.uk',
            'live.co.za', 'live.com.pt', 'live.de', 'live.dk', 'live.fi', 'live.fr',
            'live.ie', 'live.it', 'live.nl', 'live.no', 'live.ru', 'live.se', 'live.cn',
            'live.co.in', 'live.co.kr', 'live.com.au', 'live.com.my', 'live.com.ph',
            'live.com.pk', 'live.com.sg', 'live.hk', 'live.in', 'live.jp', 'live.ph',
            
            'msn.com', 'msn.nl', 'passport.com', 'webtv.net', 'windowslive.com',
            'windowslive.es',
            
            # Yahoo domains
            'yahoo.com', 'yahoo.com.ar', 'yahoo.at', 'yahoo.com.au', 'yahoo.be',
            'yahoo.bg', 'yahoo.com.br', 'yahoo.ca', 'yahoo.cl', 'yahoo.com.co',
            'yahoo.cz', 'yahoo.de', 'yahoo.dk', 'yahoo.ee', 'yahoo.es', 'yahoo.fi',
            'yahoo.fr', 'yahoo.gr', 'yahoo.com.hk', 'yahoo.com.hr', 'yahoo.hu',
            'yahoo.co.hu', 'yahoo.co.id', 'yahoo.ie', 'yahoo.co.il', 'yahoo.in',
            'yahoo.co.in', 'yahoo.it', 'yahoo.co.jp', 'yahoo.ne.jp', 'ybb.ne.jp',
            'yahoo.co.kr', 'yahoo.lt', 'yahoo.lv', 'yahoo.com.mx', 'yahoo.com.my',
            'yahoo.nl', 'yahoo.no', 'yahoo.co.nz', 'yahooxtra.co.nz', 'yahoo.com.pe',
            'yahoo.com.ph', 'yahoo.pl', 'yahoo.pt', 'yahoo.ro', 'yahoo.rs', 'yahoo.ru',
            'yahoo.se', 'yahoo.com.sg', 'yahoo.si', 'yahoo.sk', 'yahoo.co.th',
            'yahoo.com.tr', 'yahoo.com.tw', 'yahoo.com.ua', 'yahoo.co.uk', 'yahoo.com.ve',
            'yahoo.com.vn', 'yahoo.co.za', 'rocketmail.com', 'ymail.com', 'ygm.com',
            'y7mail.com',
            
            # AOL domains
            'aol.com', 'aol.com.ar', 'aol.at', 'aol.com.au', 'aol.be', 'aol.com.br',
            'aol.cl', 'aol.com.co', 'aol.cz', 'aol.de', 'aol.dk', 'aol.es', 'aol.fi',
            'aol.fr', 'aol.hk', 'aol.in', 'aol.it', 'aol.jp', 'aol.kr', 'aol.nl',
            'aol.co.nz', 'aol.pl', 'aol.ru', 'aol.se', 'aol.tw', 'aol.com.tr',
            'aol.co.uk', 'aol.com.ve', 'aim.com', 'compuserve.com', 'cs.com',
            'netscape.com', 'wow.com', 'games.com', 'goowy.com',
            
            # Verizon family domains
            'verizon.net', 'verizonmedia.it', 'bellatlantic.net', 'citlink.net',
            'frontiernet.net', 'gte.net', 'netscape.net', 'frontier.com',
            
            # Canadian domains
            'rogers.com',
            
            # Other domains
            'sky.com', 'wild4music.com', 'wmconnect.com'
        ]
        
        self.common_domains = common_domains or default_domains

    def levenshtein_distance(self, a: str, b: str) -> int:
        """Calculate the Levenshtein distance between two strings"""
        if len(a) < len(b):
            return self.levenshtein_distance(b, a)

        if len(b) == 0:
            return len(a)

        previous_row = range(len(b) + 1)
        for i, a_char in enumerate(a):
            current_row = [i + 1]
            for j, b_char in enumerate(b):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (a_char != b_char)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def find_closest_domain(self, input_domain: str, threshold: int = 2) -> Dict[str, Any]:
        """Find the closest matching domain from common domains list"""
        # If the domain is already in our list, it's valid
        if input_domain in self.common_domains:
            return {
                "is_valid": True,
                "input_domain": input_domain,
                "suggested_domain": None,
                "distance": 0
            }

        closest_match = None
        min_distance = float('inf')

        # Find the closest match
        for domain in self.common_domains:
            distance = self.levenshtein_distance(input_domain, domain)
            
            if distance < min_distance:
                min_distance = distance
                closest_match = domain

        # If the closest match is within our threshold, suggest it
        if min_distance <= threshold:
            return {
                "is_valid": False,
                "input_domain": input_domain,
                "suggested_domain": closest_match,
                "distance": min_distance
            }

        # No close match found
        return {
            "is_valid": False,
            "input_domain": input_domain,
            "suggested_domain": None,
            "distance": min_distance
        }

    def validate_email(self, email: str) -> Dict[str, Any]:
        """Validate an email address and check for common domain typos"""
        # Basic email format validation
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
        if not re.match(email_regex, email):
            return {
                "is_valid": False,
                "email": email,
                "error": "Invalid email format"
            }

        # Extract the domain part
        parts = email.split('@')
        domain_part = parts[1]
        local_part = parts[0]

        # Check if the domain is potentially misspelled
        domain_check = self.find_closest_domain(domain_part)

        # If domain is valid or has a suggested correction
        if domain_check["is_valid"]:
            return {
                "is_valid": True,
                "email": email,
                "correction_needed": False
            }
        elif domain_check["suggested_domain"]:
            corrected_email = f"{local_part}@{domain_check['suggested_domain']}"
            max_len = max(len(domain_part), len(domain_check["suggested_domain"]))
            confidence = 1 - (domain_check["distance"] / max_len) if max_len > 0 else 0
            
            return {
                "is_valid": False,
                "email": email,
                "correction_needed": True,
                "suggested_email": corrected_email,
                "suggested_domain": domain_check["suggested_domain"],
                "confidence": confidence
            }

        # No suggestion found, but basic email format is valid
        return {
            "is_valid": True,
            "email": email,
            "correction_needed": False,
            "note": "Unknown domain but valid email format"
        }

    def process_csv(self, csv_file: str, output_file: str = None) -> List[Dict[str, Any]]:
        """Process a CSV file containing email addresses"""
        results = []
        email_column = None
        email_column_index = None

        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                # Try to detect if it's a real CSV or just a list of emails
                sample = file.read(1024)
                file.seek(0)
                
                # Determine if this is a CSV with headers or just a list of emails
                if ',' in sample:
                    # Treat as CSV
                    reader = csv.reader(file)
                    headers = next(reader, None)
                    
                    # Try to find an email column if headers exist
                    if headers:
                        for i, header in enumerate(headers):
                            if 'email' in header.lower():
                                email_column = header
                                email_column_index = i
                                break
                    
                    # Process each row
                    for row in reader:
                        if email_column_index is not None and email_column_index < len(row):
                            email = row[email_column_index].strip()
                        else:
                            # If no email column found, assume the first column
                            email = row[0].strip() if row else ""
                        
                        if email:
                            results.append(self.validate_email(email))
                else:
                    # Treat as simple list of emails, one per line
                    for line in file:
                        email = line.strip()
                        if email:
                            results.append(self.validate_email(email))
                            
        except Exception as e:
            print(f"Error processing file: {e}")
            return []

        # Write results to output file if specified
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    
                    # Write header
                    writer.writerow(["Email", "Valid", "Suggested Correction", "Confidence"])
                    
                    # Write data
                    for result in results:
                        writer.writerow([
                            result["email"],
                            "Yes" if result["is_valid"] and not result.get("correction_needed") else "No",
                            result.get("suggested_email", ""),
                            f"{result.get('confidence', 0)*100:.1f}%" if "confidence" in result else ""
                        ])
            except Exception as e:
                print(f"Error writing output file: {e}")

        return results

    def print_results_summary(self, results: List[Dict[str, Any]]) -> None:
        """Print a summary of the validation results"""
        total = len(results)
        valid = sum(1 for r in results if r["is_valid"] and not r.get("correction_needed"))
        needs_correction = sum(1 for r in results if r.get("correction_needed"))
        invalid = total - valid - needs_correction
        
        print(f"\nSummary:")
        print(f"Total emails processed: {total}")
        print(f"Valid emails: {valid} ({valid/total*100:.1f}%)")
        print(f"Emails with suggested corrections: {needs_correction} ({needs_correction/total*100:.1f}%)")
        print(f"Invalid emails: {invalid} ({invalid/total*100:.1f}%)")
        
        if needs_correction > 0:
            print("\nSuggested corrections:")
            for result in results:
                if result.get("correction_needed"):
                    confidence = result.get("confidence", 0) * 100
                    print(f"  {result['email']} → {result['suggested_email']} ({confidence:.1f}% confident)")


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <csv_file> [output_file]")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    validator = EmailDomainValidator()
    print(f"Processing {input_file}...")
    results = validator.process_csv(input_file, output_file)
    
    validator.print_results_summary(results)
    
    if output_file:
        print(f"Detailed results saved to {output_file}")


if __name__ == "__main__":
    main()
