# 20 days (kins) in a unial
# 18 uinals in a tun
# 20 tuns in a katun
# 20 katuns in a backtun

# mayan = backtun, katun, tun, uinal, kin

def mayan_converter(backtun: object, katun: object, tun: object, uinal: object, kin: object) -> object:
    starting_days = (3 + (16 * 20) + (7 * 18 * 20) + (20 * 20 * 18 * 20) + (13 * 20 * 20 * 18 * 20))

    day = 0
    day += kin
    day += 20 * uinal
    day += tun * (18 * 20)
    day += katun * (18 * 20 * 20)
    day += backtun * (20 * 20 * 18 * 20)

    day -= starting_days
    ndays = day % 365 + 1

    jan = 31
    feb = 28 + jan
    mar = 31 + feb
    apr = 30 + mar
    may = 31 + apr
    june = 30 + may
    july = 31 + june
    aug = 31 + july
    sept = 30 + aug
    oct = 31 + sept
    nov = 30 + oct
    dec = 31 + nov

    leap_year = 0
    starting_year = 2000

    for day in range(day):
        if day % 365 == 0 and day != 0:
            feb = 28 + jan
            if starting_year % 4 == 0:
                feb -= 28 + jan
                feb += 60
                leap_year += 1

            starting_year += 1

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    print(leap_year)

    ndays = ndays - leap_year



    if ndays <= jan:
        return ndays, list[0], starting_year
    elif ndays > jan and ndays <= feb:
        return ndays - jan, list[1], starting_year
    elif ndays > feb and ndays <= mar:
        return ndays - feb, list[2], starting_year
    elif ndays > mar and ndays <= apr:
        return ndays - mar, list[3], starting_year
    elif ndays > apr and ndays <= may:
        return ndays - apr, list[4], starting_year
    elif ndays > may and ndays <= june:
        return ndays - may, list[5], starting_year
    elif ndays > june and ndays <= july:
        return ndays - june, list[6], starting_year
    elif ndays > july and ndays <= aug:
        return ndays - july, list[7], starting_year
    elif ndays > aug and ndays <= sept:
        return ndays - aug, list[8], starting_year
    elif ndays > sept and ndays <= oct:
        return ndays - sept, list[9], starting_year
    elif ndays > oct and ndays <= nov:
        return ndays - oct, list[10], starting_year
    elif ndays > nov and ndays <= dec:
        return ndays - nov, list[11], starting_year



def finding_dates():
    kin1 = 3
    uinal1 = 16
    tun1 = 7
    katun1 = 20
    backtun1 = 13

    for i in range(1000):
        find_date = mayan_converter(backtun1, katun1, tun1, uinal1, kin1)
        if find_date == (1, 2, 2000) or find_date == (1, 1, 2001):
            print(kin1, uinal1, tun1, katun1, backtun1)

        kin1 += 1
        if kin1 == 20:
            kin1 = 1
            uinal1 += 1
            if uinal1 == 18:
                uinal1 = 0
                tun1 += 1
                if tun1 == 20:
                    tun1 = 1
                    katun1 += 1
                    if katun1 == 20:
                        katun1 = 1
                        backtun1 += 1




dayzz = 20 * 20 * 20 * 18 * 20
print("20 Backtun = ", dayzz)



print(mayan_converter(13, 20, 9, 2, 9))
print(mayan_converter(13, 20, 7, 16, 3))
print(mayan_converter(13, 20, 7, 16, 12))
print(mayan_converter(13, 20, 7, 18, 3))
print(mayan_converter(13, 20, 8, 11, 8))
print(mayan_converter(13, 20, 16, 3, 4))
print(mayan_converter(13, 20, 14, 6, 9))
print(mayan_converter(14, 1, 1, 1, 1))
print(mayan_converter(14, 1, 14, 14, 14))

print(mayan_converter(13, 20, 7, 17, 14))
print(mayan_converter(13, 20, 8, 16, 9))