class FeedbackSystem:
    def __init__(self):
        # 定义层级结构
        self.hierarchy = {
            "村": {"next": "乡/镇"},
            "乡/镇": {"next": "区/县"},
            "区/县": {"next": "市"},
            "市": {"next": "省"},
            "省": {"next": "国家"},
            "国家": {"next": None}
        }
        # 特殊情况
        self.special_regions = {
            "直辖市": ["区/县", "国家"],  # 跳过省
            "特别行政区": ["国家"]        # 跳过市和省
        }

    def handle_feedback(self, level, issue, region_type="普通"):
        """
        处理信息反馈
        :param level: 当前反馈层级
        :param issue: 问题信息
        :param region_type: 地区类型（普通/直辖市/特别行政区）
        """
        try:
            # 输出当前层级处理情况
            print(f"【{level}】正在处理问题: {issue}")
            # 模拟某些层级未能处理问题的情况
            if self.can_handle(level):
                print(f"✅【{level}】已成功处理问题: {issue}")
                return
            else:
                print(f"⚠️【{level}】无法处理问题: {issue}")
            
            # 获取下一层级
            next_level = self.get_next_level(level, region_type)
            if next_level:
                # 递归调用反馈系统，向上反馈
                self.handle_feedback(next_level, issue, region_type)
            else:
                # 如果已经到达顶层且未解决
                print(f"❌ 问题: {issue} 未能在任何层级解决，建议手动介入。")
        except Exception as e:
            print(f"❌ 在处理层级【{level}】时出现异常: {e}")

    def can_handle(self, level):
        """
        模拟当前层级是否能处理问题
        """
        # 假设每个层级有 50% 概率处理失败
        import random
        return random.choice([True, False])

    def get_next_level(self, current_level, region_type):
        """
        根据层级和地区类型获取下一层级
        """
        if region_type in self.special_regions:
            # 特殊行政区直接跳过某些层级
            levels = self.special_regions[region_type]
            current_index = levels.index(current_level)
            return levels[current_index + 1] if current_index + 1 < len(levels) else None
        else:
            # 普通地区按层级正常向上反馈
            return self.hierarchy[current_level]["next"]


# 测试反馈系统
if __name__ == "__main__":
    system = FeedbackSystem()

    print("测试1：普通地区问题反馈")
    system.handle_feedback(level="村", issue="道路损坏问题")

    print("\n测试2：直辖市问题反馈")
    system.handle_feedback(level="区/县", issue="垃圾处理问题", region_type="直辖市")

    print("\n测试3：特别行政区问题反馈")
    system.handle_feedback(level="村", issue="公共安全问题", region_type="特别行政区")
