import sys
import commands

if __name__ == "__main__":
    output = commands.getoutput("cat /dev/urandom | /rngtest -c 1000")

    successes = failures = None

    for line in output.split("\n"):
        if line.startswith("rngtest: FIPS 140-2 successes"):
            sp = line.split("successes: ")
            successes = int(sp[-1])

        elif line.startswith("rngtest: FIPS 140-2 failures"):
            sp = line.split("failures: ")
            failures = int(sp[-1])

        elif line.startswith("rngtest: FIPS 140-2(2001-10-10) Monobit"):
            break
    
    if failures > 5:
        sys.exit(1)
    else:
        sys.exit(0)
