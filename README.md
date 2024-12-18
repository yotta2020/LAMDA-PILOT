## 🎉 Introduction

Welcome to PILOT, a pre-trained model-based continual learning toolbox <a href="https://arxiv.org/abs/2309.07117">[Paper]</a>. On the one hand, PILOT implements some state-of-the-art class-incremental learning algorithms based on pre-trained models, such as L2P, DualPrompt, and CODA-Prompt. On the other hand, PILOT also fits typical class-incremental learning algorithmswithin the context of pre-trained models to evaluate their effectiveness.

欢迎来到 PILOT，一个基于预训练模型的持续学习工具箱，PILOT 实现了一些基于预训练模型的最先进的类增量学习算法，如 L2P、DualPrompt 和 CODA-Prompt。另一方面，PILOT 还将典型的类增量学习算法 (_e.g._, FOSTER, and MEMO)拟合在预训练模型的上下文中，以评估其有效性。

## 🌟 Methods Reproduced

- `FineTune`: Baseline method which simply updates parameters on new tasks.
- `iCaRL`: iCaRL: Incremental Classifier and Representation Learning. CVPR 2017 [[paper](https://arxiv.org/abs/1611.07725)]
- `Coil`: Co-Transport for Class-Incremental Learning. ACMMM 2021 [[paper](https://arxiv.org/abs/2107.12654)]
- `DER`: DER: Dynamically Expandable Representation for Class Incremental Learning. CVPR 2021 [[paper](https://arxiv.org/abs/2103.16788)]
- `FOSTER`: Feature Boosting and Compression for Class-incremental Learning. ECCV 2022 [[paper](https://arxiv.org/abs/2204.04662)]
- `MEMO`: A Model or 603 Exemplars: Towards Memory-Efficient Class-Incremental Learning. ICLR 2023 Spotlight [[paper](https://openreview.net/forum?id=S07feAlQHgM)]
- `L2P`: Learning to Prompt for Continual Learning. CVPR 2022 [[paper](https://arxiv.org/abs/2112.08654)]
- `DualPrompt`: DualPrompt: Complementary Prompting for Rehearsal-free Continual Learning. ECCV 2022 [[paper](https://arxiv.org/abs/2204.04799)]
- `CODA-Prompt`: CODA-Prompt: COntinual Decomposed Attention-based Prompting for Rehearsal-Free Continual Learning. CVPR 2023 [[paper](https://arxiv.org/abs/2211.13218)]
- `RanPAC`: RanPAC: Random Projections and Pre-trained Models for Continual Learning. NeurIPS 2023 [[paper](https://arxiv.org/abs/2307.02251)]
- `LAE`: A Unified Continual Learning Framework with General Parameter-Efficient Tuning. ICCV 2023 [[paper](https://arxiv.org/abs/2303.10070)]
- `SLCA`: SLCA: Slow Learner with Classifier Alignment for Continual Learning on a Pre-trained Model. ICCV 2023 [[paper](https://arxiv.org/abs/2303.05118)]
- `FeCAM`: FeCAM:Exploiting the Heterogeneity of Class Distributions in Exemplar-Free Continual Learning. NeurIPS 2023 [[paper](https://proceedings.neurips.cc/paper_files/paper/2023/file/15294ba2dcfb4521274f7aa1c26f4dd4-Paper-Conference.pdf)]
- `DGR`: Gradient Reweighting: Towards Imbalanced Class-Incremental Learning. CVPR 2024 [[paper](https://arxiv.org/abs/2402.18528)]
- `Ease`: Expandable Subspace Ensemble for Pre-Trained Model-Based Class-Incremental Learning. CVPR 2024 [[paper](https://arxiv.org/abs/2403.12030)]
- `CoFiMA`: Weighted Ensemble Models Are Strong Continual Learners. ECCV 2024 [[paper](https://arxiv.org/abs/2312.08977)]
- `SimpleCIL`: Revisiting Class-Incremental Learning with Pre-Trained Models: Generalizability and Adaptivity are All You Need. IJCV 2024 [[paper](https://arxiv.org/abs/2303.07338)]
- `Aper`: Revisiting Class-Incremental Learning with Pre-Trained Models: Generalizability and Adaptivity are All You Need. IJCV 2024 [[paper](https://arxiv.org/abs/2303.07338)]
- `MOS`: Model Surgery for Pre-Trained Model-Based Class-Incremental Learning. AAAI 2025 [[paper](https://arxiv.org/abs/2412.09441)]
- 《微调（FineTune）》：一种基础方法，仅在新任务上更新参数。
- 《iCaRL》：增量分类器与表征学习。发表于 2017 年计算机视觉与模式识别会议（CVPR） [[论文链接](https://arxiv.org/pdf/1611.07725)]
- 《Coil》：用于类别增量学习的协同迁移方法。发表于 2021 年美国计算机协会多媒体会议（ACMMM） [[论文链接](https://arxiv.org/pdf/2107.12654)]
- 《DER》：用于类别增量学习的动态可扩展表征。发表于 2021 年计算机视觉与模式识别会议（CVPR） [[论文链接](https://arxiv.org/pdf/2103.16788)]
- 《FOSTER》：用于类别增量学习的特征增强与压缩方法。发表于 2022 年欧洲计算机视觉会议（ECCV） [[论文链接](https://arxiv.org/pdf/2204.04662)]
- 《MEMO》：一种基于 603 个范例的模型：迈向内存高效的类别增量学习。2023 年国际学习表征会议（ICLR） spotlight（亮点）论文 [[论文链接](https://openreview.net/forum?id=S07feAlQHgM)]
- 《L2P》：为持续学习学习提示信息。发表于 2022 年计算机视觉与模式识别会议（CVPR） [[论文链接](https://arxiv.org/pdf/2112.08654)]
- 《DualPrompt》：双重提示：用于无排练持续学习的互补提示方法。发表于 2022 年欧洲计算机视觉会议（ECCV） [[论文链接](https://arxiv.org/pdf/2204.04799)]
- 《CODA - Prompt》：基于持续分解注意力的提示方法，用于无排练持续学习。发表于 2023 年计算机视觉与模式识别会议（CVPR） [[论文链接](https://arxiv.org/pdf/2211.13218)]
- 《RanPAC》：随机投影与预训练模型用于持续学习。发表于 2023 年神经信息处理系统大会（NeurIPS） [[论文链接](https://arxiv.org/pdf/2307.02251)]
- 《LAE》：一种带有通用参数高效调优的统一持续学习框架。发表于 2023 年国际计算机视觉会议（ICCV） [[论文链接](https://arxiv.org/pdf/2303.10070)]
- 《SLCA》：基于预训练模型进行持续学习的带分类器对齐的慢学习器。发表于 2023 年国际计算机视觉会议（ICCV） [[论文链接](https://arxiv.org/pdf/2303.05118)]
- 《FeCAM》：在无范例持续学习中利用类别分布的异质性。发表于 2023 年神经信息处理系统大会（NeurIPS） [[论文链接](https://proceedings.neurips.cc/paper_files/paper/2023/file/15294ba2dcfb4521274f7aa1c26f4dd4-Paper-Conference.pdf)]
- 《DGR》：梯度重加权：迈向不平衡类别增量学习。发表于 2024 年计算机视觉与模式识别会议（CVPR） [[论文链接](https://arxiv.org/pdf/2402.18528)]
- 《Ease》：用于基于预训练模型的类别增量学习的可扩展子空间集成方法。发表于 2024 年计算机视觉与模式识别会议（CVPR） [[论文链接](https://arxiv.org/pdf/2403.12030)]
- 《CoFiMA》：加权集成模型是强大的持续学习器。发表于 2024 年欧洲计算机视觉会议（ECCV） [[论文链接](https://arxiv.org/pdf/2312.08977)]
- 《SimpleCIL》：重新审视基于预训练模型的类别增量学习：通用性和适应性就是你所需要的全部。发表于 2024 年《国际计算机视觉杂志》（IJCV） [[论文链接](https://arxiv.org/pdf/2303.07338)]
- 《Aper》：重新审视基于预训练模型的类别增量学习：通用性和适应性就是你所需要的全部。发表于 2024 年《国际计算机视觉杂志》（IJCV） [[论文链接](https://arxiv.org/pdf/2303.07338)]
- 《MOS》：用于基于预训练模型的类别增量学习的模型手术方法。发表于 2025 年美国人工智能协会（AAAI）会议 [[论文链接](https://arxiv.org/pdf/2412.09441)]

## 📝 Reproduced Results

#### CIFAR-100

<div align="center">
<img src="./resources/cifarb0inc10.jpg" width="600px">
</div>

#### ImageNet-R

<div align="center">
<img src="./resources/imagenetRb0inc20.jpg" width="600px">
</div>

> For exemplar parameters, Coil, DER, iCaRL, MEMO, and FOSTER set the `fixed_memory` option to false and retain the `memory_size` of 2000 for CIFAR100, while setting `fixed_memory` option to true and retaining the `memory_per_class` of 20 for ImageNet-R. On the contrary, other models are exemplar-free.

## ☄️ how to use

### 🕹️ Clone

Clone this GitHub repository:

```
git clone https://github.com/sun-hailong/LAMDA-PILOT
cd LAMDA-PILOT
```

### 🗂️ Dependencies

1. [torch 2.0.1](https://github.com/pytorch/pytorch)
2. [torchvision 0.15.2](https://github.com/pytorch/vision)
3. [timm 0.6.12](https://github.com/huggingface/pytorch-image-models)
4. [tqdm](https://github.com/tqdm/tqdm)
5. [numpy](https://github.com/numpy/numpy)
6. [scipy](https://github.com/scipy/scipy)
7. [easydict](https://github.com/makinacorpus/easydict)

### 🔑 Run experiment

1. Edit the `[MODEL NAME].json` file for global settings and hyperparameters.
2. Run:

   ```bash
   python main.py --config=./exps/[MODEL NAME].json
   ```

3. `hyper-parameters`

使用PILOT时，你可以在相应的JSON文件中编辑全局参数以及特定算法的超参数。

这些参数包括：

   - **model_name**: The model's name should be selected from the 11 methods listed above, _i.e._, `finetune`, `icarl`, `coil`, `der`, `foster`, `memo`, `simplecil`, `l2p`, `dualprompt`, `coda-prompt` and `adam`.
   - **init_cls**: The number of classes in the initial incremental stage. As the configuration of CIL includes different settings with varying class numbers at the outset, our framework accommodates diverse options for defining the initial stage.
   - **increment**: The number of classes in each incremental stage $i$, $i$ > 1. By default, the number of classes is equal across all incremental stages.
   - **backbone_type**: The backbone network of the incremental model. It can be selected from a variety of pre-trained models available in the Timm library, such as **ViT-B/16-IN1K** and **ViT-B/16-IN21K**. Both are pre-trained on ImageNet21K, while the former is additionally fine-tuned on ImageNet1K.
   - **seed**: The random seed is utilized for shuffling the class order. It is set to 1993 by default, following the benchmark setting iCaRL.
   - **fixed_memory**: a Boolean parameter. When set to true, the model will maintain a fixed amount of memory per class. Alternatively, when set to false, the model will preserve dynamic memory allocation per class.
   - **memory_size**: The total number of exemplars in the incremental learning process. If `fixed_memory` is set to false, assuming there are $K$ classes at the current stage, the model will preserve $\left[\frac{{memory-size}}{K}\right]$ exemplars for each class. **L2P, DualPrompt, SimpleCIL, ADAM, and CODA-Prompt do not require exemplars.** Therefore, parameters related to the exemplar are not utilized.
   - **memory_per_class**: If `fixed memory` is set to true, the model will preserve a fixed number of `memory_per_class` exemplars for each class.



- **模型名称（model_name）**：模型名称应从上述列出的11种方法中选取，即“微调（finetune）”、“iCaRL”、“Coil”、“DER”、“FOSTER”、“MEMO”、“SimpleCIL”、“L2P”、“DualPrompt”、“CODA-Prompt”以及“ADAM”。
- **初始类别数（init_cls）**：初始增量阶段的类别数量。由于类别增量学习（CIL）的配置在一开始就包含了类别数量不同的各种设置，我们的框架能适应定义初始阶段的多种选项。
- **增量（increment）**：每个增量阶段\(i\)（\(i > 1\)）的类别数量。默认情况下，所有增量阶段的类别数量是相等的。
- **骨干网络类型（backbone_type）**：增量模型的骨干网络。可以从Timm库中可用的各种预训练模型中进行选择，例如“视觉Transformer - B/16 - IN1K”和“视觉Transformer - B/16 - IN21K”。这两种模型都在ImageNet21K上进行了预训练，而前者还在ImageNet1K上进行了额外的微调。
- **随机种子（seed）**：随机种子用于打乱类别顺序。按照iCaRL基准设置，默认值为1993。
- **固定内存（fixed_memory）**：一个布尔型参数。当设置为“真（true）”时，模型将为每个类别维持固定的内存量。反之，当设置为“假（false）”时，模型将为每个类别保留动态内存分配。
- **内存大小（memory_size）**：增量学习过程中的范例总数。如果“固定内存（fixed_memory）”设置为“假（false）”，假设当前阶段有\(K\)个类别，模型将为每个类别保留\(\left[\frac{{内存大小（memory_size）}}{K}\right]\)个范例。“L2P”、“DualPrompt”、“SimpleCIL”、“ADAM”以及“CODA-Prompt”不需要范例。因此，与范例相关的参数不会被使用。
- **每类内存（memory_per_class）**：如果“固定内存（fixed memory）”设置为“真（true）”，模型将为每个类别保留固定数量为“每类内存（memory_per_class）”的范例。 





### 🔎 Datasets

We have implemented the pre-processing datasets as follows:

- **CIFAR100**: will be automatically downloaded by the code.
- **CUB200**: Google Drive: [link](https://drive.google.com/file/d/1XbUpnWpJPnItt5zQ6sHJnsjPncnNLvWb/view?usp=sharing) or Onedrive: [link](https://entuedu-my.sharepoint.com/:u:/g/personal/n2207876b_e_ntu_edu_sg/EVV4pT9VJ9pBrVs2x0lcwd0BlVQCtSrdbLVfhuajMry-lA?e=L6Wjsc)
- **ImageNet-R**: Google Drive: [link](https://drive.google.com/file/d/1SG4TbiL8_DooekztyCVK8mPmfhMo8fkR/view?usp=sharing) or Onedrive: [link](https://entuedu-my.sharepoint.com/:u:/g/personal/n2207876b_e_ntu_edu_sg/EU4jyLL29CtBsZkB6y-JSbgBzWF5YHhBAUz1Qw8qM2954A?e=hlWpNW)
- **ImageNet-A**: Google Drive: [link](https://drive.google.com/file/d/19l52ua_vvTtttgVRziCZJjal0TPE9f2p/view?usp=sharing) or Onedrive: [link](https://entuedu-my.sharepoint.com/:u:/g/personal/n2207876b_e_ntu_edu_sg/ERYi36eg9b1KkfEplgFTW3gBg1otwWwkQPSml0igWBC46A?e=NiTUkL)
- **OmniBenchmark**: Google Drive: [link](https://drive.google.com/file/d/1AbCP3zBMtv_TDXJypOCnOgX8hJmvJm3u/view?usp=sharing) or Onedrive: [link](https://entuedu-my.sharepoint.com/:u:/g/personal/n2207876b_e_ntu_edu_sg/EcoUATKl24JFo3jBMnTV2WcBwkuyBH0TmCAy6Lml1gOHJA?e=eCNcoA)
- **VTAB**: Google Drive: [link](https://drive.google.com/file/d/1xUiwlnx4k0oDhYi26KL5KwrCAya-mvJ_/view?usp=sharing) or Onedrive: [link](https://entuedu-my.sharepoint.com/:u:/g/personal/n2207876b_e_ntu_edu_sg/EQyTP1nOIH5PrfhXtpPgKQ8BlEFW2Erda1t7Kdi3Al-ePw?e=Yt4RnV)
- **ObjectNet**: Onedrive: [link](https://entuedu-my.sharepoint.com/:u:/g/personal/n2207876b_e_ntu_edu_sg/EZFv9uaaO1hBj7Y40KoCvYkBnuUZHnHnjMda6obiDpiIWw?e=4n8Kpy) You can also refer to the [filelist](https://drive.google.com/file/d/147Mta-HcENF6IhZ8dvPnZ93Romcie7T6/view?usp=sharing) if the file is too large to download.

> These subsets are sampled from the original datasets. Please note that I do not have the right to distribute these datasets. If the distribution violates the license, I shall provide the filenames instead.

When training **not** on `CIFAR100`, you should specify the folder of your dataset in `utils/data.py`.

```python
    def download_data(self):
        assert 0,"You should specify the folder of your dataset"
        train_dir = '[DATA-PATH]/train/'
        test_dir = '[DATA-PATH]/val/'
```
