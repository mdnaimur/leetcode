function lengthOfLongestSubstring(s: string): number {
    let maxLen = 0;
    let window = new Set<string>();

    let left = 0, right = 0;

    while(right < s.length){
        console.log(`Checking: s[${right}] = '${s[right]}'`);
        while(window.has(s[right])){
            console.log(`Duplicate found: '${s[right]}'. Removing s[${left}] = '${s[left]}'`);
            window.delete(s[left]);
            left++;
        }
        window.add(s[right])
        console.log(`Added '${s[right]}' to window:`, Array.from(window));
        right++;
        maxLen = Math.max(maxLen,right-left);
        console.log(`Updated maxLen = ${maxLen}, Left = ${left}, Right = ${right}\n`);
    }
    return maxLen;
 }

// Example Usage
console.log(lengthOfLongestSubstring("abcabcbb")); 
