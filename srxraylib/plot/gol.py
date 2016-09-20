"""


GOL: Graphics in One Line

To make matplotlib plots in a single command line

(I am tired of polluting my code with matplotlib instructions)


"""

__author__ = "Manuel Sanchez del Rio"
__contact__ = "srio@esrf.eu"
__copyright = "ESRF, 2016"

import numpy as np
try:
    import matplotlib.pylab as plt
except:
    raise ImportError("Please install matplotlib to allow graphics")


def plot_show():
    plt.show()

def plot_image(*positional_parameters,title="TITLE",xtitle=r"X",ytitle=r"Y",cmap=None,aspect=None,show=1):

    n_arguments = len(positional_parameters)
    if n_arguments == 1:
        z = positional_parameters[0]
        x = np.arange(0,z.shape[0])
        y = np.arange(0,z.shape[0])
    elif n_arguments == 2:
        z = positional_parameters[0]
        x = positional_parameters[1]
        y = positional_parameters[1]
    elif n_arguments == 3:
        z = positional_parameters[0]
        x = positional_parameters[1]
        y = positional_parameters[2]
    else:
        raise Exception("Bad number of inputs")


    fig = plt.figure()

    # cmap = plt.cm.Greys
    plt.imshow(z.T,origin='lower',extent=[x[0],x[-1],y[0],y[-1]],cmap=cmap,aspect=aspect)
    plt.colorbar()
    ax = fig.gca()
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)

    plt.title(title)

    if show:
        plt.show()

    return fig

def plot(*positional_parameters,title="",xtitle="",ytitle="",
         xrange=None,yrange=None,show=1,legend=None,legend_position=None,color=None,marker=None,linestyle=None,
         xlog=False,ylog=False):

    n_arguments = len(positional_parameters)
    if n_arguments == 0:
        return

    fig = plt.figure()
    if n_arguments == 1:
        y = positional_parameters[0]
        x = np.arange(y.size)
        if linestyle == None:
            linestyle = '-'
        plt.plot(x,y,label=legend,marker=marker,color=color,linestyle=linestyle)
    elif n_arguments == 2:
        x = positional_parameters[0]
        y = positional_parameters[1]
        if linestyle == None:
            linestyle = '-'
        plt.plot(x,y,label=legend,color=color,marker=marker,linestyle=linestyle)
    elif n_arguments == 4:
        x1 = positional_parameters[0]
        y1 = positional_parameters[1]
        x2 = positional_parameters[2]
        y2 = positional_parameters[3]
        if legend is None:
            legend1 = None
            legend2 = None
        else:
            legend1 = legend[0]
            legend2 = legend[1]

        if color is None:
            color1 = None
            color2 = None
        else:
            color1 = color[0]
            color2 = color[1]

        if marker is None:
            marker1 = None
            marker2 = None
        else:
            marker1 = marker[0]
            marker2 = marker[1]

        if linestyle is None:
            linestyle1 = '-'
            linestyle2 = '-'
        else:
            linestyle1 = linestyle[0]
            linestyle2 = linestyle[1]

        plt.plot(x1,y1,label=legend1,marker=marker1,linestyle=linestyle1,color=color1)
        plt.plot(x2,y2,label=legend2,marker=marker2,linestyle=linestyle2,color=color2)
    elif n_arguments == 6:
        x1 = positional_parameters[0]
        y1 = positional_parameters[1]
        x2 = positional_parameters[2]
        y2 = positional_parameters[3]
        x3 = positional_parameters[4]
        y3 = positional_parameters[5]
        if legend is None:
            legend1 = None
            legend2 = None
            legend3 = None
        else:
            legend1 = legend[0]
            legend2 = legend[1]
            legend3 = legend[2]

        if color is None:
            color1 = None
            color2 = None
            color3 = None
        else:
            color1 = color[0]
            color2 = color[1]
            color3 = color[2]

        if marker is None:
            marker1 = None
            marker2 = None
            marker3 = None
        else:
            marker1 = marker[0]
            marker2 = marker[1]
            marker3 = marker[2]

        if linestyle is None:
            linestyle1 = '-'
            linestyle2 = '-'
            linestyle3 = '-'
        else:
            linestyle1 = linestyle[0]
            linestyle2 = linestyle[1]
            linestyle3 = linestyle[2]

        plt.plot(x1,y1,label=legend1,marker=marker1,linestyle=linestyle1,color=color1)
        plt.plot(x2,y2,label=legend2,marker=marker2,linestyle=linestyle2,color=color2)
        plt.plot(x3,y3,label=legend3,marker=marker3,linestyle=linestyle3,color=color3)
    else:
        "Incorrect number of arguments, plotting only two first arguments"
        x = positional_parameters[0]
        y = positional_parameters[1]
        plt.plot(x,y,label=legend)

    ax = plt.subplot(111)
    if legend is not None:
        ax.legend(bbox_to_anchor=legend_position)

    if xlog:
        ax.set_xscale("log")

    if ylog:
        ax.set_yscale("log")

    plt.xlim( xrange )
    plt.ylim( yrange )

    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)


    if show:
        plt.show()

    return fig

def plot_table(*positional_parameters,errorbars=None,xrange=None,yrange=None,
               title="",xtitle="",ytitle="",show=1,legend=None,color=None):

    n_arguments = len(positional_parameters)
    if n_arguments == 0:
        return

    fig = plt.figure()

    if n_arguments == 1:
        y = positional_parameters[0]
        x = np.arange(y.size)
        plt.plot(x,y,label=legend)
    elif n_arguments == 2:
        x = positional_parameters[0]
        y = positional_parameters[1]

        if len(y.shape) == 1:
            y = np.reshape(y,(1,y.size))
            if isinstance(legend,str):
                legend = [legend]
            if isinstance(color,str):
                color = [color]

        for i in range(y.shape[0]):
            if legend is None:
                ilegend = None
            else:
                ilegend = legend[i]

            if color is None:
                icolor = None
            else:
                icolor = color[i]

            if errorbars is None:
                plt.plot(x,y[i],label=ilegend,color=icolor)
            else:
                plt.errorbar(x,y[i],yerr=errorbars[i],label=ilegend,color=icolor)
    else:
        raise Exception("Incorrect number of arguments")


    plt.xlim( xrange )
    plt.ylim( yrange )

    if legend is not None:
        ax = plt.subplot(111)
        ax.legend(bbox_to_anchor=(1.1, 1.05))

    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)


    if show:
        plt.show()

    return fig

def plot_surface(mymode,theta,psi,title="TITLE",xtitle="",ytitle="",ztitle="",legend=None,cmap=None,show=1):

    from matplotlib import cm
    from matplotlib.ticker import LinearLocator, FormatStrFormatter
    from mpl_toolkits.mplot3d import Axes3D

    ftheta, fpsi = np.meshgrid(theta, psi)
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    II0 = mymode.T

    if cmap == None:
        cmap = cm.coolwarm

    print(II0.shape,ftheta.shape,fpsi.shape)
    surf = ax.plot_surface(ftheta, fpsi, II0, rstride=1, cstride=1, cmap=cmap,
                           linewidth=0, antialiased=False)

    ax.set_zlim(II0.min(),II0.max())
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.title(title)
    ax.set_xlabel(xtitle)
    ax.set_ylabel(ytitle)
    ax.set_zlabel(ztitle)

    if show:
        plt.show()

    return fig

def plot_scatter(x,y,show=1,nbins=100,xrange=None,yrange=None,title="",xtitle="",ytitle=""):

    from matplotlib.ticker import NullFormatter

    # the random data

    nullfmt   = NullFormatter()         # no labels

    # definitions for the axes
    left, width    = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left+width+0.02

    rect_scatter = [left, bottom, width, height]
    rect_histx   = [left, bottom_h, width, 0.2]
    rect_histy   = [left_h, bottom, 0.2, height]

    # start with a rectangular Figure
    fig = plt.figure(figsize=(8,8))

    axScatter = plt.axes(rect_scatter)
    axHistx = plt.axes(rect_histx)
    axHisty = plt.axes(rect_histy)

    # no labels
    axHistx.xaxis.set_major_formatter(nullfmt)
    axHisty.yaxis.set_major_formatter(nullfmt)

    # now determine nice limits by hand:
    binwidth = np.array([x.max() - x.min(), y.max() - y.min()]).max() / nbins

    if xrange == None:
        xrange = np.array((x.min(), x.max()))
    if yrange == None:
        yrange = np.array((y.min(), y.max()))

    # the scatter plot:
    axScatter.scatter(x, y, marker='.', edgecolor='b', s=.1)

    axScatter.set_xlabel(xtitle)
    axScatter.set_ylabel(ytitle)

    axScatter.set_xlim( xrange )
    axScatter.set_ylim( yrange )

    bins_x = np.arange(xrange[0], xrange[1] + binwidth, binwidth)
    axHistx.hist(x, bins=nbins)
    axHisty.hist(y, bins=nbins, orientation='horizontal')

    axHistx.set_xlim( axScatter.get_xlim() )

    axHistx.set_title(title)
    axHisty.set_ylim( axScatter.get_ylim() )


    if show: plt.show()

    return fig

def plot_contour(z,x,y,title="TITLE",xtitle="",ytitle="",xrange=None,yrange=None,plot_points=0,contour_levels=20,
                 cmap=None,cbar=True,fill=False,cbar_title="",show=1):

    fig = plt.figure()

    if fill:
        fig = plt.contourf(x, y, z.T, contour_levels, cmap=cmap, origin='lower')
    else:
        fig = plt.contour( x, y, z.T, contour_levels, cmap=cmap, origin='lower')

    if cbar:
        cbar = plt.colorbar(fig)
        cbar.ax.set_ylabel(cbar_title)


    plt.title(title)
    plt.xlabel(xtitle)
    plt.ylabel(ytitle)

    # the scatter plot:
    if plot_points:
        axScatter = plt.subplot(111)
        axScatter.scatter( np.outer(x,np.ones_like(y)), np.outer(np.ones_like(x),y))

    # set axes range
    plt.xlim(xrange)
    plt.ylim(yrange)

    if show:
        plt.show()

    return fig
#
# examples
#

def example_plot_image():
    x = np.linspace(-4, 4, 90)
    y = np.linspace(-4, 4, 90)
    print('Size %d pixels' % (len(x) * len(y)))
    z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
    plot_image(z,x,y,title="example_plot_image",xtitle=r"X [$\mu m$]",ytitle=r"Y [$\mu m$]",cmap=None,show=1)

def example_plot_surface():
    x = np.linspace(-4, 4, 20)
    y = np.linspace(-4, 4, 20)
    print('Size %d pixels' % (len(x) * len(y)))
    z = np.sqrt(x[np.newaxis, :]**2 + y[:, np.newaxis]**2)
    plot_surface(z,x,y,title="example_plot_surface",xtitle=r"X [$\mu m$]",ytitle=r"Y [$\mu m$]",cmap=None,show=1)

def example_plot_scatter():
    #example motivated by http://www.ster.kuleuven.be/~pieterd/python/html/core/scipystats.html
    from scipy import stats
    # x = np.random.rand(1000)
    # y = np.random.rand(1000)
    x = stats.norm.rvs(size=2000)
    y = stats.norm.rvs(scale=0.5, size=2000)
    data = np.vstack([x+y, x-y])
    plot_scatter(data[0],data[1],title="example_plot_scatter",xtitle=r"X [$\mu m$]",ytitle=r"Y [$\mu m$]",show=1)

def example_plot_contour():
    # inspired by http://stackoverflow.com/questions/10291221/axis-limits-for-scatter-plot-not-holding-in-matplotlib
    # random data
    x = np.random.randn(50)
    y = np.random.randn(100)

    X, Y = np.meshgrid(y, x)
    Z1 = plt.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
    Z2 = plt.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
    Z = 10 * (Z1 - Z2)

    plot_contour(Z,x,y,title='example_plot_contour',xtitle='x-stuff',ytitle='y-stuff',plot_points=1,show=1)

def example_plot_one_curve():
    x = np.linspace(-100,100,10)
    y = x**2
    plot(x,y,xtitle=r'$x$',title="example_plot_one_curve",
         ytitle=r'$y=f(x)=x^2$',legend="Example 1",color='pink',marker='o',linestyle=None,show=1)

def example_plot_one_curve_log():
    x = np.linspace(-100,100,10)
    y = x**2
    plot(x,y,xtitle=r'$x$',title="example_plot_one_curve",
         ytitle=r'$y=f(x)=x^2$',legend="Example 1",color='pink',marker='o',linestyle=None,xlog=1,ylog=1,show=1)

def example_plot_two_curves():
    x1 = np.linspace(-100,100,1000)
    y1 = x1**2
    x2 = np.linspace(0,200,700)
    y2 = x2**2.1
    plot(x1,y1,x2,y2,xtitle=r'$x$',title="example_plot_two_curves",
         ytitle=r'$y=f(x)$',legend=[r"$x^2$",r"$x^{2.1}$"],color=['green','blue'],marker=[' ','o'],linestyle=['-',' '],show=1)

def example_plot_table():
    x1 = np.linspace(0,100,100)
    out = np.zeros((6,x1.size))
    out[0,:] = x1**2
    out[1,:] = x1**2.1
    out[2,:] = x1**2.2
    out[3,:] = x1**2.3
    out[4,:] = x1**2.4
    out[5,:] = x1**2.5
    # another way
    # out = np.vstack( (
    #     x1**2,
    #     x1**2.1,
    #     x1**2.2,
    #     x1**2.3,
    #     x1**2.4,
    #     x1**2.5 ))
    legend=np.arange(out.shape[0]).astype("str")
    plot_table(x1,out,xtitle=r'$x$',ytitle=r'$y=f(x)$',title="example_plot_table",legend=legend,show=1)

def example_plot_table_one_curve():
    x1 = np.linspace(-100,100,1000)
    out = x1**2
    plot_table(x1,out,title="example_plot_table_one_curve",xtitle=r'$x$',ytitle=r'$y=f(x)$',legend="Example 1",color='pink',show=1)

def example_plot_table_with_errorbars():
    x = np.linspace(0,100,30)
    out = np.zeros((2,x.size))
    out[0,:] = 1e-3 * x**2
    out[1,:] = 5 + 1e-3 * x**2
    yerr = np.sqrt(out)
    yerr[1,:] = 1.0
    plot_table(x,out,errorbars=yerr,title="example_plot_table_with_errorbars",xtitle=r'$x$',ytitle=r'$y=f(x)=x^2$',xrange=[20,80],
               legend=["Statistical error","Constant error"],color=['black','magenta'],show=1)

def example_plot_image_lena():
    from scipy.misc import lena

    lena = np.rot90(lena(),-1)
    plot_image(lena,np.arange(0,lena.shape[0]),np.arange(0,lena.shape[1]),cmap='gray' )
#
# main
#
if __name__ == "__main__":
    # example_plot_one_curve()
    # example_plot_two_curves()
    # example_plot_one_curve_log()
    # example_plot_table()
    # example_plot_table_one_curve()
    # example_plot_table_with_errorbars()
    example_plot_image()
    # example_plot_surface()
    # example_plot_contour()
    # example_plot_scatter()
    example_plot_image_lena()

