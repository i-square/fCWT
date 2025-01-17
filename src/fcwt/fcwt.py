# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _fcwt
else:
    import _fcwt

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


FCWT_LINSCALES = _fcwt.FCWT_LINSCALES
FCWT_LOGSCALES = _fcwt.FCWT_LOGSCALES
FCWT_LINFREQS = _fcwt.FCWT_LINFREQS
class Wavelet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self):
        _fcwt.Wavelet_swiginit(self, _fcwt.new_Wavelet())

    def generate(self, *args):
        return _fcwt.Wavelet_generate(self, *args)

    def getSupport(self, scale):
        return _fcwt.Wavelet_getSupport(self, scale)

    def getWavelet(self, scale, pwav):
        return _fcwt.Wavelet_getWavelet(self, scale, pwav)
    width = property(_fcwt.Wavelet_width_get, _fcwt.Wavelet_width_set)
    four_wavelen = property(_fcwt.Wavelet_four_wavelen_get, _fcwt.Wavelet_four_wavelen_set)
    imag_frequency = property(_fcwt.Wavelet_imag_frequency_get, _fcwt.Wavelet_imag_frequency_set)
    doublesided = property(_fcwt.Wavelet_doublesided_get, _fcwt.Wavelet_doublesided_set)
    mother = property(_fcwt.Wavelet_mother_get, _fcwt.Wavelet_mother_set)
    __swig_destroy__ = _fcwt.delete_Wavelet

# Register Wavelet in _fcwt:
_fcwt.Wavelet_swigregister(Wavelet)

class Morlet(Wavelet):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, bandwidth):
        _fcwt.Morlet_swiginit(self, _fcwt.new_Morlet(bandwidth))

    def generate(self, *args):
        return _fcwt.Morlet_generate(self, *args)

    def getSupport(self, scale):
        return _fcwt.Morlet_getSupport(self, scale)

    def getWavelet(self, scale, pwav):
        return _fcwt.Morlet_getWavelet(self, scale, pwav)
    fb = property(_fcwt.Morlet_fb_get, _fcwt.Morlet_fb_set)
    __swig_destroy__ = _fcwt.delete_Morlet

# Register Morlet in _fcwt:
_fcwt.Morlet_swigregister(Morlet)

class Scales(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, pwav, st, fs, f0, f1, fn):
        _fcwt.Scales_swiginit(self, _fcwt.new_Scales(pwav, st, fs, f0, f1, fn))

    def getScales(self, pfreqs):
        return _fcwt.Scales_getScales(self, pfreqs)

    def getFrequencies(self, pfreqs):
        return _fcwt.Scales_getFrequencies(self, pfreqs)
    scales = property(_fcwt.Scales_scales_get, _fcwt.Scales_scales_set)
    fs = property(_fcwt.Scales_fs_get, _fcwt.Scales_fs_set)
    nscales = property(_fcwt.Scales_nscales_get, _fcwt.Scales_nscales_set)
    __swig_destroy__ = _fcwt.delete_Scales

# Register Scales in _fcwt:
_fcwt.Scales_swigregister(Scales)

class FCWT(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, pwav, pthreads, puse_optimalization_schemes, puse_normalization):
        _fcwt.FCWT_swiginit(self, _fcwt.new_FCWT(pwav, pthreads, puse_optimalization_schemes, puse_normalization))

    def create_FFT_optimization_plan(self, pmaxsize, poptimizationflags):
        return _fcwt.FCWT_create_FFT_optimization_plan(self, pmaxsize, poptimizationflags)

    def cwt(self, pinput, scales, poutput):
        return _fcwt.FCWT_cwt(self, pinput, scales, poutput)

    def ccwt(self, pcinput, scales, poutput):
        return _fcwt.FCWT_ccwt(self, pcinput, scales, poutput)
    wavelet = property(_fcwt.FCWT_wavelet_get, _fcwt.FCWT_wavelet_set)
    __swig_destroy__ = _fcwt.delete_FCWT

# Register FCWT in _fcwt:
_fcwt.FCWT_swigregister(FCWT)



