class Task:
    def __init__(self, t_id: int, description: str, state: str = 'incomplete'):
        self.t_id = t_id
        self.description = description
        self.state = state
    
    def change_description(self, description: str) -> None:
        self.description = description

    def change_state(self, state: str) -> None:
        self.state = state
    
    def __repr__(self) -> str:
        return f"Task(t_id={self.t_id}, description={self.description}, state={self.state})"
