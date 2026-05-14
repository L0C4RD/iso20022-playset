# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._Party50Choice import Party50Choice

class GroupHeader117(base_types._BaseFieldType):

	__slots__ = ["_CreDtTm", "_MsgId", "_MsgSndr"]
	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if type(value) != base_types.auto else self.make_default("CreDtTm")

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def MsgSndr(self):
		return self._MsgSndr

	@MsgSndr.setter
	def MsgSndr(self, value):
		self._MsgSndr = value if type(value) != base_types.auto else self.make_default("MsgSndr")

	@MsgSndr.deleter
	def MsgSndr(self):
		del self._MsgSndr
		self._MsgSndr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSndr', type=Party50Choice, min=0, max=1, mutex_group=None, array=False),
	))