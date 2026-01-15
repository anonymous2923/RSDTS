from core.scheduler import RSDTS
from config.settings import NUM_NODES, TASK_LAMBDA, MAX_TIME_SLOTS, CHURN_RATE, V


def main():
    scheduler = RSDTS(num_nodes=NUM_NODES, task_lambda=TASK_LAMBDA, max_time_slots=MAX_TIME_SLOTS,
                      churn_rate=CHURN_RATE, V=V)
    total_regret, total_delay = scheduler.simulate()

    print(f"Total Regret: {total_regret}")
    print(f"Total Delay: {total_delay}")


if __name__ == "__main__":
    main()
