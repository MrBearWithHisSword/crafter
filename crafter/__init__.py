from .env import Env
from .recorder import Recorder

def _register_environments():
  """Register Crafter environments with gym."""
  try:
    import gym
    # Check if already registered to avoid warnings
    registry = gym.envs.registry
    if isinstance(registry, dict):
      env_ids = list(registry.keys())
    else:
      env_ids = []
    
    if 'CrafterReward-v1' not in env_ids:
      gym.register(
          id='CrafterReward-v1',
          entry_point='crafter:Env',
          max_episode_steps=10000,
          kwargs={'reward': True})
    
    if 'CrafterNoReward-v1' not in env_ids:
      gym.register(
          id='CrafterNoReward-v1',
          entry_point='crafter:Env',
          max_episode_steps=10000,
          kwargs={'reward': False})
  except ImportError:
    pass
  except Exception as e:
    # Catch any other exceptions to prevent import failures
    # Registration can be retried later using _register_environments()
    pass

# Automatically register environments on import
# This will work if gym is already imported, or will be retried when gym is imported
try:
  _register_environments()
except Exception:
  # If registration fails during import, it can be retried later
  pass
