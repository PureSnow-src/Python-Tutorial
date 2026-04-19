class Skill:
    def __init__(self, name: str, caster, mana_cost: int, 
                 cooldown: int, icon: str = "这是图标"):
        self.name = name                    # 名称
        self.caster = caster
        self.mana_cost = mana_cost          # 蓝耗
        self.cooldown = cooldown            # 冷却
        self.icon = icon                    # 图标
        self.current_cooldown = 0           # 当前冷却

    def show_info(self):
        """输出技能说明"""
        print(f"技能名称: {self.name}")
        print(f"蓝耗: {self.mana_cost}")
        print(f"冷却: {self.cooldown}")
        print(f"当前冷却: {self.current_cooldown}")
        print(f"图标: {self.icon}")

    def is_ready(self) -> bool:
        """判断技能是否准备完毕"""
        return self.current_cooldown == 0

    def spend_mana(self, caster) -> bool:
        """
        耗蓝
        - 如果施法者蓝量不足，返回 False
        - 否则扣蓝并返回 True
        """
        pass

    def reset_cooldown(self):
        """重置冷却"""
        self.current_cooldown = self.cooldown

    def cast(self):
        """
        技能投射
        由派生类重写
        """
        pass


class InstantSkill(Skill):
    """
    瞬发作用技能
    """
    def __init__(self, name: str, caster, mana_cost: int, cooldown: int, 
                 effect: int, icon: str = "这是图标"):
        super().__init__(name, caster, mana_cost, cooldown, icon)
        self.effect = effect    # 直接效果值，例如伤害量、治疗量

    def cast(self, target, skill_type: str):
        """
        瞬发技能投射

        target: 作用单位
        skill_type:
        - "damage" 表示伤害型
        - "heal"   表示治疗型
        """
        if skill_type == "damage":
            print((f"{self.caster}瞬发了{self.name}"
                   f"伤害为{self.effect}"))
        elif skill_type == "heal":
            print((f"{self.caster}瞬发了{self.name}"
                   f"治疗了{self.effect}"))
            
        self.current_cooldown = self.cooldown


class DurationSkill(Skill):
    """
    持续作用技能
    """
    def __init__(self, name: str, caster, mana_cost: int, cooldown: int,
        effect: int, effect_time: int, icon: str = "这是图标"):
        super().__init__(name, caster, mana_cost, cooldown, icon)

        self.effect = effect                # 作用效果值
        self.effect_time = effect_time      # 持续时间（回合数 / 秒数）

    def cast(self, target: object, skill_type: str):
        """
        持续技能释放

        caster: 施法单位
        target: 作用单位
        skill_type:
        - "dot"  持续伤害（damage over time）
        - "hot"  持续治疗（heal over time）

        这里不把完整的计时系统写出来，只做注释说明：
        实际工程里，通常会把持续效果注册到角色的 buff/debuff 列表中，
        然后由战斗系统逐回合或逐帧结算。
        """
        if skill_type == "dot":
            print((f"{self.caster}给{target}挂了一个毒"
                   f"伤害为{self.effect}"
                   f"持续时间{self.effect_time}"))
                    
        self.current_cooldown = self.cooldown

class StatusSkill(Skill):
    """
    状态类技能
    """
    def __init__(self, name: str, caster, mana_cost: int, cooldown: int,
                 status_type: str, duration: int, icon: str = "这是图标"):
        super().__init__(name, caster, mana_cost, cooldown, icon)
        self.status_type = status_type      # 状态类型
        self.duration = duration            # 持续时间

    def cast(self, target: object):
        """
        状态技能释放

        实际工程中，通常会：
        1. 先判定命中
        2. 再检查免疫、抗性、驱散规则
        3. 最后把状态挂到目标对象上
        """
        print((f"{target}获得状态{self.status_type}"
               f"施法人为{self.caster}"))
                    
        self.current_cooldown = self.cooldown

# --------------------------------------------------
# 实例化对象（对应幻灯片右侧）
# 注意：这些都是对象，不是类
# --------------------------------------------------

# 瞬发作用技能对象
execute = InstantSkill(
    name="斩杀",
    caster="player_1",
    mana_cost=30,
    cooldown=5,
    effect=80,
    icon="execute.png"
)

heal_spell = InstantSkill(
    name="治愈术",
    caster="player_2",
    mana_cost=20,
    cooldown=3,
    effect=60,
    icon="heal.png"
)

# 持续作用技能对象
poison = DurationSkill(
    name="投毒",
    caster="player_3",
    mana_cost=25,
    cooldown=6,
    effect=15,
    effect_time=4,
    icon="poison.png"
)

life_echo = DurationSkill(
    name="生命回响",
    caster="player_4",
    mana_cost=28,
    cooldown=6,
    effect=12,
    effect_time=5,
    icon="life_echo.png"
)

# 状态类技能对象
root_spell = StatusSkill(
    name="定身术",
    caster="player_5",
    mana_cost=18,
    cooldown=4,
    status_type="定身",
    duration=2,
    icon="root.png"
)

golden_body = StatusSkill(
    name="无敌金身",
    caster="player_6",
    mana_cost=40,
    cooldown=12,
    status_type="无敌",
    duration=1,
    icon="golden_body.png"
)

###### 自己做测试 #########
