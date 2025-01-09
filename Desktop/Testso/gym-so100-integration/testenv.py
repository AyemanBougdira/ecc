import gymnasium as gym
import gym_so100
import time


def visualize_env():
    # Create the environment
    env = gym.make('gym_so100/PushCube-v0', render_mode="human")
    observation, info = env.reset()

    # Run for a few steps to visualize the environment
    for _ in range(100000):  # Run for 100 steps
        # Sample a random action
        action = env.action_space.sample()

        # Take the action
        observation, reward, terminated, truncated, info = env.step(action)

        # Small delay to make visualization viewable
        time.sleep(0.05)

        if terminated or truncated:
            observation, info = env.reset()

    env.close()


if __name__ == "__main__":
    try:
        visualize_env()
    except Exception as e:
        print(f"Error occurred: {e}")