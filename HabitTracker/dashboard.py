from datetime import datetime, timedelta
import database_models

def total_habits(user_id:int,db):
    return(
        db.query(database_models.Habits).filter(database_models.Habits.user_id==user_id).count()
    )

def completed_today(user_id: int, db):
    today = datetime.now().replace(hour=0,minute=0,second=0,microsecond=0)
    tomorrow = today + timedelta(days=1)
    return (
        db.query(database_models.Habit_logs).join(database_models.Habits,
            database_models.Habit_logs.habit_id == database_models.Habits.id #where condition
        )
        .filter(
            database_models.Habits.user_id == user_id,
            database_models.Habit_logs.status == True,
            database_models.Habit_logs.date >= today, #for today's log only
            database_models.Habit_logs.date < tomorrow
        )
        .count()
    )
def pending_today(total:int,completed:int):
    return total-completed