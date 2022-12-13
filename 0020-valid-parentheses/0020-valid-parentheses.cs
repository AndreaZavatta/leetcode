public class Solution {
    public bool IsValid(string s) {
        string tmp = "";
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{')
            {
                tmp += s[i];
            }
            else if (s[i] == ')' && tmp.Length > 0 && tmp[tmp.Length - 1] == '(')
            {
                tmp = tmp.Substring(0, tmp.Length - 1);
            }
            else if (s[i] == ']' && tmp.Length > 0 && tmp[tmp.Length - 1] == '[')
            {
                tmp = tmp.Substring(0, tmp.Length - 1);
            }
            else if (s[i] == '}' && tmp.Length > 0 && tmp[tmp.Length - 1] == '{')
            {
                tmp = tmp.Substring(0, tmp.Length - 1);
            }
            else
            {
                return false;
            }
        }
        if (tmp == "")
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}