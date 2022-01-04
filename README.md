# 基于python的显著性目标检测测评工具箱

A Python-based RGB salient object detection evaluation toolbox.

## TODO

* [ ] 添加测试脚本
* [ ] 添加更详细的注释
* [ ] 优化xlsx导出的代码(? 导出CSV或许更好些? 既可以当做文本文件打开, 亦可使用Excel来进行整理)
* [x] 多进程和多线程的支持.
* [X] 剥离USVOS部分的代码, 让本仓库更专注一些, 相关代码已转移到另一个仓库[PyDavis16EvalToolbox](https://github.com/lartpang/PyDavis16EvalToolbox).
* [X] 提供对输出的结果基于某个指标进行排序的功能的支持(即, 使表格更加直观), 将会在接下来的版本中添加github-page来展示动态页面.
* [X] 基于Fan的matlab代码, 实现了一份更加快速和准确的指标代码<https://github.com/lartpang/PySODMetrics>, 已经整合到该代码中.

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

## 相关文献

```text
@inproceedings{Fmeasure,
    title={Frequency-tuned salient region detection},
    author={Achanta, Radhakrishna and Hemami, Sheila and Estrada, Francisco and S{\"u}sstrunk, Sabine},
    booktitle=CVPR,
    number={CONF},
    pages={1597--1604},
    year={2009}
}

@inproceedings{MAE,
    title={Saliency filters: Contrast based filtering for salient region detection},
    author={Perazzi, Federico and Kr{\"a}henb{\"u}hl, Philipp and Pritch, Yael and Hornung, Alexander},
    booktitle=CVPR,
    pages={733--740},
    year={2012}
}

@inproceedings{Smeasure,
    title={Structure-measure: A new way to eval foreground maps},
    author={Fan, Deng-Ping and Cheng, Ming-Ming and Liu, Yun and Li, Tao and Borji, Ali},
    booktitle=ICCV,
    pages={4548--4557},
    year={2017}
}

@inproceedings{Emeasure,
    title="Enhanced-alignment Measure for Binary Foreground Map Evaluation",
    author="Deng-Ping {Fan} and Cheng {Gong} and Yang {Cao} and Bo {Ren} and Ming-Ming {Cheng} and Ali {Borji}",
    booktitle=IJCAI,
    pages="698--704",
    year={2018}
}

@inproceedings{wFmeasure,
  title={How to eval foreground maps?},
  author={Margolin, Ran and Zelnik-Manor, Lihi and Tal, Ayellet},
  booktitle=CVPR,
  pages={248--255},
  year={2014}
}
```

## Some Tips

**For some methods, their results' names are not consistent with those of original datsets.**
* You can use the script `rename.py` in folder `tools` to modify the file names of a large number of files. **Please use with care and it is recommended to read the code carefully before use to avoid data corruption.**
* **Other useful tools**
  + Linux: `rename`
  + Windows: `Microsoft PowerToys` <https://github.com/microsoft/PowerToys>

## 编程参考

* Python_Openpyxl: <https://www.cnblogs.com/programmer-tlh/p/10461353.html>
* Python之re模块: <https://www.cnblogs.com/shenjianping/p/11647473.html>
