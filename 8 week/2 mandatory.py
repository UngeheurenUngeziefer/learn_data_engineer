import sys
print(
    len(
        list(
            dict.fromkeys(
                map(
                    str,
                    sys.stdin.read().split()
                )
            )
        )
    )
)
