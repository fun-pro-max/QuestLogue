# Overview

This is a gamified task management application called "Quest Master" that transforms everyday tasks into RPG-style adventures. Users can create tasks categorized as boss fights, quests, or training sessions, complete them to earn XP, and unlock achievements. The application features a medieval fantasy theme with custom styling and interactive UI components. The application has been completely converted from React/Node.js to Python/Streamlit for easy deployment on Streamlit Cloud.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Application Architecture
- **Framework**: Python 3.11 with Streamlit 1.49+
- **Application Type**: Single-page web application with server-side Python logic
- **State Management**: Streamlit session state for persistent data during user sessions
- **Styling**: Custom CSS injected via st.markdown for medieval fantasy theme
- **UI Components**: Native Streamlit components with custom CSS styling
- **Deployment**: Streamlit Cloud for free hosting and automatic deployment

## Data Architecture
- **Data Storage**: In-memory storage using Python lists stored in Streamlit session state
- **Data Models**: Python dataclasses for Task and Achievement entities
- **Persistence**: Session-based persistence (data persists within same browser session)
- **Data Types**: Native Python types with datetime for timestamps and uuid for unique identifiers

## Data Schema

### Task Dataclass
```python
@dataclass
class Task:
    id: str          # UUID string
    title: str       # Task name
    description: str # Task details
    category: str    # 'boss', 'quest', or 'training'
    xp_reward: int   # XP points (boss: 500, quest: 200, training: 100)
    created_at: str  # ISO format datetime string
```

### Achievement Dataclass
```python
@dataclass
class Achievement:
    id: str            # UUID string
    title: str         # Achievement name (e.g., "Dragon Slayer Victor")
    description: str   # Achievement details (e.g., "Conquered: Ancient Dragon")
    icon: str          # Emoji icon (🐉, ⚔️, etc.)
    xp_earned: int     # XP points earned
    completed_at: str  # ISO format datetime string
```

## Key Design Patterns
- **Class-based Architecture**: QuestMaster class encapsulates all business logic
- **Dataclass Models**: Type-safe data structures for tasks and achievements
- **Session State Management**: Persistent data storage using Streamlit's session state
- **Component Composition**: Reusable functions for rendering UI components
- **Responsive Design**: Streamlit's native responsive layout with custom CSS enhancements

## Core Functionality
- **Task Management**: Create, complete, and delete tasks across three categories
- **Achievement System**: Automatic achievement creation for completed boss fights
- **Dynamic Icon Assignment**: Context-aware icon selection based on task titles
- **XP Calculation**: Category-based XP rewards (Boss: 500, Quest: 200, Training: 100)
- **Stats Tracking**: Real-time statistics panel with task counts and total XP

## Theme System
Custom medieval fantasy theme implemented via CSS injection:
- **Color Palette**: Primary #8B4513 (brown), Secondary #DAA520 (gold), Accent #DC143C (red), Background #2F1B14 (dark leather), Text #F5DEB3 (parchment), Success #228B22 (green)
- **Typography**: Cinzel font family for headers, Roboto for body text
- **Visual Elements**: Parchment-style cards with ornate borders, achievement badges with golden glow, scroll dividers with decorative elements
- **Animations**: CSS transitions for hover effects and component interactions

# External Dependencies

## Core Framework Dependencies
- **streamlit**: Main framework for building the web application interface
- **uuid**: UUID generation for unique task and achievement identifiers
- **datetime**: Date and time handling for timestamps
- **dataclasses**: Python data structures for Task and Achievement models

## Built-in Python Libraries
- **typing**: Type hints for better code documentation and IDE support

The application leverages Python 3.11 built-in capabilities and Streamlit's comprehensive web framework for creating interactive data applications. All dependencies are lightweight and focused on core functionality, making deployment simple and efficient on Streamlit Cloud.

## Deployment

### Local Development
```bash
streamlit run streamlit_app.py
```

### Streamlit Cloud Deployment
1. Push repository to GitHub
2. Connect to Streamlit Cloud (streamlit.io)
3. Deploy with main file: `streamlit_app.py`
4. Dependencies automatically detected from `requirements.txt`

Note: Legacy Node.js/Vite files remain in repository but are not used for Streamlit deployment.