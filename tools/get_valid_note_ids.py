#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取有效小红书笔记ID的辅助工具
使用方法：
1. 运行此脚本
2. 按照提示搜索关键词
3. 脚本会返回可用的笔记ID列表
4. 将这些ID复制到config/base_config.py的XHS_SPECIFIED_ID_LIST中
"""

import asyncio
import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from media_platform.xhs.client import XiaoHongShuClient
from media_platform.xhs.login import XiaoHongShuLogin
from playwright.async_api import async_playwright
import config
from tools import utils


async def get_valid_note_ids():
    """获取有效的笔记ID"""
    print("=== 小红书笔记ID获取工具 ===")
    print("此工具将帮助您获取有效的小红书笔记ID")
    
    # 获取用户输入的关键词
    keyword = input("请输入搜索关键词（例如：美食、旅行、科技等）: ").strip()
    if not keyword:
        keyword = "美食"  # 默认关键词
        print(f"使用默认关键词: {keyword}")
    
    async with async_playwright() as playwright:
        # 启动浏览器
        browser = await playwright.chromium.launch(headless=False)
        browser_context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            user_agent=utils.get_user_agent()
        )
        
        # 创建页面
        page = await browser_context.new_page()
        await page.goto("https://www.xiaohongshu.com")
        
        # 创建客户端
        headers = {
            "User-Agent": utils.get_user_agent(),
            "Cookie": "",
            "Origin": "https://www.xiaohongshu.com",
            "Referer": "https://www.xiaohongshu.com",
            "Content-Type": "application/json;charset=UTF-8"
        }
        
        xhs_client = XiaoHongShuClient(
            timeout=10,
            proxies=None,
            headers=headers,
            playwright_page=page,
            cookie_dict={}
        )
        
        # 检查登录状态
        print("检查登录状态...")
        if not await xhs_client.pong():
            print("需要登录，请扫码登录...")
            login_obj = XiaoHongShuLogin(
                login_type="qrcode",
                login_phone="",
                browser_context=browser_context,
                context_page=page,
                cookie_str=""
            )
            await login_obj.begin()
            await xhs_client.update_cookies(browser_context=browser_context)
        
        print("登录成功！开始搜索笔记...")
        
        try:
            # 搜索笔记
            notes_res = await xhs_client.get_note_by_keyword(keyword=keyword, page=1)
            
            if not notes_res.get("items"):
                print("未找到相关笔记，请尝试其他关键词")
                return
            
            print(f"找到 {len(notes_res['items'])} 个笔记，正在验证可访问性...")
            
            valid_note_ids = []
            for i, item in enumerate(notes_res["items"][:10]):  # 只检查前10个
                if item.get('model_type') in ('rec_query', 'hot_query'):
                    continue
                    
                note_id = item.get("id")
                if not note_id:
                    continue
                
                print(f"验证笔记 {i+1}/10: {note_id}")
                
                try:
                    # 尝试获取笔记详情
                    note_detail = await xhs_client.get_note_by_id(note_id)
                    if note_detail:
                        valid_note_ids.append(note_id)
                        title = note_detail.get("title", "无标题")[:30]
                        print(f"  ✓ 可访问: {title}")
                    else:
                        print(f"  ✗ 无法访问")
                except Exception as e:
                    print(f"  ✗ 访问失败: {str(e)[:50]}")
                
                # 添加延迟避免请求过快
                await asyncio.sleep(1)
            
            # 输出结果
            print("\n=== 结果 ===")
            if valid_note_ids:
                print(f"找到 {len(valid_note_ids)} 个可访问的笔记ID:")
                print("\n请将以下ID复制到 config/base_config.py 的 XHS_SPECIFIED_ID_LIST 中:")
                print("XHS_SPECIFIED_ID_LIST = [")
                for note_id in valid_note_ids:
                    print(f'    "{note_id}",')
                print("]")
            else:
                print("未找到可访问的笔记，建议：")
                print("1. 尝试其他关键词")
                print("2. 确保账号登录状态正常")
                print("3. 检查网络连接")
        
        except Exception as e:
            print(f"搜索过程中出现错误: {e}")
        
        finally:
            await browser.close()


if __name__ == "__main__":
    asyncio.run(get_valid_note_ids())
