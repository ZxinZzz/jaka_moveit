// Auto-generated. Do not edit!

// (in-package joint_motor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class image_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.detected_point_x = null;
      this.detected_point_y = null;
      this.detected_point_depth = null;
      this.area = null;
    }
    else {
      if (initObj.hasOwnProperty('detected_point_x')) {
        this.detected_point_x = initObj.detected_point_x
      }
      else {
        this.detected_point_x = new std_msgs.msg.Int64();
      }
      if (initObj.hasOwnProperty('detected_point_y')) {
        this.detected_point_y = initObj.detected_point_y
      }
      else {
        this.detected_point_y = new std_msgs.msg.Int64();
      }
      if (initObj.hasOwnProperty('detected_point_depth')) {
        this.detected_point_depth = initObj.detected_point_depth
      }
      else {
        this.detected_point_depth = new std_msgs.msg.Float64();
      }
      if (initObj.hasOwnProperty('area')) {
        this.area = initObj.area
      }
      else {
        this.area = new std_msgs.msg.Float64();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type image_data
    // Serialize message field [detected_point_x]
    bufferOffset = std_msgs.msg.Int64.serialize(obj.detected_point_x, buffer, bufferOffset);
    // Serialize message field [detected_point_y]
    bufferOffset = std_msgs.msg.Int64.serialize(obj.detected_point_y, buffer, bufferOffset);
    // Serialize message field [detected_point_depth]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.detected_point_depth, buffer, bufferOffset);
    // Serialize message field [area]
    bufferOffset = std_msgs.msg.Float64.serialize(obj.area, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type image_data
    let len;
    let data = new image_data(null);
    // Deserialize message field [detected_point_x]
    data.detected_point_x = std_msgs.msg.Int64.deserialize(buffer, bufferOffset);
    // Deserialize message field [detected_point_y]
    data.detected_point_y = std_msgs.msg.Int64.deserialize(buffer, bufferOffset);
    // Deserialize message field [detected_point_depth]
    data.detected_point_depth = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    // Deserialize message field [area]
    data.area = std_msgs.msg.Float64.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'joint_motor/image_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1f5298c36c9abfd1a7f6f23e0f3b7591';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Int64 detected_point_x
    std_msgs/Int64 detected_point_y
    std_msgs/Float64 detected_point_depth
    std_msgs/Float64 area
    ================================================================================
    MSG: std_msgs/Int64
    int64 data
    ================================================================================
    MSG: std_msgs/Float64
    float64 data
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new image_data(null);
    if (msg.detected_point_x !== undefined) {
      resolved.detected_point_x = std_msgs.msg.Int64.Resolve(msg.detected_point_x)
    }
    else {
      resolved.detected_point_x = new std_msgs.msg.Int64()
    }

    if (msg.detected_point_y !== undefined) {
      resolved.detected_point_y = std_msgs.msg.Int64.Resolve(msg.detected_point_y)
    }
    else {
      resolved.detected_point_y = new std_msgs.msg.Int64()
    }

    if (msg.detected_point_depth !== undefined) {
      resolved.detected_point_depth = std_msgs.msg.Float64.Resolve(msg.detected_point_depth)
    }
    else {
      resolved.detected_point_depth = new std_msgs.msg.Float64()
    }

    if (msg.area !== undefined) {
      resolved.area = std_msgs.msg.Float64.Resolve(msg.area)
    }
    else {
      resolved.area = new std_msgs.msg.Float64()
    }

    return resolved;
    }
};

module.exports = image_data;
