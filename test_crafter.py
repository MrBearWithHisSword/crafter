#!/usr/bin/env python3
"""诊断和测试 Crafter 环境的脚本"""

def test_crafter():
    """测试 Crafter 环境是否正常工作"""
    print("=== Crafter 环境诊断 ===\n")
    
    # 1. 导入 gym
    print("1. 导入 gym...")
    try:
        import gym
        print("   ✓ gym 导入成功")
    except Exception as e:
        print(f"   ✗ gym 导入失败: {e}")
        return False
    
    # 2. 导入 crafter
    print("\n2. 导入 crafter...")
    try:
        import crafter
        print(f"   ✓ crafter 导入成功")
        print(f"   位置: {crafter.__file__}")
    except Exception as e:
        print(f"   ✗ crafter 导入失败: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    # 3. 检查注册
    print("\n3. 检查环境注册...")
    registry = gym.envs.registry
    if isinstance(registry, dict):
        crafter_envs = [k for k in registry.keys() if 'Crafter' in k]
        print(f"   已注册的环境: {crafter_envs}")
        
        if not crafter_envs:
            print("   ⚠️ 环境未注册，尝试手动注册...")
            try:
                crafter._register_environments()
                registry = gym.envs.registry
                crafter_envs = [k for k in registry.keys() if 'Crafter' in k]
                print(f"   手动注册后: {crafter_envs}")
            except Exception as e:
                print(f"   ✗ 手动注册失败: {e}")
                import traceback
                traceback.print_exc()
                return False
    
    # 4. 测试创建环境
    print("\n4. 测试创建环境...")
    try:
        env = gym.make('CrafterReward-v1')
        print("   ✓ 成功创建 CrafterReward-v1")
        print(f"   观察空间: {env.observation_space}")
        print(f"   动作空间: {env.action_space}")
        
        # 测试重置
        obs = env.reset()
        print(f"   ✓ 环境重置成功，观察形状: {obs.shape}")
        
        return True
    except Exception as e:
        print(f"   ✗ 创建环境失败: {e}")
        import traceback
        traceback.print_exc()
        
        # 尝试直接使用 Env
        print("\n   尝试直接使用 Env 类...")
        try:
            from crafter import Env
            env = Env(reward=True)
            obs = env.reset()
            print("   ✓ 直接使用 Env 成功！")
            return True
        except Exception as e2:
            print(f"   ✗ 直接使用也失败: {e2}")
            return False

if __name__ == '__main__':
    success = test_crafter()
    if success:
        print("\n=== 所有测试通过！===")
        print("\n使用方法:")
        print("  import gym")
        print("  import crafter")
        print("  env = gym.make('CrafterReward-v1')")
    else:
        print("\n=== 测试失败 ===")
        print("\n建议:")
        print("  1. 退出 Python 会话并重新启动")
        print("  2. 确保 crafter 已正确安装: pip install -e .")
        print("  3. 如果仍有问题，使用: from crafter import Env; env = Env(reward=True)")

