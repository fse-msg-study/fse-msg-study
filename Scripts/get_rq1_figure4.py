import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
def plot_ratios_bleu(data, name):
    bleus = [i / 10 for i in range(0, 10)]
    plt.figure()
    for i in range(len(model_names)):
        plt.plot(bleus, data[i], label=model_names[i])  
    plt.xlabel('x label')
    plt.ylabel('y label')
    plt.title("Simple Plot")
    plt.legend()
    plt.savefig('%s.png'%name)
if __name__ == '__main__':
    model_names = ['nmt', 'ptrgn', 'codisum', 'coregen']
    output_names = {'nmt':'NMT', 'ptrgn':'PtrGNCMsg', 'codisum':'CODISUM', 'coregen':'CoreGen'}

    total_ratios_train = []
    total_ratios_test = []
    
    for i in range(len(model_names)):
        model_name = model_names[i]
        cur_ratios_train = eval(open('../Patterns/pattern_bleu_%s_train'%model_name).read())
        cur_ratios_train = [float(x) for x in cur_ratios_train]
        cur_ratios_train = [float(x) * 100 for x in cur_ratios_train]
        cur_ratios_test = eval(open('../Patterns/pattern_bleu_%s_test'%model_name).read())
        cur_ratios_test = [float(x) for x in cur_ratios_test]
        cur_ratios_test = [float(x) * 100 for x in cur_ratios_test]

        total_ratios_train.append(cur_ratios_train)
        total_ratios_test.append(cur_ratios_test)
        bleus = [i * 10 for i in range(0, 10)]
    # mpl.style.use('seaborn')
    plt.figure()
    CB91_Blue = '#2CBDFE'
    CB91_Green = '#47DBCD'
    CB91_Pink = '#F3A0F2'
    CB91_Purple = '#9D2EC5'
    CB91_Violet = '#661D98'
    CB91_Amber = '#F5B14C'    
    # colors = ['b', 'g', CB91_Pink, 'c']
    colors = ['b', 'g', 'c', CB91_Amber]
    for i in range(len(model_names)):
        plt.plot(bleus, total_ratios_train[i], color=colors[i], linewidth=2, label=output_names[model_names[i]] + '-train')  
    for i in range(len(model_names)):
        plt.plot(bleus, total_ratios_test[i], color=colors[i], linestyle='--', linewidth=2, label=output_names[model_names[i]] + '-test')  
    # plt.ylim(top=1)
    plt.xlabel('BLEU')
    plt.ylabel('Ratio of patterns (%)')
    # plt.title("")
    leg = plt.legend(fontsize=8,frameon=False, ncol =2)
    # prop=dict(weight='bold')
    # plt.savefig('pattern_bleu.pdf')
    plt.savefig('TablesAndFigures/rq1_figure4.png')
