nums = [14, 131, 196, 451, 472, 694, 735, 769, 999, 1012, 1040, 1065, 1079, 1091, 1190, 1252, 1276, 1279, 1284, 1296, 1299, 1309, 1312, 1324, 1327, 1344, 1356, 1369, 1383, 1392, 1400, 1405, 1406, 1425, 1436, 1437, 1451, 1453, 1458, 1461, 1474, 1495, 1508, 1522, 1528, 1531, 1540, 1544, 1546, 1550, 1551, 1552, 1554, 1556, 1565, 1566, 1571, 1572, 1574, 1581, 1582, 1589, 1590, 1594, 1600, 1602, 1606, 1607, 1609, 1611, 1613, 1619, 1621, 1623, 1627, 1630, 1631, 1632, 1635, 1638, 1639, 1640, 1641, 1643, 1644, 1645, 1646, 1657, 1659, 1661, 1662, 1669, 1670, 1674, 1681, 1683, 1686, 1687, 1688, 1694, 1700, 1705, 1708, 1710, 1711, 1716, 1717, 1718, 1720, 1724, 1727, 1728, 1734, 1737, 1743, 1745, 1748, 1753, 1754, 1756, 1763, 1766, 1767, 1768, 1769, 1771, 1776, 1777, 1780, 1782, 1786, 1787, 1788, 1790, 1792, 1795, 1798, 1799, 1802, 1809, 1817, 1823, 1824, 1825, 1830, 1837, 1846, 1852, 1855, 1856, 1857, 1860, 1865, 1868, 1870, 1878, 1884, 1887, 1893, 1894, 1897, 1902, 1905, 1914, 1917, 1919, 1921, 1930, 1932, 1933, 1934, 1935, 1936, 1942, 1945, 1948, 1959, 1960, 1963, 1966, 1969, 1972, 1974, 1975, 1977, 1982, 1989, 1990, 1991, 1993, 1994, 1995, 1997, 2000, 2001, 2002, 2003, 2005, 2008, 2009]

def AddendsMultiplier():
    for num in nums:
        for secnum in nums:
            for thirdnum in nums:
                if (num + secnum + thirdnum == 2020):
                    print("Addends of 2020: " + str(num) + ", " + str(secnum) + ", " + str(thirdnum))
                    return(num * secnum * thirdnum)

print(AddendsMultiplier())