import os
import psutil
from surreal.main.ppo_configs import PPOLauncher

def _setup_env():
    """
    Setup the necessary environment variables
    """
    os.environ["SYMPH_PS_BACKEND_PORT"] = "7006"
    os.environ["SYMPH_PARAMETER_PUBLISH_PORT"] = "7001"
    os.environ["SYMPH_SAMPLER_FRONTEND_ADDR"] = "7004"
    os.environ["SYMPHONY_PARAMETER_SERVER_HOST"] = "127.0.0.1"
    os.environ["SYMPH_TENSORPLEX_HOST"] = "127.0.0.1"
    os.environ["SYMPH_TENSORPLEX_PORT"] = "7009"
    os.environ["SYMPH_LOGGERPLEX_HOST"] = "127.0.0.1"
    os.environ["SYMPH_LOGGERPLEX_PORT"] = "7003"
    os.environ["SYMPH_COLLECTOR_FRONTEND_HOST"] = "127.0.0.1"
    os.environ["SYMPH_COLLECTOR_FRONTEND_PORT"] = "7005"
    os.environ["SYMPH_PS_FRONTEND_HOST"] = "127.0.0.1"
    os.environ["SYMPH_PS_FRONTEND_PORT"] = "7008"
    os.environ["SYMPH_SAMPLER_FRONTEND_HOST"] = "127.0.0.1"
    os.environ["SYMPH_SAMPLER_FRONTEND_PORT"] = "7003"
    os.environ["SYMPH_SAMPLER_BACKEND_HOST"] = "127.0.0.1"
    os.environ["SYMPH_SAMPLER_BACKEND_PORT"] = "7002"
    os.environ["SYMPH_PARAMETER_PUBLISH_HOST"] = "127.0.0.1"
    os.environ["SYMPH_PARAMETER_PUBLISH_PORT"] = "7001"
    os.environ["SYMPH_COLLECTOR_BACKEND_HOST"] = "127.0.0.1"
    os.environ["SYMPH_COLLECTOR_BACKEND_PORT"] = "7007"
    os.environ["SYMPH_PREFETCH_QUEUE_HOST"] = "127.0.0.1"
    os.environ["SYMPH_PREFETCH_QUEUE_PORT"] = "7000"

temp_path = '/tmp/surreal/ddpg'
config_path = os.path.join(os.path.dirname(__file__),
                                  '../surreal/main/ppo_configs.py')

launcher = PPOLauncher()

args = [
    '--unit-test',
    '--num-agents',
    '1',
    '--env',
    #'gym:HalfCheetah-v2',
    'gym:HalfCheetahPyBulletEnv-v0',
    #'robosuite:SawyerLift',
    # 'dm_control:cartpole-balance',
    '--experiment-folder',
    str(temp_path)]
_setup_env()

launcher.setup(args)

print('Launcher setup')

agent = launcher.setup_agent(0)
agent.main_setup()

print('Agent setup')

#learner = launcher.setup_learner()
#learner.main_setup()

print('Learner setup')

for i in range(1):
    print('Iteration {}'.format(i))
    for j in range(1):
        agent.main_loop()
    #learner.main_loop()
