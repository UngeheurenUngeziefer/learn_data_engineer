from itertools import repeat
print(
    0 in list(
        map(
            lambda r: int(
                r()),
            repeat(
                input,
                int(
                    input(

                    )
                )
            )
        )
    )
)
