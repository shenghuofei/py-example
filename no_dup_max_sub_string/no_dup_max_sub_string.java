class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 0) return s.length();
        Set<Character> set = new LinkedHashSet<>();
        int j = 0;
        String res = "";
        int maxLen = 0;
        for (char str : s.toCharArray()) {
            if (!set.contains(str)) {
                set.add(str);
            } else {
                while (set.contains(str)) {
                    set.remove(s.charAt(j++));
                }
            }
            set.add(str);
            if (set.size() >= maxLen) {
                maxLen = set.size();
                String cur = "";
                for (Character a : set) {
                    cur += a;
                }
                res = cur;
            }
            System.out.println(maxLen);
        }
        return res.length();
    }
}
