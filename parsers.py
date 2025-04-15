# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

import re
import defusedxml.ElementTree as ET
from collections import namedtuple as __namedtuple__

import iso20022

__node_info__ = __namedtuple__("__node_info__", ["ns", "msgtype", "tagname", "msgtype_normalised", "data"])

# Note that we need to protect the user from etree vulns!

def parse_file(filepath, msgtype=None):

	try:
		tree = ET.parse(filepath)
	except Exception as e:
		raise iso20022.ParseError(str(e))

	return parse_etree(tree, msgtype)

def parse_xml(xml, msgtype=None):

	try:
		tree = ET.ElementTree(ET.fromstring(xml))
	except Exception as e:
		raise iso20022.ParseError(str(e))

	return parse_etree(tree, msgtype)

def parse_etree(tree, msgtype=None):

	"""
	All this class needs to do is:
	 - get the namespace
	 - ascertain the correct class for the root element
	 - Create an object of that class
	 - call parse() on that class
	   (This is fine; if we ask users to always use
	   these methods to parse, then we don't have to
	   write some sort of silly string parsing method
	   for each class)

	"""

	# Look for root document node.
	node = tree.getroot()

	# Get info from this node.
	nodeinfo = __extract_nsinfo__(node)

	# Get the class that we'll use to parse this node.
	try:
		msg_class = getattr(iso20022, nodeinfo.tagname)
	except AttributeError:
		try:
			msg_class_outer = getattr(iso20022, nodeinfo.msgtype_normalised)
			msg_class = getattr(msg_class_outer, nodeinfo.tagname)
		except AttributeError:
			raise iso20022.ParseError(f"No class for messages of type {nodeinfo.msgtype+':' if nodeinfo.msgtype is not None else ''}{classname}")

	# Create a new item of this class.
	msg = msg_class(data=nodeinfo.data, tag = nodeinfo.tagname, ns=nodeinfo.ns)
	msg.parse(node)

	return msg

def __extract_nsinfo__(node):

	# Attempt to pull out namespace and tag type.
	try:
		matches = re.match(r"^(\{(([^\{\}:]*:)*([^\{\}:]*))\})?([^\{\}:]*)$", node.tag)
	except:
		raise ValueError(f"Could not extract info from node {node}")
	else:
		ns = matches.group(2)
		msgtype = matches.group(4)
		tagname = matches.group(5)
		normalised_msgtype = None if msgtype is None else msgtype.replace(".", "_").upper()

		return __node_info__(ns, msgtype, tagname, normalised_msgtype, node.text)