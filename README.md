# 基于python的显著性目标检测测评工具箱

A Python-based RGB salient object detection evaluation toolbox.


## 特性

* 提供11项显著性目标检测指标的评估
    - F-measure-Threshold Curve
    - Precision-Recall Curve
    - MAE
    - weighted F-measure
    - S-measure
    - max/mean/adaptive F-measure
    - max/mean/adaptive E-measure
* 测试代码高度优化
    - 纯python实现, 基于numpy和各种小trick计算各项指标, 速度有保障
    - 导出特定模型的结果到xlsx文件中（2021年01月04日重新提供支持）
    - 直接支持从生成的npy文件导出latex表格代码，顺便还可以对前三的方法使用不同颜色进行标记。
    - 导出测试结果到txt文件中
    - 评估所有指定的方法, 根据评估结果绘制PR曲线和F-measure曲线

## 使用方法


**python版本的配置文件的例子可以参考 `examples` 文件夹中的 `dataset_config.py` 和 `method_config.py` .**

具体使用流程:
1. 先安装指标代码库： `pip install pysodmetrics`.
2. 配置不同数据集以及方法的路径信息：
    - 本项目依赖于json文件存放数据.
    - 但是本项目提供了`tools/info_py_to_json.py`来将python格式的信息（例子可见`examples`文件夹中的`dataset_config.py`和`method_config.py`）转换为json文件. 使用方法可见`tools/readme.md`.
    - 准备好json文件后, 建议使用提供的`tools/check_path.py`来检查下路径信息是否正常.
    - **请务必确保*数据集字典的名字*和方法中配置不同*数据集字典的名字*一致**.
3. 一切正常后, 可以开始评估了.
    - **具体关于评估以及使用评估得到的`.npy`文件来绘图的例子, 可以参考 `examples` 文件夹中的 `eval_all.py` 和 `plot_results.py` .**
4. 运行`eval_all.py`, 如无异常, 默认会在 <./results> 下生成结果文件, 并将用于绘图的信息保存到`.npy`文件中.
5. 后续可以使用`plot_results.py`来读取`.npy`文件绘制`PR`曲线和`Fm`曲线.

