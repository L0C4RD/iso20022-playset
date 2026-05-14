# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text

class OriginalMessageAndIssuer1(base_types._BaseFieldType):

	__slots__ = ["_MsgId", "_MsgNmId", "_OrgtrNm"]
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
	def MsgNmId(self):
		return self._MsgNmId

	@MsgNmId.setter
	def MsgNmId(self, value):
		self._MsgNmId = value if type(value) != base_types.auto else self.make_default("MsgNmId")

	@MsgNmId.deleter
	def MsgNmId(self):
		del self._MsgNmId
		self._MsgNmId = None

	@property
	def OrgtrNm(self):
		return self._OrgtrNm

	@OrgtrNm.setter
	def OrgtrNm(self, value):
		self._OrgtrNm = value if type(value) != base_types.auto else self.make_default("OrgtrNm")

	@OrgtrNm.deleter
	def OrgtrNm(self):
		del self._OrgtrNm
		self._OrgtrNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgNmId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgtrNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
	))