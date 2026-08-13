class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        n = len(s)
        M = 1 << (n - 1).bit_length()
        size = 2 * M
        
        pref_c = [0] * size
        pref_l = [0] * size
        suff_c = [0] * size
        suff_l = [0] * size
        max_l = [0] * size
        sz = [0] * size
        
        s_ord = [ord(c) for c in s]
        for i in range(n):
            node = M + i
            c = s_ord[i]
            pref_c[node] = suff_c[node] = c
            pref_l[node] = suff_l[node] = max_l[node] = sz[node] = 1
            
        for i in range(M - 1, 0, -1):
            lc, rc = 2 * i, 2 * i + 1
            sz[i] = sz[lc] + sz[rc]
            
            if sz[rc] == 0:
                pref_c[i], pref_l[i], suff_c[i], suff_l[i], max_l[i] = pref_c[lc], pref_l[lc], suff_c[lc], suff_l[lc], max_l[lc]
            elif sz[lc] == 0:
                pref_c[i], pref_l[i], suff_c[i], suff_l[i], max_l[i] = pref_c[rc], pref_l[rc], suff_c[rc], suff_l[rc], max_l[rc]
            else:
                lc_pc, lc_pl, lc_sc, lc_sl, lc_ml = pref_c[lc], pref_l[lc], suff_c[lc], suff_l[lc], max_l[lc]
                rc_pc, rc_pl, rc_sc, rc_sl, rc_ml = pref_c[rc], pref_l[rc], suff_c[rc], suff_l[rc], max_l[rc]
                l_sz, r_sz = sz[lc], sz[rc]
                
                pc = lc_pc
                pl = lc_pl + (rc_pl if lc_pl == l_sz and lc_pc == rc_pc else 0)
                
                sc = rc_sc
                sl = rc_sl + (lc_sl if rc_sl == r_sz and rc_sc == lc_sc else 0)
                
                ml = max(lc_ml, rc_ml)
                if lc_sc == rc_pc:
                    ml = max(ml, lc_sl + rc_pl)
                    
                pref_c[i], pref_l[i], suff_c[i], suff_l[i], max_l[i] = pc, pl, sc, sl, ml

        ans = []
        q_chars = [ord(c) for c in queryCharacters]
        
        for val, idx in zip(q_chars, queryIndices):
            node = M + idx
            if pref_c[node] == val:
                ans.append(max_l[1])
                continue
                
            pref_c[node] = suff_c[node] = val
            node >>= 1
            
            while node > 0:
                lc, rc = node << 1, (node << 1) | 1
                
                if sz[rc] == 0:
                    pref_c[node], pref_l[node], suff_c[node], suff_l[node], max_l[node] = pref_c[lc], pref_l[lc], suff_c[lc], suff_l[lc], max_l[lc]
                elif sz[lc] == 0:
                    pref_c[node], pref_l[node], suff_c[node], suff_l[node], max_l[node] = pref_c[rc], pref_l[rc], suff_c[rc], suff_l[rc], max_l[rc]
                else:
                    lc_pc, lc_pl, lc_sc, lc_sl, lc_ml = pref_c[lc], pref_l[lc], suff_c[lc], suff_l[lc], max_l[lc]
                    rc_pc, rc_pl, rc_sc, rc_sl, rc_ml = pref_c[rc], pref_l[rc], suff_c[rc], suff_l[rc], max_l[rc]
                    l_sz, r_sz = sz[lc], sz[rc]
                    
                    pc = lc_pc
                    pl = lc_pl + (rc_pl if lc_pl == l_sz and lc_pc == rc_pc else 0)
                    
                    sc = rc_sc
                    sl = rc_sl + (lc_sl if rc_sl == r_sz and rc_sc == lc_sc else 0)
                    
                    ml = max(lc_ml, rc_ml)
                    if lc_sc == rc_pc:
                        ml = max(ml, lc_sl + rc_pl)
                        
                    pref_c[node], pref_l[node], suff_c[node], suff_l[node], max_l[node] = pc, pl, sc, sl, ml
                
                node >>= 1
                
            ans.append(max_l[1])
            
        return ans