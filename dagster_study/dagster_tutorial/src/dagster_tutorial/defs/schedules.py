import dagster as dg

@dg.schedule(cron_schedule="*/5 * * * 1-5", target="*", execution_timezone="America/Sao_Paulo")
def tutorial_schedule(
    context: dg.ScheduleEvaluationContext,
) -> dg.RunRequest | dg.SkipReason:
    return dg.SkipReason(
        "Skipping. Change this to return a RunRequest to launch a run."
    )