import streamlit as st
import uuid
from datetime import datetime
from dataclasses import dataclass

# Configure page
st.set_page_config(
    page_title="Quest Master - RPG Task Manager",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

@dataclass
class Task:
    id: str
    title: str
    description: str
    category: str  # 'boss', 'quest', 'training'
    xp_reward: int
    created_at: str

@dataclass  
class Achievement:
    id: str
    title: str
    description: str
    icon: str
    xp_earned: int
    completed_at: str

class QuestMaster:
    def __init__(self):
        self.init_session_state()
        self.load_data()
    
    def init_session_state(self):
        """Initialize session state variables"""
        if 'tasks' not in st.session_state:
            st.session_state.tasks = []
        if 'achievements' not in st.session_state:
            st.session_state.achievements = []
        if 'initialized' not in st.session_state:
            st.session_state.initialized = True
    
    def load_data(self):
        """Load data from session state"""
        # In Streamlit, session state persists during the browser session
        pass
    
    def save_data(self):
        """Save data (session state automatically persists)"""
        # Session state automatically persists in Streamlit
        pass
    
    def get_icon_for_boss(self, title: str) -> str:
        """Generate achievement icons based on boss fight titles"""
        title_lower = title.lower()
        if 'dragon' in title_lower: return '🐉'
        elif 'titan' in title_lower or 'frost' in title_lower: return '🏔️'
        elif 'lich' in title_lower or 'arcane' in title_lower: return '🔮'
        elif 'demon' in title_lower or 'fiend' in title_lower: return '👹'
        elif 'beast' in title_lower or 'wolf' in title_lower: return '🐺'
        elif 'skeleton' in title_lower or 'bone' in title_lower: return '💀'
        else: return '⚔️'
    
    def create_task(self, title: str, description: str, category: str):
        """Create a new task"""
        xp_rewards = {'boss': 500, 'quest': 200, 'training': 100}
        task = Task(
            id=str(uuid.uuid4()),
            title=title,
            description=description,
            category=category,
            xp_reward=xp_rewards[category],
            created_at=datetime.now().isoformat()
        )
        st.session_state.tasks.append(task)
        self.save_data()
        return task
    
    def complete_task(self, task_id: str):
        """Complete a task and create achievement if boss fight"""
        task = next((t for t in st.session_state.tasks if t.id == task_id), None)
        if not task:
            return
        
        # Create achievement for boss fights
        if task.category == 'boss':
            achievement = Achievement(
                id=str(uuid.uuid4()),
                title=f"{task.title} Victor",
                description=f"Conquered: {task.description}",
                icon=self.get_icon_for_boss(task.title),
                xp_earned=task.xp_reward,
                completed_at=datetime.now().isoformat()
            )
            st.session_state.achievements.append(achievement)
        
        # Remove task
        st.session_state.tasks = [t for t in st.session_state.tasks if t.id != task_id]
        self.save_data()
        return True
    
    def delete_task(self, task_id: str):
        """Delete a task"""
        st.session_state.tasks = [t for t in st.session_state.tasks if t.id != task_id]
        self.save_data()
    
    def delete_achievement(self, achievement_id: str):
        """Delete an achievement"""
        st.session_state.achievements = [a for a in st.session_state.achievements if a.id != achievement_id]
        self.save_data()

# CSS for medieval theme - exact replication of original design
def inject_medieval_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Roboto:wght@300;400;500;700&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #2F1B14 0%, #1a0f0a 100%);
        background-attachment: fixed;
        min-height: 100vh;
        color: #F5DEB3;
    }
    
    .medieval-header {
        font-family: 'Cinzel', serif;
        font-size: 4rem;
        font-weight: bold;
        color: #DAA520;
        text-align: center;
        text-shadow: 0 0 10px rgba(218, 165, 32, 0.8);
        margin: 2rem 0;
    }
    
    .medieval-subtitle {
        font-family: 'Cinzel', serif;
        font-size: 1.2rem;
        color: #F5DEB3;
        text-align: center;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .parchment-card {
        background: linear-gradient(145deg, #f4e6d0 0%, #e8d5b7 100%);
        border: 3px solid #8B4513;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 
            inset 0 1px 3px rgba(139, 69, 19, 0.3),
            0 8px 25px rgba(0, 0, 0, 0.4),
            0 2px 6px rgba(0, 0, 0, 0.2);
        color: #8B4513;
        position: relative;
    }
    
    .parchment-card::before {
        content: '';
        position: absolute;
        top: -2px;
        left: -2px;
        right: -2px;
        bottom: -2px;
        background: linear-gradient(45deg, #DAA520, #B8860B, #DAA520);
        border-radius: inherit;
        z-index: -1;
    }
    
    .boss-fight-card {
        border-left: 6px solid #DC143C;
        background: linear-gradient(135deg, #ffebee 0%, #f8bbd9 100%);
    }
    
    .quest-card {
        border-left: 6px solid #DAA520;
        background: linear-gradient(135deg, #fffbf0 0%, #f5e6a3 100%);
    }
    
    .training-card {
        border-left: 6px solid #228B22;
        background: linear-gradient(135deg, #f1f8e9 0%, #c8e6c9 100%);
    }
    
    .achievement-badge {
        background: radial-gradient(circle, #DAA520 0%, #B8860B 70%);
        border: 2px solid #8B4513;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 
            0 0 20px rgba(218, 165, 32, 0.5),
            inset 0 1px 3px rgba(255, 255, 255, 0.3);
        color: white;
        margin: 1rem 0;
        position: relative;
        transition: transform 0.3s ease;
    }
    
    .achievement-badge:hover {
        transform: scale(1.05);
    }
    
    .section-header {
        font-family: 'Cinzel', serif;
        font-size: 2rem;
        font-weight: bold;
        text-align: center;
        margin: 2rem 0 1rem 0;
    }
    
    .boss-header { color: #DC143C; }
    .quest-header { color: #DAA520; }
    .training-header { color: #228B22; }
    .achievement-header { color: #DAA520; }
    
    .scroll-divider {
        background: linear-gradient(90deg, transparent 0%, #8B4513 20%, #8B4513 80%, transparent 100%);
        height: 2px;
        margin: 2rem auto;
        position: relative;
        width: 300px;
    }
    
    .scroll-divider::before,
    .scroll-divider::after {
        content: '⚜';
        color: #DAA520;
        font-size: 1.5rem;
        position: absolute;
        top: -12px;
    }
    
    .scroll-divider::before { left: 10%; }
    .scroll-divider::after { right: 10%; }
    
    .stats-panel {
        background: linear-gradient(145deg, #f4e6d0 0%, #e8d5b7 100%);
        border: 2px solid #8B4513;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 0.5rem;
        text-align: center;
        color: #8B4513;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
    }
    
    .stats-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    
    .stats-number {
        font-family: 'Cinzel', serif;
        font-size: 2rem;
        font-weight: bold;
        margin: 0.5rem 0;
    }
    
    .stats-label {
        font-size: 0.9rem;
        opacity: 0.8;
        font-family: 'Cinzel', serif;
    }
    
    .task-title {
        font-family: 'Cinzel', serif;
        font-size: 1.2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    
    .task-description {
        margin-bottom: 1rem;
        line-height: 1.4;
    }
    
    .task-reward {
        font-size: 0.85rem;
        opacity: 0.8;
        font-weight: bold;
    }
    
    .category-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-family: 'Cinzel', serif;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    
    .boss-badge {
        background-color: rgba(220, 20, 60, 0.2);
        color: #DC143C;
    }
    
    .quest-badge {
        background-color: rgba(218, 165, 32, 0.2);
        color: #DAA520;
    }
    
    .training-badge {
        background-color: rgba(34, 139, 34, 0.2);
        color: #228B22;
    }
    
    /* Streamlit component styling */
    .stButton button {
        background: linear-gradient(145deg, #8B4513 0%, #5d2e0c 100%);
        border: 2px solid #DAA520;
        color: #F5DEB3;
        border-radius: 8px;
        font-family: 'Cinzel', serif;
        transition: all 0.3s ease;
        font-weight: bold;
    }
    
    .stButton button:hover {
        background: linear-gradient(145deg, #a0521a 0%, #6b3410 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background-color: white;
        color: #8B4513;
        border: 2px solid #8B4513;
        border-radius: 8px;
    }
    
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #DAA520;
        box-shadow: 0 0 0 2px rgba(218, 165, 32, 0.2);
    }
    
    /* Hide Streamlit elements */
    .stApp > header {
        background-color: transparent;
    }
    
    .stApp > .main {
        background-color: transparent;
    }
    
    #MainMenu {
        visibility: hidden;
    }
    
    .footer {
        visibility: hidden;
    }
    
    .stHeader {
        background-color: transparent;
    }
    </style>
    """, unsafe_allow_html=True)

def render_task_card(task: Task, quest_master: QuestMaster, key_prefix: str):
    """Render individual task card with medieval styling"""
    category_styles = {
        'boss': {
            'class': 'boss-fight-card',
            'color': '#DC143C', 
            'icon': '⚔️',
            'badge': 'Epic Challenge',
            'badge_class': 'boss-badge'
        },
        'quest': {
            'class': 'quest-card',
            'color': '#DAA520', 
            'icon': '🗺️',
            'badge': 'Noble Mission',
            'badge_class': 'quest-badge'
        }, 
        'training': {
            'class': 'training-card',
            'color': '#228B22', 
            'icon': '🛡️',
            'badge': 'Skill Development',
            'badge_class': 'training-badge'
        }
    }
    
    style = category_styles[task.category]
    
    with st.container():
        st.markdown(f"""
        <div class="parchment-card {style['class']}">
            <div class="task-title" style="color: {style['color']};">
                {style['icon']} {task.title}
            </div>
            <div class="category-badge {style['badge_class']}">{style['badge']}</div>
            <div class="task-description">{task.description}</div>
            <div class="task-reward">Reward: {task.xp_reward} XP</div>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Complete", key=f"complete_{key_prefix}_{task.id}", type="primary"):
                quest_master.complete_task(task.id)
                st.success("Quest completed! Victory is yours!")
                st.rerun()
        with col2:
            if st.button("❌ Delete", key=f"delete_{key_prefix}_{task.id}"):
                quest_master.delete_task(task.id)
                st.rerun()

def render_achievement_badge(achievement: Achievement, quest_master: QuestMaster):
    """Render individual achievement badge"""
    completed_date = datetime.fromisoformat(achievement.completed_at).strftime("%B %d, %Y")
    
    with st.container():
        st.markdown(f"""
        <div class="achievement-badge">
            <div style="font-size: 3rem; margin-bottom: 1rem;">{achievement.icon}</div>
            <h3 style="font-family: 'Cinzel', serif; margin-bottom: 0.5rem; font-weight: bold;">
                {achievement.title}
            </h3>
            <p style="margin-bottom: 1rem; opacity: 0.9;">{achievement.description}</p>
            <div style="font-size: 0.8rem; opacity: 0.8;">
                📅 Completed: {completed_date}<br>
                ⭐ {achievement.xp_earned} XP Earned
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🗑️ Remove Achievement", key=f"del_ach_{achievement.id}"):
            quest_master.delete_achievement(achievement.id)
            st.rerun()

def main():
    # Inject medieval CSS styling
    inject_medieval_css()
    
    # Initialize Quest Master
    quest_master = QuestMaster()
    
    # Header Section
    st.markdown('<div class="medieval-header">⚔️ Quest Master ⚔️</div>', unsafe_allow_html=True)
    st.markdown('<div class="medieval-subtitle">"Forge your destiny through valorous deeds and noble quests"</div>', unsafe_allow_html=True)
    st.markdown('<div class="scroll-divider"></div>', unsafe_allow_html=True)
    
    # Task Creation Form
    st.markdown('<div class="section-header" style="color: #8B4513;">📜 Chronicle New Adventures</div>', unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="parchment-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            title = st.text_input("🖋️ Quest Title", placeholder="Enter your noble quest...", key="quest_title")
        with col2:
            category = st.selectbox("🏴 Adventure Type", 
                                  options=['boss', 'quest', 'training'],
                                  format_func=lambda x: {
                                      'boss': '⚔️ Boss Fight - Epic Challenge', 
                                      'quest': '🗺️ Quest - Noble Mission',
                                      'training': '🛡️ Training - Skill Development'
                                  }[x],
                                  key="quest_category")
        
        description = st.text_area("📋 Quest Description", 
                                 placeholder="Describe the trials and rewards that await...",
                                 key="quest_description")
        
        if st.button("🌟 Embark on Adventure", type="primary", key="create_quest"):
            if title and description and category:
                quest_master.create_task(title, description, category)
                st.success("Quest created! Your new adventure awaits in the quest log.")
                st.rerun()
            else:
                st.error("Please fill in all fields to create your quest.")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="scroll-divider"></div>', unsafe_allow_html=True)
    
    # Task Categories Display
    tasks = st.session_state.tasks
    boss_fights = [t for t in tasks if t.category == 'boss']
    quests = [t for t in tasks if t.category == 'quest']  
    training = [t for t in tasks if t.category == 'training']
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="section-header boss-header">⚔️ Boss Fights</div>', unsafe_allow_html=True)
        if boss_fights:
            for task in boss_fights:
                render_task_card(task, quest_master, "boss")
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #888; font-family: 'Cinzel', serif;">
                ⚔️<br>No boss fights await...
            </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="section-header quest-header">🗺️ Quests</div>', unsafe_allow_html=True)
        if quests:
            for task in quests:
                render_task_card(task, quest_master, "quest")
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #888; font-family: 'Cinzel', serif;">
                🗺️<br>No quests available...
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="section-header training-header">🛡️ Training</div>', unsafe_allow_html=True)
        if training:
            for task in training:
                render_task_card(task, quest_master, "training")
        else:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #888; font-family: 'Cinzel', serif;">
                🛡️<br>No training sessions planned...
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('<div class="scroll-divider"></div>', unsafe_allow_html=True)
    
    # Stats Panel
    total_xp = sum(a.xp_earned for a in st.session_state.achievements)
    
    stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)
    
    with stat_col1:
        st.markdown(f"""
        <div class="stats-panel">
            <div class="stats-icon" style="color: #DC143C;">⚔️</div>
            <div class="stats-number">{len(boss_fights)}</div>
            <div class="stats-label">Boss Fights</div>
        </div>
        """, unsafe_allow_html=True)
    
    with stat_col2:
        st.markdown(f"""
        <div class="stats-panel">
            <div class="stats-icon" style="color: #DAA520;">🗺️</div>
            <div class="stats-number">{len(quests)}</div>
            <div class="stats-label">Active Quests</div>
        </div>
        """, unsafe_allow_html=True)
    
    with stat_col3:
        st.markdown(f"""
        <div class="stats-panel">
            <div class="stats-icon" style="color: #228B22;">🛡️</div>
            <div class="stats-number">{len(training)}</div>
            <div class="stats-label">Training Sessions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with stat_col4:
        st.markdown(f"""
        <div class="stats-panel">
            <div class="stats-icon" style="color: #DAA520;">⭐</div>
            <div class="stats-number">{total_xp:,}</div>
            <div class="stats-label">Total XP</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="scroll-divider"></div>', unsafe_allow_html=True)
    
    # Hall of Victories (Achievement Gallery)
    st.markdown('<div class="section-header achievement-header">🏆 Hall of Victories 👑</div>', unsafe_allow_html=True)
    
    achievements = st.session_state.achievements
    if achievements:
        # Display achievements in a grid
        cols_per_row = 3
        for i in range(0, len(achievements), cols_per_row):
            cols = st.columns(cols_per_row)
            for j, achievement in enumerate(achievements[i:i+cols_per_row]):
                with cols[j]:
                    render_achievement_badge(achievement, quest_master)
    else:
        st.markdown("""
        <div style="text-align: center; padding: 3rem; border: 2px dashed #DAA520; border-radius: 15px; margin: 2rem 0; background: rgba(218, 165, 32, 0.05);">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🏆</div>
            <p style="color: #DAA520; font-family: 'Cinzel', serif; font-size: 1.1rem;">
                Complete Boss Fights to earn eternal glory!
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="scroll-divider"></div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: rgba(47, 27, 20, 0.5); border-top: 2px solid #DAA520; border-radius: 15px;">
        <div class="scroll-divider" style="width: 200px;"></div>
        <p style="font-family: 'Cinzel', serif; color: #DAA520; margin: 2rem 0 1rem 0; font-size: 1.1rem;">
            "May your quests be legendary and your victories eternal"
        </p>
        <small style="color: #888;">Quest Master RPG Task Manager © 2024</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()