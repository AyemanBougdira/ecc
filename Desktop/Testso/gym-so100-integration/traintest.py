import gymnasium as gym
import gym_so100
from lerobot.algorithms import TDMPC
from lerobot.wrappers import GymWrapper


def setup_training():
    # Créer l'environnement
    env = gym.make('gym_so100/PushCube-v0')
    env = GymWrapper(env)  # Wrapper pour la compatibilité avec lerobot

    # Configuration du TDMPC
    agent = TDMPC(
        env=env,
        episode_length=1000,
        planning_horizon=5,
        optimization_steps=3,
        num_samples=512,
        num_iterations=3,
        num_elites=64,
        min_std=0.05,
        temperature=0.5,
        momentum=0.1
    )

    # Lancer l'entraînement
    agent.train(
        num_episodes=1000,
        eval_interval=10,
        save_interval=100
    )


if __name__ == "__main__":
    setup_training()
