# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from joint_motor/image_data.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class image_data(genpy.Message):
  _md5sum = "1f5298c36c9abfd1a7f6f23e0f3b7591"
  _type = "joint_motor/image_data"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """std_msgs/Int64 detected_point_x
std_msgs/Int64 detected_point_y
std_msgs/Float64 detected_point_depth
std_msgs/Float64 area
================================================================================
MSG: std_msgs/Int64
int64 data
================================================================================
MSG: std_msgs/Float64
float64 data"""
  __slots__ = ['detected_point_x','detected_point_y','detected_point_depth','area']
  _slot_types = ['std_msgs/Int64','std_msgs/Int64','std_msgs/Float64','std_msgs/Float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       detected_point_x,detected_point_y,detected_point_depth,area

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(image_data, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.detected_point_x is None:
        self.detected_point_x = std_msgs.msg.Int64()
      if self.detected_point_y is None:
        self.detected_point_y = std_msgs.msg.Int64()
      if self.detected_point_depth is None:
        self.detected_point_depth = std_msgs.msg.Float64()
      if self.area is None:
        self.area = std_msgs.msg.Float64()
    else:
      self.detected_point_x = std_msgs.msg.Int64()
      self.detected_point_y = std_msgs.msg.Int64()
      self.detected_point_depth = std_msgs.msg.Float64()
      self.area = std_msgs.msg.Float64()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2q2d().pack(_x.detected_point_x.data, _x.detected_point_y.data, _x.detected_point_depth.data, _x.area.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.detected_point_x is None:
        self.detected_point_x = std_msgs.msg.Int64()
      if self.detected_point_y is None:
        self.detected_point_y = std_msgs.msg.Int64()
      if self.detected_point_depth is None:
        self.detected_point_depth = std_msgs.msg.Float64()
      if self.area is None:
        self.area = std_msgs.msg.Float64()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.detected_point_x.data, _x.detected_point_y.data, _x.detected_point_depth.data, _x.area.data,) = _get_struct_2q2d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2q2d().pack(_x.detected_point_x.data, _x.detected_point_y.data, _x.detected_point_depth.data, _x.area.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.detected_point_x is None:
        self.detected_point_x = std_msgs.msg.Int64()
      if self.detected_point_y is None:
        self.detected_point_y = std_msgs.msg.Int64()
      if self.detected_point_depth is None:
        self.detected_point_depth = std_msgs.msg.Float64()
      if self.area is None:
        self.area = std_msgs.msg.Float64()
      end = 0
      _x = self
      start = end
      end += 32
      (_x.detected_point_x.data, _x.detected_point_y.data, _x.detected_point_depth.data, _x.area.data,) = _get_struct_2q2d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2q2d = None
def _get_struct_2q2d():
    global _struct_2q2d
    if _struct_2q2d is None:
        _struct_2q2d = struct.Struct("<2q2d")
    return _struct_2q2d
