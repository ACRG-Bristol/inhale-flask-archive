from agage_archive.run import run_all


if __name__ == "__main__":

    run_all("inhale_flask",
            combined=False,
            baseline=False,
            monthly=False,
            top_level_only=True,)