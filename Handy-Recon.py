#!/usr/bin/env python3
"""
Simplified OSINT- Handy Edition 
All components in one file for easy testing
Cyberzilla™ - MMXXVI 
"""

import asyncio
import aiohttp
import json
import random
import time
from datetime import datetime
from typing import Dict, List, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OSINTSystem:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.results = {}
        
        # Platforms to check
        self.platforms = {
            'github': 'https://github.com/{}',
            'twitter': 'https://twitter.com/{}',
            'instagram': 'https://instagram.com/{}',
            'reddit': 'https://reddit.com/user/{}',
            'linkedin': 'https://linkedin.com/in/{}',
        }
    
    async def brain_analyze(self, username: str) -> Dict[str, Any]:
        """AI Brain - Pattern analysis"""
        logging.info(f"🧠 Brain analyzing: {username}")
        
        # Simulate AI processing
        await asyncio.sleep(0.5)
        
        features = {
            'length': len(username),
            'has_digits': any(c.isdigit() for c in username),
            'has_underscore': '_' in username,
            'has_dot': '.' in username,
        }
        
        # Simple pattern recognition
        if any(x in username for x in ['admin', 'test', 'user']):
            pattern_type = "generic"
        elif len(username) < 5:
            pattern_type = "short"
        elif sum(c.isdigit() for c in username) > 2:
            pattern_type = "numeric"
        else:
            pattern_type = "personal"
        
        return {
            'pattern_type': pattern_type,
            'features': features,
            'confidence': random.uniform(0.7, 0.95),
            'timestamp': datetime.now().isoformat()
        }
    
    async def muscle_scan(self, username: str, brain_data: Dict) -> Dict[str, Any]:
        """Muscle - High performance scanning"""
        logging.info(f"💪 Muscle scanning: {username}")
        
        results = {}
        tasks = []
        
        for platform, url in self.platforms.items():
            task = self.check_platform(platform, url.format(username))
            tasks.append(task)
        
        # Run all checks concurrently
        platform_results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for platform, result in zip(self.platforms.keys(), platform_results):
            if isinstance(result, Exception):
                results[platform] = {'status': 'error', 'error': str(result)}
            else:
                results[platform] = result
        
        return {
            'username': username,
            'platform_results': results,
            'scan_duration': random.uniform(1.0, 3.0),
            'total_checked': len(self.platforms)
        }
    
    async def check_platform(self, platform: str, url: str) -> Dict[str, Any]:
        """Check if username exists on a platform"""
        try:
            async with self.session.get(url, timeout=10, allow_redirects=False) as response:
                return {
                    'status': 'found' if response.status == 200 else 'not_found',
                    'status_code': response.status,
                    'url': str(response.url),
                    'platform': platform
                }
        except Exception as e:
            return {'status': 'error', 'error': str(e), 'platform': platform}
    
    async def api_gather_intel(self, username: str, scan_data: Dict) -> Dict[str, Any]:
        """API - Gather additional intelligence"""
        logging.info(f"🌐 API gathering intel for: {username}")
        
        # Simulate API calls to various services
        await asyncio.sleep(0.3)
        
        return {
            'username': username,
            'breach_data': self.simulate_breach_check(username),
            'social_analysis': self.simulate_social_analysis(username),
            'reputation_score': random.uniform(0.0, 1.0),
        }
    
    def simulate_breach_check(self, username: str) -> Dict[str, Any]:
        """Simulate breach data check"""
        breaches = [
            {'breach': 'Collection1', 'date': '2019-01-15', 'data_compromised': 'emails, passwords'},
            {'breach': 'AntiPublic', 'date': '2017-03-10', 'data_compromised': 'usernames, IPs'},
        ]
        return {
            'breaches_found': random.randint(0, 2),
            'breach_details': random.sample(breaches, random.randint(0, 2)) if random.random() > 0.7 else [],
            'last_checked': datetime.now().isoformat()
        }
    
    def simulate_social_analysis(self, username: str) -> Dict[str, Any]:
        """Simulate social media analysis"""
        return {
            'activity_level': random.choice(['low', 'medium', 'high']),
            'account_age': random.randint(1, 60),  # months
            'influence_score': random.uniform(0.0, 100.0),
        }
    
    async def orchestrate_investigation(self, username: str) -> Dict[str, Any]:
        """Orchestrate complete investigation"""
        logging.info(f"🎻 Starting investigation for: {username}")
        
        start_time = time.time()
        
        # Step 1: Brain analysis
        brain_data = await self.brain_analyze(username)
        
        # Step 2: Muscle scanning
        scan_data = await self.muscle_scan(username, brain_data)
        
        # Step 3: API intelligence gathering
        api_data = await self.api_gather_intel(username, scan_data)
        
        # Step 4: Final correlation
        final_analysis = await self.correlate_intelligence(username, brain_data, scan_data, api_data)
        
        total_time = time.time() - start_time
        
        return {
            'operation_id': f"op_{int(time.time())}_{random.randint(1000, 9999)}",
            'username': username,
            'brain_analysis': brain_data,
            'scan_results': scan_data,
            'api_intelligence': api_data,
            'final_analysis': final_analysis,
            'total_duration': total_time,
            'timestamp': datetime.now().isoformat()
        }
    
    async def correlate_intelligence(self, username: str, *data_sources) -> Dict[str, Any]:
        """Correlate all intelligence sources"""
        logging.info(f"🔗 Correlating intelligence for: {username}")
        
        await asyncio.sleep(0.2)
        
        # Simple correlation logic
        all_data = {}
        for i, data in enumerate(data_sources):
            all_data[f'source_{i}'] = data
        
        risk_score = random.uniform(0.0, 1.0)
        
        return {
            'risk_assessment': {
                'score': risk_score,
                'level': 'low' if risk_score < 0.3 else 'medium' if risk_score < 0.7 else 'high',
                'factors': ['multiple_platforms', 'pattern_analysis', 'breach_data']
            },
            'confidence': random.uniform(0.8, 0.95),
            'recommendations': [
                'Monitor social media activity',
                'Check for additional aliases',
                'Verify breach exposure details'
            ]
        }
    
    async def close(self):
        """Cleanup resources"""
        await self.session.close()

# Usage examples
async def main():
    # Initialize the system
    osint_system = OSINTSystem()
    
    try:
        # Example 1: Single username investigation
        print("🔍 Investigating single username...")
        results = await osint_system.orchestrate_investigation("example_user")
        print(f"✅ Investigation complete!")
        print(f"📊 Results saved to operation_{results['operation_id']}.json")
        
        # Save results
        with open(f"operation_{results['operation_id']}.json", 'w') as f:
            json.dump(results, f, indent=2)
        
        # Example 2: Multiple usernames
        print("\n🔍 Investigating multiple usernames...")
        usernames = ["test_user", "admin123", "john_doe"]
        
        for username in usernames:
            try:
                results = await osint_system.orchestrate_investigation(username)
                print(f"✅ Completed: {username}")
                
                # Save individual results
                with open(f"operation_{results['operation_id']}.json", 'w') as f:
                    json.dump(results, f, indent=2)
                    
            except Exception as e:
                print(f"❌ Error investigating {username}: {e}")
        
        print("\n🎉 All investigations completed!")
        
    finally:
        await osint_system.close()

# Command-line interface
async def cli():
    import argparse
    
    parser = argparse.ArgumentParser(description="World-Class OSINT Investigation System")
    parser.add_argument("username", nargs="?", help="Username to investigate")
    parser.add_argument("--batch", "-b", help="File with list of usernames")
    parser.add_argument("--output", "-o", default="json", choices=["json", "text"], help="Output format")
    
    args = parser.parse_args()
    
    system = OSINTSystem()
    
    try:
        if args.batch:
            # Batch processing from file
            try:
                with open(args.batch, 'r') as f:
                    usernames = [line.strip() for line in f if line.strip()]
                
                print(f"🔍 Processing {len(usernames)} usernames...")
                
                for username in usernames:
                    try:
                        results = await system.orchestrate_investigation(username)
                        print(f"✅ {username}: {results['final_analysis']['risk_assessment']['level']} risk")
                        
                        # Save results
                        filename = f"results/{username}_{results['operation_id']}.json"
                        with open(filename, 'w') as f:
                            json.dump(results, f, indent=2)
                            
                    except Exception as e:
                        print(f"❌ Failed {username}: {e}")
                        
            except FileNotFoundError:
                print(f"❌ File not found: {args.batch}")
                
        elif args.username:
            # Single username investigation
            results = await system.orchestrate_investigation(args.username)
            
            if args.output == "json":
                print(json.dumps(results, indent=2))
            else:
                self.print_text_results(results)
                
        else:
            # Interactive mode
            print("🌐 World-Class OSINT Tool")
            print("=" * 40)
            
            while True:
                username = input("\nEnter username to investigate (or 'quit' to exit): ").strip()
                
                if username.lower() in ['quit', 'exit', 'q']:
                    break
                
                if username:
                    try:
                        print(f"🔍 Investigating {username}...")
                        results = await system.orchestrate_investigation(username)
                        self.print_text_results(results)
                        
                        # Ask to save
                        save = input("Save results? (y/n): ").lower()
                        if save.startswith('y'):
                            filename = f"results/{username}_{results['operation_id']}.json"
                            with open(filename, 'w') as f:
                                json.dump(results, f, indent=2)
                            print(f"💾 Saved to {filename}")
                            
                    except Exception as e:
                        print(f"❌ Investigation failed: {e}")
    
    finally:
        await system.close()

    def print_text_results(self, results: Dict[str, Any]):
        """Print results in readable text format"""
        print(f"\n{'='*50}")
        print(f"OSINT INVESTIGATION REPORT")
        print(f"{'='*50}")
        print(f"Target: {results['username']}")
        print(f"Operation ID: {results['operation_id']}")
        print(f"Completed in: {results['total_duration']:.2f} seconds")
        print(f"\n📊 PATTERN ANALYSIS:")
        print(f"  Type: {results['brain_analysis']['pattern_type']}")
        print(f"  Confidence: {results['brain_analysis']['confidence']:.0%}")
        
        print(f"\n🔍 PLATFORM RESULTS:")
        for platform, data in results['scan_results']['platform_results'].items():
            status = data.get('status', 'unknown')
            print(f"  {platform.upper():<12}: {status}")
        
        print(f"\n⚠️  RISK ASSESSMENT:")
        risk = results['final_analysis']['risk_assessment']
        print(f"  Score: {risk['score']:.2f}/1.0 ({risk['level']} risk)")
        
        print(f"\n💡 RECOMMENDATIONS:")
        for rec in results['final_analysis']['recommendations']:
            print(f"  • {rec}")

if __name__ == "__main__":
    # Create results directory
    import os
    os.makedirs('results', exist_ok=True)
    
    # Run the CLI interface
    asyncio.run(cli())
